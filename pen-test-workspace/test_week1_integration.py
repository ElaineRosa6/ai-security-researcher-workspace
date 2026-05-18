#!/usr/bin/env python3
"""
Week 1 Integration Test - Test the tool executor and skills integration
"""
import sys
import os
import logging

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Add project directories to path
script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(script_dir)
if project_root not in sys.path:
    sys.path.insert(0, project_root)
agent_dir = os.path.join(project_root, 'agent')
ai_agent_dir = os.path.join(project_root, 'ai-agent')
if agent_dir not in sys.path:
    sys.path.insert(0, agent_dir)
if ai_agent_dir not in sys.path:
    sys.path.insert(0, ai_agent_dir)


def test_tool_executor():
    """Test the ToolExecutor"""
    logger.info("=== Testing ToolExecutor ===")
    
    try:
        from ai_agent.harness.tool_executor import ToolExecutorFactory
        
        logger.info("✓ ToolExecutorFactory imported successfully")
        
        # Test Nmap executor creation
        nmap_executor = ToolExecutorFactory.create("nmap")
        logger.info("✓ NmapExecutor created successfully")
        
        # Test SQLMap executor creation
        sqlmap_executor = ToolExecutorFactory.create("sqlmap")
        logger.info("✓ SQLMapExecutor created successfully")
        
        # Test Nuclei executor creation
        nuclei_executor = ToolExecutorFactory.create("nuclei")
        logger.info("✓ NucleiExecutor created successfully")
        
        return True
        
    except Exception as e:
        logger.error(f"✗ ToolExecutor test failed: {e}")
        import traceback
        logger.error(traceback.format_exc())
        return False


def test_skills_manager():
    """Test the SkillsManager"""
    logger.info("\n=== Testing SkillsManager ===")
    
    try:
        from agent.core import Brain, MemoryManager, KnowledgeGraph, WorkflowEngine, StateTracker
        from agent.skills import SkillsManager
        
        logger.info("✓ Imports successful")
        
        # Initialize components
        memory = MemoryManager()
        knowledge = KnowledgeGraph()
        state_tracker = StateTracker()
        brain = Brain(memory, knowledge, state_tracker)
        
        logger.info("✓ Brain initialized successfully")
        
        # Initialize SkillsManager
        skills_manager = SkillsManager()
        logger.info("✓ SkillsManager initialized successfully")
        
        # Register skills
        skills_manager.register_all(brain)
        logger.info(f"✓ Skills registered: {len(brain.skills_registry)} skills")
        
        for skill_name in brain.skills_registry:
            logger.info(f"  - {skill_name}")
        
        return True
        
    except Exception as e:
        logger.error(f"✗ SkillsManager test failed: {e}")
        import traceback
        logger.error(traceback.format_exc())
        return False


def test_general_skill():
    """Test GeneralSkill with tool executor"""
    logger.info("\n=== Testing GeneralSkill ===")
    
    try:
        sys.path.insert(0, ai_agent_dir)
        from skills.general.general import GeneralSkill
        
        logger.info("✓ GeneralSkill imported successfully")
        
        # Initialize skill
        skill = GeneralSkill()
        logger.info("✓ GeneralSkill initialized successfully")
        
        logger.info("✓ Tool executors initialized: %s", list(skill.executors.keys()))
        
        # Test fallback methods (without actually running nmap which might not be available)
        logger.info("Testing fallback methods...")
        
        # Test with a mock target
        result = skill._fallback_nmap_scan("scanme.nmap.org", flags="-p 80,443 --script-timeout=5")
        logger.info(f"✓ Fallback Nmap scan completed, status: {result.get('status')}")
        
        # Test nuclei scan (info only)
        result = skill.nuclei_scan("http://scanme.nmap.org")
        logger.info(f"✓ Nuclei scan (info) completed, status: {result.get('status')}")
        
        # Test sqlmap scan (info only)
        result = skill.sqlmap_scan("http://testphp.vulnweb.com/listproducts.php?cat=1")
        logger.info(f"✓ SQLMap scan (info) completed, status: {result.get('status')}")
        
        return True
        
    except Exception as e:
        logger.error(f"✗ GeneralSkill test failed: {e}")
        import traceback
        logger.error(traceback.format_exc())
        return False


def test_brain_execution():
    """Test executing a skill through the Brain"""
    logger.info("\n=== Testing Brain Skill Execution ===")
    
    try:
        from agent.core import Brain, MemoryManager, KnowledgeGraph, WorkflowEngine, StateTracker
        from agent.skills import SkillsManager
        
        # Initialize
        memory = MemoryManager()
        knowledge = KnowledgeGraph()
        state_tracker = StateTracker()
        brain = Brain(memory, knowledge, state_tracker)
        skills_manager = SkillsManager()
        skills_manager.register_all(brain)
        
        logger.info("✓ Brain and skills initialized")
        
        # Test execute_skill
        logger.info("Testing GeneralSkill methods through Brain...")
        
        # Try to execute nmap_scan
        result = brain.execute_skill("GeneralSkill.nmap_scan", {
            "params": {"target": "scanme.nmap.org", "flags": "-p 80"}
        })
        
        logger.info(f"✓ Skill execution result status: {result.get('status', 'unknown')}")
        
        return True
        
    except Exception as e:
        logger.error(f"✗ Brain execution test failed: {e}")
        import traceback
        logger.error(traceback.format_exc())
        return False


def test_agent_integration():
    """Test the full Agent integration"""
    logger.info("\n=== Testing Full Agent Integration ===")
    
    try:
        from agent.core.agent import SecurityExpertAgent
        
        logger.info("✓ SecurityExpertAgent imported")
        
        # Initialize agent with mock LLM
        config = {
            "llm": {
                "provider": "mock"
            }
        }
        
        agent = SecurityExpertAgent(config)
        logger.info("✓ Agent initialized successfully")
        
        init_result = agent.initialize()
        logger.info(f"✓ Agent initialized: {init_result.get('status')}")
        logger.info(f"✓ Skills count: {init_result.get('skills_count')}")
        logger.info(f"✓ Harness count: {init_result.get('harnesses_count')}")
        
        # Test simple task processing
        logger.info("Testing simple task...")
        result = agent.start_task("Scan 127.0.0.1 for open ports")
        
        logger.info(f"✓ Task completed: {result.get('status')}")
        
        return True
        
    except Exception as e:
        logger.error(f"✗ Agent integration test failed: {e}")
        import traceback
        logger.error(traceback.format_exc())
        return False


def main():
    """Run all tests"""
    logger.info("=" * 60)
    logger.info("Week 1 Integration Test Suite")
    logger.info("=" * 60)
    
    results = {
        "ToolExecutor": test_tool_executor(),
        "SkillsManager": test_skills_manager(),
        "GeneralSkill": test_general_skill(),
        "BrainExecution": test_brain_execution(),
        "AgentIntegration": test_agent_integration()
    }
    
    logger.info("\n" + "=" * 60)
    logger.info("Test Results Summary")
    logger.info("=" * 60)
    
    all_passed = True
    for name, passed in results.items():
        status = "✓ PASSED" if passed else "✗ FAILED"
        logger.info(f"{name}: {status}")
        if not passed:
            all_passed = False
    
    logger.info("=" * 60)
    
    if all_passed:
        logger.info("\n✓ All tests passed! Week 1 integration complete!")
        return 0
    else:
        logger.error("\n✗ Some tests failed! Please check above.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
