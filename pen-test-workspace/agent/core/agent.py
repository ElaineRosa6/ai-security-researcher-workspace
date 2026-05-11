"""
Agent Core - Main Agent Class
Expert-level AI Security Researcher Agent
"""

import json
import logging
from datetime import datetime
from typing import Dict, List, Optional, Any
from pathlib import Path

from .brain import Brain
from .memory import MemoryManager
from .knowledge import KnowledgeGraph
from .workflow import WorkflowEngine, StateTracker
from .quality import Validator, SelfAssessment, Auditor
from .awareness import AgentAwareness
from .meta import MetaSystem

logger = logging.getLogger(__name__)


class SecurityExpertAgent:
    """Main Agent class for Security Expert operations"""
    
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.session_id = self._generate_session_id()
        self.start_time = None
        
        self.memory = MemoryManager(config.get('memory', {}))
        self.knowledge = KnowledgeGraph()
        self.state_tracker = StateTracker()
        self.workflow_engine = WorkflowEngine(self.state_tracker, self.memory)
        self.brain = Brain(self.memory, self.knowledge, self.state_tracker)
        self.validator = Validator()
        self.auditor = Auditor(self.session_id)
        self.self_assessment = SelfAssessment([], self.memory)
        self.awareness = AgentAwareness(self.state_tracker, self.memory)
        self.meta_system = MetaSystem()
        
        self.target_profile = {}
        self.discoveries = []
        self.execution_history = []
        
    def _generate_session_id(self) -> str:
        """Generate unique session ID"""
        return f"session_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    
    def initialize(self) -> Dict[str, Any]:
        """Initialize the agent"""
        self.start_time = datetime.now()
        self.state_tracker.transition_to("INITIALIZED", "Agent initialized")
        
        logger.info(f"Agent initialized with session ID: {self.session_id}")
        
        return {
            "status": "initialized",
            "session_id": self.session_id,
            "start_time": self.start_time.isoformat(),
            "capabilities": self.config.get('capabilities', [])
        }
    
    def start_task(self, user_requirement: str) -> Dict[str, Any]:
        """Start processing a security testing task"""
        logger.info(f"Starting task: {user_requirement}")
        
        self.state_tracker.transition_to("REQUIREMENT_ANALYSIS", "User requirement received")
        
        requirement = self.brain.parse_requirement(user_requirement)
        
        self.memory.store({
            "requirement": requirement,
            "timestamp": datetime.now().isoformat()
        }, "short_term")
        
        self.state_tracker.transition_to("PLANNING", "Requirement analysis complete")
        
        plan = self.brain.create_task_plan(requirement)
        
        self.memory.store({
            "plan": plan,
            "timestamp": datetime.now().isoformat()
        }, "medium_term")
        
        result = self.execute_plan(plan)
        
        return result
    
    def execute_plan(self, plan: Dict[str, Any]) -> Dict[str, Any]:
        """Execute the task plan"""
        self.state_tracker.transition_to("RECON", "Starting plan execution")
        
        results = {
            "session_id": self.session_id,
            "plan": plan,
            "executions": [],
            "discoveries": [],
            "status": "in_progress"
        }
        
        for phase in plan.get('phases', []):
            phase_name = phase.get('name')
            logger.info(f"Executing phase: {phase_name}")
            
            self.state_tracker.update_context("current_phase", phase_name)
            
            for task in phase.get('tasks', []):
                task_result = self.execute_task(task)
                results['executions'].append(task_result)
                
                if task_result.get('status') == 'success':
                    self.discoveries.extend(task_result.get('discoveries', []))
        
        self.state_tracker.transition_to("REPORTING", "Plan execution complete")
        
        report = self.generate_report(results)
        results['report'] = report
        results['status'] = 'completed'
        
        return results
    
    def execute_task(self, task: Dict[str, Any]) -> Dict[str, Any]:
        """Execute a single task"""
        task_id = task.get('id', 'unknown')
        logger.info(f"Executing task: {task_id}")
        
        execution_record = {
            "task_id": task_id,
            "task_name": task.get('name'),
            "start_time": datetime.now().isoformat(),
            "status": "in_progress",
            "actions": []
        }
        
        try:
            skill_name = task.get('skill')
            if skill_name:
                skill_result = self.brain.execute_skill(skill_name, task)
                execution_record['result'] = skill_result
                execution_record['status'] = 'success'
                execution_record['discoveries'] = skill_result.get('discoveries', [])
            else:
                execution_record['status'] = 'skipped'
                execution_record['reason'] = 'No skill specified'
                
        except Exception as e:
            logger.error(f"Task execution failed: {e}")
            execution_record['status'] = 'failed'
            execution_record['error'] = str(e)
            
            self.handle_failure(execution_record)
        
        execution_record['end_time'] = datetime.now().isoformat()
        self.execution_history.append(execution_record)
        
        return execution_record
    
    def handle_failure(self, execution_record: Dict[str, Any]) -> None:
        """Handle task execution failure"""
        self.state_tracker.transition_to("ERROR", f"Task failed: {execution_record.get('error')}")
        
        self.auditor.log_decision({
            "type": "failure",
            "execution": execution_record,
            "timestamp": datetime.now().isoformat()
        })
        
        self.memory.store({
            "failure": execution_record,
            "timestamp": datetime.now().isoformat()
        }, "medium_term")
    
    def generate_report(self, results: Dict[str, Any]) -> Dict[str, Any]:
        """Generate final report"""
        self.state_tracker.transition_to("COMPLETED", "Task completed")
        
        report = {
            "session_id": self.session_id,
            "generated_at": datetime.now().isoformat(),
            "executive_summary": self._generate_executive_summary(results),
            "findings": self.discoveries,
            "execution_summary": {
                "total_tasks": len(results.get('executions', [])),
                "successful": len([e for e in results.get('executions', []) if e.get('status') == 'success']),
                "failed": len([e for e in results.get('executions', []) if e.get('status') == 'failed'])
            },
            "state_history": self.state_tracker.get_state_history(),
            "recommendations": self._generate_recommendations()
        }
        
        self.auditor.log_decision({
            "type": "report_generated",
            "report_summary": report['executive_summary'],
            "timestamp": datetime.now().isoformat()
        })
        
        return report
    
    def _generate_executive_summary(self, results: Dict[str, Any]) -> str:
        """Generate executive summary"""
        total_tasks = len(results.get('executions', []))
        successful = len([e for e in results.get('executions', []) if e.get('status') == 'success'])
        findings_count = len(self.discoveries)
        
        return f"Completed security assessment with {successful}/{total_tasks} tasks successful. Found {findings_count} security findings."
    
    def _generate_recommendations(self) -> List[str]:
        """Generate recommendations based on findings"""
        recommendations = []
        
        if any(d.get('severity') == 'critical' for d in self.discoveries):
            recommendations.append("Immediate action required for critical vulnerabilities")
        
        if any(d.get('type') == 'sql_injection' for d in self.discoveries):
            recommendations.append("Implement parameterized queries to prevent SQL injection")
        
        if any(d.get('type') == 'xss' for d in self.discoveries):
            recommendations.append("Implement input validation and output encoding")
        
        return recommendations
    
    def get_status(self) -> Dict[str, Any]:
        """Get current agent status"""
        return self.awareness.get_self_status()
    
    def pause(self) -> None:
        """Pause agent execution"""
        self.state_tracker.transition_to("PAUSED", "Agent paused by user")
        logger.info("Agent execution paused")
    
    def resume(self) -> None:
        """Resume agent execution"""
        last_state = self.state_tracker.get_last_active_state()
        self.state_tracker.transition_to(last_state, "Agent resumed")
        logger.info("Agent execution resumed")
