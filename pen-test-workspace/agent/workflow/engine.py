"""
Workflow Engine - State Management and Flow Control
"""

import json
import logging
from typing import Dict, List, Optional, Any, Callable
from datetime import datetime
from enum import Enum

logger = logging.getLogger(__name__)


class State(str, Enum):
    """Agent state enumeration"""
    INITIALIZED = "INITIALIZED"
    REQUIREMENT_ANALYSIS = "REQUIREMENT_ANALYSIS"
    PLANNING = "PLANNING"
    RECON = "RECON"
    SCANNING = "SCANNING"
    VULN_ASSESS = "VULN_ASSESS"
    EXPLOITATION = "EXPLOITATION"
    POST_EXPLOIT = "POST_EXPLOIT"
    REPORTING = "REPORTING"
    COMPLETED = "COMPLETED"
    PAUSED = "PAUSED"
    BLOCKED = "BLOCKED"
    ERROR = "ERROR"


class StateTracker:
    """Tracks agent state and history"""
    
    TRANSITION_RULES = {
        "INITIALIZED": ["REQUIREMENT_ANALYSIS"],
        "REQUIREMENT_ANALYSIS": ["PLANNING"],
        "PLANNING": ["RECON", "ERROR"],
        "RECON": ["SCANNING", "PLANNING", "ERROR"],
        "SCANNING": ["VULN_ASSESS", "RECON", "ERROR"],
        "VULN_ASSESS": ["EXPLOITATION", "RECON", "SCANNING", "REPORTING", "ERROR"],
        "EXPLOITATION": ["POST_EXPLOIT", "VULN_ASSESS", "REPORTING", "ERROR"],
        "POST_EXPLOIT": ["REPORTING", "EXPLOITATION", "VULN_ASSESS", "ERROR"],
        "REPORTING": ["COMPLETED", "ERROR"],
        "COMPLETED": [],
        "PAUSED": ["RECON", "SCANNING", "VULN_ASSESS", "EXPLOITATION", "POST_EXPLOIT", "REPORTING"],
        "BLOCKED": [],
        "ERROR": ["PLANNING", "PAUSED"]
    }
    
    def __init__(self):
        self.current_state = State.INITIALIZED
        self.state_history = []
        self.state_context = {}
        self.state_metadata = {}
        self.last_active_state = State.INITIALIZED
    
    def get_current_state(self) -> str:
        """Get current state"""
        return self.current_state
    
    def transition_to(self, new_state: str, reason: str = None) -> bool:
        """Transition to new state"""
        if new_state not in [s.value for s in State]:
            logger.error(f"Invalid state: {new_state}")
            return False
        
        allowed_states = self.TRANSITION_RULES.get(self.current_state.value, [])
        
        if new_state not in allowed_states and new_state != self.current_state:
            logger.warning(f"Invalid transition from {self.current_state} to {new_state}")
            return False
        
        old_state = self.current_state
        
        self.state_history.append({
            "from": old_state.value,
            "to": new_state,
            "reason": reason,
            "timestamp": datetime.now().isoformat()
        })
        
        self.current_state = State(new_state)
        
        if new_state not in [State.PAUSED.value, State.BLOCKED.value, State.ERROR.value]:
            self.last_active_state = State(new_state)
        
        logger.info(f"State transition: {old_state} -> {new_state} ({reason})")
        
        return True
    
    def update_context(self, key: str, value: Any) -> None:
        """Update state context"""
        self.state_context[key] = value
    
    def get_context(self, key: str = None) -> Any:
        """Get state context"""
        if key:
            return self.state_context.get(key)
        return self.state_context
    
    def should_continue(self) -> bool:
        """Check if workflow should continue"""
        terminal_states = [State.COMPLETED.value, State.BLOCKED.value]
        
        if self.current_state.value in terminal_states:
            return False
        
        if self.current_state.value == State.ERROR.value:
            return False
        
        return True
    
    def is_state_completed(self, state: str) -> bool:
        """Check if a state has been completed"""
        for entry in self.state_history:
            if entry['from'] == state or entry['to'] == state:
                if entry['to'] != State.PAUSED.value:
                    return True
        return False
    
    def get_state_history(self) -> List[Dict[str, Any]]:
        """Get state transition history"""
        return self.state_history
    
    def get_last_active_state(self) -> str:
        """Get the last active state before pause/error"""
        return self.last_active_state.value
    
    def reset(self) -> None:
        """Reset state tracker"""
        self.current_state = State.INITIALIZED
        self.state_history = []
        self.state_context = {}
        self.state_metadata = {}


class WorkflowEngine:
    """Workflow execution engine"""
    
    def __init__(self, state_tracker: StateTracker, memory_manager):
        self.state_tracker = state_tracker
        self.memory_manager = memory_manager
        self.transition_rules = StateTracker.TRANSITION_RULES
        self.dynamic_adapters = []
        self.workflow_definitions = {}
        self.current_workflow = None
    
    def register_adapter(self, adapter: Callable) -> None:
        """Register a dynamic adapter"""
        self.dynamic_adapters.append(adapter)
    
    def load_workflow_definition(self, workflow_name: str, definition: Dict[str, Any]) -> None:
        """Load a workflow definition"""
        self.workflow_definitions[workflow_name] = definition
    
    def execute_workflow(self, task_definition: Dict[str, Any]) -> Dict[str, Any]:
        """Execute a complete workflow"""
        logger.info(f"Starting workflow execution: {task_definition.get('name', 'unnamed')}")
        
        self.current_workflow = task_definition
        
        execution_result = {
            "workflow_name": task_definition.get('name'),
            "start_time": datetime.now().isoformat(),
            "stages_completed": [],
            "stages_failed": [],
            "final_state": None
        }
        
        while self.state_tracker.should_continue():
            current_state = self.state_tracker.get_current_state()
            logger.info(f"Executing state: {current_state}")
            
            if not self._check_continue_conditions():
                logger.warning("Continue conditions not met")
                self.state_tracker.transition_to("BLOCKED", "Continue conditions not met")
                break
            
            self._execute_state_actions(current_state)
            
            next_state = self._decide_next_state()
            
            if next_state:
                self.state_tracker.transition_to(next_state, "Workflow progression")
            
            self._run_dynamic_adapters()
            
            self._update_memory()
        
        execution_result["end_time"] = datetime.now().isoformat()
        execution_result["final_state"] = self.state_tracker.get_current_state()
        
        return execution_result
    
    def execute_stage(self, stage_name: str) -> Dict[str, Any]:
        """Execute a single stage"""
        if not self.current_workflow:
            return {"status": "error", "message": "No workflow loaded"}
        
        stages = self.current_workflow.get('stages', [])
        stage = next((s for s in stages if s.get('name') == stage_name), None)
        
        if not stage:
            return {"status": "error", "message": f"Stage {stage_name} not found"}
        
        result = {
            "stage_name": stage_name,
            "start_time": datetime.now().isoformat(),
            "tasks": []
        }
        
        for task in stage.get('skills', []):
            task_result = self._execute_task(task)
            result['tasks'].append(task_result)
        
        result["end_time"] = datetime.now().isoformat()
        result["status"] = "completed"
        
        return result
    
    def _execute_state_actions(self, state: str) -> None:
        """Execute actions for current state"""
        if self.current_workflow:
            stages = self.current_workflow.get('stages', [])
            stage_name = self._state_to_stage_name(state)
            
            stage = next((s for s in stages if s.get('name') == stage_name), None)
            
            if stage:
                for task in stage.get('skills', []):
                    self._execute_task(task)
    
    def _execute_task(self, task: str) -> Dict[str, Any]:
        """Execute a single task"""
        return {
            "task": task,
            "status": "executed",
            "timestamp": datetime.now().isoformat()
        }
    
    def _decide_next_state(self) -> Optional[str]:
        """Decide next state based on context"""
        current_state = self.state_tracker.get_current_state()
        
        allowed_states = self.transition_rules.get(current_state, [])
        
        if not allowed_states:
            return None
        
        context = self.state_tracker.get_context()
        
        discoveries = context.get('requirement', {}).get('discoveries', [])
        
        if current_state == "RECON" and len(discoveries) > 0:
            return "SCANNING"
        
        elif current_state == "SCANNING":
            return "VULN_ASSESS"
        
        elif current_state == "VULN_ASSESS":
            exploitable = [d for d in discoveries if d.get('exploitable')]
            if len(exploitable) > 0:
                return "EXPLOITATION"
            else:
                return "REPORTING"
        
        elif current_state == "EXPLOITATION":
            return "POST_EXPLOIT"
        
        elif current_state == "POST_EXPLOIT":
            return "REPORTING"
        
        elif current_state == "REPORTING":
            return "COMPLETED"
        
        elif current_state == "PLANNING":
            return "RECON"
        
        return allowed_states[0] if allowed_states else None
    
    def _state_to_stage_name(self, state: str) -> str:
        """Convert state to stage name"""
        mapping = {
            "RECON": "reconnaissance",
            "SCANNING": "scanning",
            "VULN_ASSESS": "vulnerability_assessment",
            "EXPLOITATION": "exploitation",
            "POST_EXPLOIT": "post_exploitation",
            "REPORTING": "reporting"
        }
        return mapping.get(state, state.lower())
    
    def _check_continue_conditions(self) -> bool:
        """Check if workflow should continue"""
        if not self.state_tracker.should_continue():
            return False
        
        return True
    
    def _run_dynamic_adapters(self) -> None:
        """Run registered dynamic adapters"""
        for adapter in self.dynamic_adapters:
            try:
                adapter(self.state_tracker, self.memory_manager)
            except Exception as e:
                logger.error(f"Dynamic adapter error: {e}")
    
    def _update_memory(self) -> None:
        """Update memory with current state"""
        self.memory_manager.store({
            "current_state": self.state_tracker.get_current_state(),
            "state_context": self.state_tracker.get_context(),
            "timestamp": datetime.now().isoformat()
        }, "short_term")
    
    def get_workflow_status(self) -> Dict[str, Any]:
        """Get current workflow status"""
        return {
            "current_state": self.state_tracker.get_current_state(),
            "workflow_name": self.current_workflow.get('name') if self.current_workflow else None,
            "state_history": self.state_tracker.get_state_history(),
            "context": self.state_tracker.get_context()
        }
