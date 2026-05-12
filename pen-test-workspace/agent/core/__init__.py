"""Agent Core Package"""
from .brain import Brain
from .llm_client import LLMClient

# Import from relative modules
import sys
import os

# Add parent directory to path for imports
_parent = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _parent not in sys.path:
    sys.path.insert(0, _parent)

from agent.memory.memory_manager import MemoryManager
from agent.knowledge.graph import KnowledgeGraph
from agent.workflow.engine import WorkflowEngine, StateTracker
from agent.quality.quality_control import Validator, SelfAssessment, Auditor
from agent.awareness.awareness import AgentAwareness
from agent.meta.meta_system import MetaSystem

__all__ = [
    'Brain',
    'LLMClient',
    'MemoryManager',
    'KnowledgeGraph',
    'WorkflowEngine',
    'StateTracker',
    'Validator',
    'SelfAssessment',
    'Auditor',
    'AgentAwareness',
    'MetaSystem',
]
