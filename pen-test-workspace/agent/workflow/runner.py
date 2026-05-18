"""
Workflow Runner - 完整的工作流执行引擎
"""
import logging
from typing import Dict, List, Optional, Any
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed
import threading

from agent.workflow.engine import StateTracker
from agent.core import Brain
from agent.workflow.yaml_loader import WorkflowLoader

logger = logging.getLogger(__name__)


class TaskStatus:
    """任务状态枚举"""
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    SKIPPED = "skipped"


class WorkflowRunner:
    """工作流执行器"""
    
    def __init__(self, brain: Brain, state_tracker: StateTracker = None):
        self.brain = brain
        self.state_tracker = state_tracker or StateTracker()
        self.loader = WorkflowLoader()
        self.lock = threading.RLock()
        
        # 任务追踪
        self.current_workflow: Optional[Dict] = None
        self.current_phase: Optional[Dict] = None
        self.task_results: Dict[str, Dict] = {}
        self.execution_history: List[Dict] = []
        
        # 并发控制
        self.max_workers = 3
        self.executor: Optional[ThreadPoolExecutor] = None
    
    def load_workflow(self, workflow_name: str) -> Optional[Dict]:
        """加载并验证工作流"""
        workflow = self.loader.get_workflow(workflow_name)
        if not workflow:
            logger.error(f"Workflow not found: {workflow_name}")
            return None
        
        # 验证工作流
        if not self._validate_workflow(workflow):
            return None
        
        self.current_workflow = workflow
        logger.info(f"Loaded workflow: {workflow_name}")
        return workflow
    
    def list_available_workflows(self) -> List[str]:
        """列出所有可用的工作流"""
        return self.loader.list_workflows()
    
    def _validate_workflow(self, workflow: Dict) -> bool:
        """验证工作流定义"""
        required_fields = ['name', 'phases']
        for field in required_fields:
            if field not in workflow:
                logger.error(f"Workflow missing required field: {field}")
                return False
        
        # 验证每个阶段
        for phase in workflow.get('phases', []):
            if not phase.get('name'):
                logger.warning("Phase missing name")
            
            for task in phase.get('tasks', []):
                if not task.get('id'):
                    logger.warning("Task missing ID")
                if not task.get('skill'):
                    logger.warning(f"Task {task.get('id')} missing skill")
        
        return True
    
    def execute_workflow(self, workflow_name: str, context: Dict[str, Any] = None) -> Dict[str, Any]:
        """完整执行工作流"""
        context = context or {}
        
        logger.info(f"Starting workflow: {workflow_name}")
        
        workflow = self.load_workflow(workflow_name)
        if not workflow:
            return self._create_error_result(f"Workflow '{workflow_name}' not found")
        
        start_time = datetime.now()
        result = {
            "workflow": workflow_name,
            "start_time": start_time.isoformat(),
            "phases": [],
            "status": "running",
            "context": context
        }
        
        try:
            # 重置状态
            self.state_tracker.reset()
            self.task_results = {}
            
            # 执行所有阶段
            phases = sorted(workflow.get('phases', []), key=lambda p: p.get('order', 999))
            
            for phase in phases:
                phase_result = self._execute_phase(phase, context)
                result["phases"].append(phase_result)
                
                # 检查是否需要停止
                if phase_result["status"] == "failed":
                    logger.error(f"Phase {phase.get('name')} failed, stopping workflow")
                    result["status"] = "failed"
                    break
            
            if result["status"] == "running":
                result["status"] = "completed"
            
            # 生成报告
            result["report"] = self._generate_report(result, context)
            
        except Exception as e:
            logger.exception(f"Workflow execution error: {e}")
            result["status"] = "failed"
            result["error"] = str(e)
        
        result["end_time"] = datetime.now().isoformat()
        result["duration"] = (datetime.now() - start_time).total_seconds()
        
        # 保存历史
        self.execution_history.append(result)
        
        return result
    
    def _execute_phase(self, phase: Dict, context: Dict[str, Any]) -> Dict[str, Any]:
        """执行单个阶段"""
        phase_name = phase.get('name', 'unknown')
        self.current_phase = phase
        
        logger.info(f"Executing phase: {phase_name}")
        
        result = {
            "phase": phase_name,
            "start_time": datetime.now().isoformat(),
            "tasks": [],
            "status": "running"
        }
        
        # 检查依赖关系
        if not self._check_dependencies(phase):
            result["status"] = "skipped"
            result["reason"] = "Dependencies not met"
            logger.warning(f"Phase {phase_name} skipped due to dependencies")
            return result
        
        # 执行任务
        tasks = phase.get('tasks', [])
        
        if phase.get('parallel'):
            # 并行执行
            task_results = self._execute_tasks_parallel(tasks, context)
        else:
            # 串行执行
            task_results = self._execute_tasks_serial(tasks, context)
        
        result["tasks"] = task_results
        
        # 检查阶段结果
        failed_tasks = [t for t in task_results if t["status"] == TaskStatus.FAILED]
        
        if failed_tasks:
            if phase.get('continue_on_error'):
                result["status"] = "completed_with_errors"
            else:
                result["status"] = "failed"
        else:
            result["status"] = "completed"
        
        result["end_time"] = datetime.now().isoformat()
        
        logger.info(f"Phase {phase_name} completed with status: {result['status']}")
        
        return result
    
    def _check_dependencies(self, phase: Dict) -> bool:
        """检查阶段依赖是否满足"""
        depends_on = phase.get('depends_on', [])
        
        if not depends_on:
            return True
        
        # 检查之前的阶段是否完成
        for dep in depends_on:
            # 查找依赖的阶段结果
            dep_completed = False
            for hist in reversed(self.execution_history):
                for phase_result in hist.get("phases", []):
                    if phase_result["phase"] == dep:
                        if phase_result["status"] in ["completed", "completed_with_errors"]:
                            dep_completed = True
                            break
                if dep_completed:
                    break
            
            if not dep_completed:
                logger.warning(f"Dependency not met: {dep}")
                return False
        
        return True
    
    def _execute_tasks_serial(self, tasks: List[Dict], context: Dict[str, Any]) -> List[Dict]:
        """串行执行任务"""
        results = []
        
        for task in tasks:
            task_result = self._execute_task(task, context)
            results.append(task_result)
            
            # 检查是否需要继续
            if task_result["status"] == TaskStatus.FAILED:
                if not task.get('continue_on_error'):
                    logger.warning(f"Task {task.get('id')} failed, stopping phase")
                    break
        
        return results
    
    def _execute_tasks_parallel(self, tasks: List[Dict], context: Dict[str, Any]) -> List[Dict]:
        """并行执行任务"""
        results = []
        futures = []
        
        self.executor = ThreadPoolExecutor(max_workers=self.max_workers)
        
        try:
            for task in tasks:
                future = self.executor.submit(self._execute_task, task, context)
                futures.append((task, future))
            
            # 收集结果
            for task, future in futures:
                try:
                    task_result = future.result()
                    results.append(task_result)
                except Exception as e:
                    logger.exception(f"Task {task.get('id')} error: {e}")
                    results.append({
                        "task_id": task.get('id'),
                        "status": TaskStatus.FAILED,
                        "error": str(e),
                        "timestamp": datetime.now().isoformat()
                    })
        
        finally:
            self.executor.shutdown(wait=True)
            self.executor = None
        
        return results
    
    def _execute_task(self, task: Dict, context: Dict[str, Any]) -> Dict[str, Any]:
        """执行单个任务"""
        task_id = task.get('id')
        skill_path = task.get('skill')
        
        logger.info(f"Executing task: {task_id} ({skill_path})")
        
        result = {
            "task_id": task_id,
            "name": task.get('name'),
            "skill": skill_path,
            "status": TaskStatus.RUNNING,
            "start_time": datetime.now().isoformat()
        }
        
        try:
            params = {
                **task.get('params', {}),
                **context
            }
            
            # 通过 Brain 执行技能
            skill_result = self.brain.execute_skill(skill_path, {"params": params})
            
            result["result"] = skill_result
            result["status"] = TaskStatus.COMPLETED
            
            # 保存任务结果
            with self.lock:
                self.task_results[task_id] = skill_result
            
        except Exception as e:
            logger.exception(f"Task {task_id} failed: {e}")
            result["status"] = TaskStatus.FAILED
            result["error"] = str(e)
        
        result["end_time"] = datetime.now().isoformat()
        return result
    
    def pause(self) -> bool:
        """暂停工作流"""
        logger.info("Pausing workflow")
        
        if self.executor:
            self.executor.shutdown(wait=False)
        
        self.state_tracker.transition_to("PAUSED", "User paused workflow")
        return True
    
    def resume(self) -> bool:
        """恢复工作流"""
        logger.info("Resuming workflow")
        
        last_state = self.state_tracker.get_last_active_state()
        self.state_tracker.transition_to(last_state, "User resumed workflow")
        return True
    
    def get_status(self) -> Dict[str, Any]:
        """获取当前执行状态"""
        return {
            "workflow": self.current_workflow.get('name') if self.current_workflow else None,
            "phase": self.current_phase.get('name') if self.current_phase else None,
            "state": self.state_tracker.get_current_state(),
            "task_count": len(self.task_results),
            "history_count": len(self.execution_history)
        }
    
    def get_task_result(self, task_id: str) -> Optional[Dict]:
        """获取特定任务的结果"""
        with self.lock:
            return self.task_results.get(task_id)
    
    def _generate_report(self, workflow_result: Dict, context: Dict) -> Dict:
        """生成执行报告"""
        total_tasks = 0
        completed_tasks = 0
        failed_tasks = 0
        skipped_tasks = 0
        discoveries = []
        
        for phase in workflow_result.get("phases", []):
            for task in phase.get("tasks", []):
                total_tasks += 1
                
                if task["status"] == TaskStatus.COMPLETED:
                    completed_tasks += 1
                    
                    # 收集发现
                    if "result" in task:
                        task_discoveries = task["result"].get("discoveries", [])
                        if task_discoveries:
                            if isinstance(task_discoveries, list):
                                discoveries.extend(task_discoveries)
                            else:
                                discoveries.append(task_discoveries)
                
                elif task["status"] == TaskStatus.FAILED:
                    failed_tasks += 1
                
                elif task["status"] == TaskStatus.SKIPPED:
                    skipped_tasks += 1
        
        return {
            "summary": {
                "total_tasks": total_tasks,
                "completed": completed_tasks,
                "failed": failed_tasks,
                "skipped": skipped_tasks,
                "success_rate": completed_tasks / total_tasks if total_tasks > 0 else 0
            },
            "discoveries": discoveries,
            "context": context
        }


class ResultParser:
    """工作流结果解析器"""
    
    @staticmethod
    def parse(workflow_result: Dict) -> Dict:
        """解析完整的工作流结果"""
        phases = workflow_result.get("phases", [])
        all_results = []
        all_errors = []
        
        for phase in phases:
            for task in phase.get("tasks", []):
                if task.get("result"):
                    all_results.append({
                        "phase": phase.get("phase"),
                        "task": task.get("task_id"),
                        "result": task.get("result")
                    })
                
                if task.get("error"):
                    all_errors.append({
                        "phase": phase.get("phase"),
                        "task": task.get("task_id"),
                        "error": task.get("error")
                    })
        
        return {
            "summary": workflow_result.get("report", {}),
            "task_results": all_results,
            "errors": all_errors,
            "timing": {
                "start": workflow_result.get("start_time"),
                "end": workflow_result.get("end_time"),
                "duration": workflow_result.get("duration")
            }
        }
    
    @staticmethod
    def get_discoveries(workflow_result: Dict) -> List[Dict]:
        """提取所有发现"""
        report = workflow_result.get("report", {})
        return report.get("discoveries", [])
    
    @staticmethod
    def to_markdown(workflow_result: Dict) -> str:
        """转换为 Markdown 报告"""
        parsed = ResultParser.parse(workflow_result)
        summary = parsed.get("summary", {})
        report_summary = summary.get("summary", {})
        
        lines = [
            "# Workflow Execution Report",
            "",
            f"**Workflow**: {workflow_result.get('workflow', 'unknown')}",
            "",
            f"- **Duration**: {summary.get('duration', 0):.2f}s",
            f"- **Status**: {workflow_result.get('status')}",
            f"- **Total Tasks**: {report_summary.get('total_tasks', 0)}",
            f"- **Completed**: {report_summary.get('completed', 0)} ✅",
            f"- **Failed**: {report_summary.get('failed', 0)} ❌",
            "",
        ]
        
        if summary.get('discoveries'):
            lines.append("## Discoveries")
            for disc in summary['discoveries']:
                lines.append(f"- {str(disc)}")
            lines.append("")
        
        if parsed.get("errors"):
            lines.append("## Errors")
            for err in parsed["errors"]:
                lines.append(f"- **{err['task']}**: {err['error']}")
        
        return "\n".join(lines)

