#!/usr/bin/env python3
"""
Agent Startup Script
Initialize and start the Security Expert Agent
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from agent.core.agent import SecurityExpertAgent
from agent.memory.memory_manager import MemoryManager
from agent.knowledge.graph import KnowledgeGraph
from agent.workflow.engine import WorkflowEngine, StateTracker
from agent.quality.quality_control import Validator, SelfAssessment, Auditor
from agent.awareness.awareness import AgentAwareness, ContextAwareness, DecisionGuide
from agent.meta.meta_system import MetaSystem

import yaml
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)


def load_config(config_path: str = "config/agent/core.yaml") -> dict:
    """Load agent configuration"""
    try:
        with open(config_path, 'r') as f:
            return yaml.safe_load(f)
    except Exception as e:
        logger.warning(f"Failed to load config: {e}, using defaults")
        return {}


def start_agent(requirement: str, config_path: str = None) -> dict:
    """Start the security expert agent"""
    
    logger.info("Initializing Security Expert Agent...")
    
    config = load_config(config_path) if config_path else {}
    
    agent = SecurityExpertAgent(config)
    
    init_result = agent.initialize()
    logger.info(f"Agent initialized: {init_result}")
    
    result = agent.start_task(requirement)
    
    return result


def main():
    """Main entry point"""
    if len(sys.argv) > 1:
        requirement = ' '.join(sys.argv[1:])
    else:
        requirement = input("Enter security testing requirement: ")
    
    result = start_agent(requirement)
    
    print("\n" + "="*50)
    print("TASK COMPLETED")
    print("="*50)
    print(f"Session ID: {result.get('session_id')}")
    print(f"Status: {result.get('status')}")
    print(f"Findings: {len(result.get('discoveries', []))}")
    
    if 'report' in result:
        print(f"\nReport saved to: output/reports/")


if __name__ == "__main__":
    main()
