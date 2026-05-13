"""
Workflow YAML Loader - 从 YAML 文件加载工作流
"""
import os
import json
import logging
from typing import Dict, List, Any, Optional

logger = logging.getLogger(__name__)


class WorkflowLoader:
    """工作流加载器 (简化版 - 支持 YAML 和 JSON 格式)"""
    
    def __init__(self, workflows_dir: Optional[str] = None):
        if workflows_dir is None:
            parent_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
            self.workflows_dir = os.path.join(parent_dir, 'ai-agent', 'workflows')
        else:
            self.workflows_dir = workflows_dir
        
        self.workflows: Dict[str, Dict] = {}
        self._load_all_workflows()
    
    def _load_all_workflows(self):
        """加载所有工作流文件"""
        if not os.path.exists(self.workflows_dir):
            logger.warning(f"Workflows directory not found: {self.workflows_dir}")
            return
        
        for filename in os.listdir(self.workflows_dir):
            if filename.endswith('.yaml') or filename.endswith('.yml'):
                workflow_path = os.path.join(self.workflows_dir, filename)
                try:
                    workflow_data = self._load_yaml_simple(workflow_path)
                    if workflow_data:
                        workflow_name = workflow_data.get('name', filename.replace('.yaml', ''))
                        self.workflows[workflow_name] = workflow_data
                        logger.info(f"Loaded workflow: {workflow_name}")
                except Exception as e:
                    logger.warning(f"Failed to load workflow {filename}: {e}")
            elif filename.endswith('.json'):
                workflow_path = os.path.join(self.workflows_dir, filename)
                try:
                    with open(workflow_path, 'r', encoding='utf-8') as f:
                        workflow_data = json.load(f)
                        workflow_name = workflow_data.get('name', filename.replace('.json', ''))
                        self.workflows[workflow_name] = workflow_data
                        logger.info(f"Loaded workflow: {workflow_name}")
                except Exception as e:
                    logger.warning(f"Failed to load workflow {filename}: {e}")
    
    def _load_yaml_simple(self, file_path: str) -> Dict:
        """简单的 YAML 加载器（使用 json 作为备选）"""
        try:
            import yaml
            with open(file_path, 'r', encoding='utf-8') as f:
                return yaml.safe_load(f)
        except ImportError:
            logger.info("pyyaml not available, trying to parse YAML manually")
            return self._parse_yaml_manually(file_path)
    
    def _parse_yaml_manually(self, file_path: str) -> Dict:
        """手动解析简单的 YAML 格式"""
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        result = {}
        current_key = None
        current_list = []
        
        for line in lines:
            stripped = line.strip()
            if not stripped or stripped.startswith('#'):
                continue
            
            if ':' in stripped and not stripped.startswith('-'):
                if current_key and current_list:
                    result[current_key] = current_list
                parts = stripped.split(':', 1)
                current_key = parts[0].strip()
                if len(parts) > 1:
                    value = parts[1].strip().strip('"').strip("'")
                    if value:
                        result[current_key] = value
                    else:
                        current_list = []
            
            elif stripped.startswith('-'):
                item = stripped[1:].strip().strip('"').strip("'")
                if ':' in item:
                    parts = item.split(':', 1)
                    current_list.append({parts[0].strip(): parts[1].strip() if len(parts) > 1 else ''})
                else:
                    current_list.append(item)
        
        if current_key and current_list:
            result[current_key] = current_list
        
        return result
    
    def get_workflow(self, name: str) -> Optional[Dict]:
        """获取指定名称的工作流"""
        return self.workflows.get(name)
    
    def list_workflows(self) -> List[str]:
        """列出所有可用工作流"""
        return list(self.workflows.keys())
    
    def execute_workflow(self, name: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """执行指定工作流"""
        workflow = self.get_workflow(name)
        if not workflow:
            return {"status": "error", "message": f"Workflow '{name}' not found"}
        
        return self._execute_phases(workflow, context)
    
    def _execute_phases(self, workflow: Dict, context: Dict) -> Dict[str, Any]:
        """执行工作流的各个阶段"""
        results = {
            "workflow": workflow.get('name'),
            "phases": [],
            "status": "completed"
        }
        
        for phase in workflow.get('phases', []):
            phase_result = {
                "phase": phase.get('name'),
                "tasks": []
            }
            
            for task in phase.get('tasks', []):
                task_result = {
                    "task_id": task.get('id'),
                    "executed": True,
                    "skill": task.get('skill')
                }
                phase_result["tasks"].append(task_result)
            
            results["phases"].append(phase_result)
        
        return results
