#!/usr/bin/env python3
"""
Week 2 Integration Test - Workflow Runner and Execution
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
if agent_dir not in sys.path:
    sys.path.insert(0, agent_dir)


def test_workflow_loader():
    """测试工作流加载器"""
    logger.info("=== Testing Workflow Loader ===")
    
    try:
        from agent.workflow.yaml_loader import WorkflowLoader
        
        loader = WorkflowLoader()
        workflows = loader.list_workflows()
        
        logger.info(f"Found {len(workflows)} workflows")
        
        if workflows:
            logger.info(f"Workflows available: {', '.join(workflows)}")
            return {"status": "passed", "workflows": workflows}
        else:
            logger.warning("No workflows found")
            return {"status": "passed", "workflows": []}
            
    except Exception as e:
        logger.error(f"Workflow loader test failed: {e}")
        import traceback
        logger.error(traceback.format_exc())
        return {"status": "failed", "error": str(e)}


def test_workflow_runner():
    """测试工作流执行器"""
    logger.info("\n=== Testing Workflow Runner ===")
    
    try:
        from agent.core import Brain, MemoryManager, KnowledgeGraph, StateTracker
        from agent.skills import SkillsManager
        from agent.workflow.runner import WorkflowRunner
        
        # Initialize components
        memory = MemoryManager()
        knowledge = KnowledgeGraph()
        state_tracker = StateTracker()
        brain = Brain(memory, knowledge, state_tracker)
        
        # Register skills
        skills_manager = SkillsManager()
        skills_manager.register_all(brain)
        
        logger.info(f"Registered {len(brain.skills_registry)} skills")
        
        # Create workflow runner
        runner = WorkflowRunner(brain, state_tracker)
        
        # List available workflows
        available = runner.list_available_workflows()
        logger.info(f"Available workflows: {available}")
        
        return {
            "status": "passed",
            "available_workflows": available,
            "skills_count": len(brain.skills_registry)
        }
        
    except Exception as e:
        logger.error(f"Workflow runner test failed: {e}")
        import traceback
        logger.error(traceback.format_exc())
        return {"status": "failed", "error": str(e)}


def test_result_parser():
    """测试结果解析器"""
    logger.info("\n=== Testing Result Parser ===")
    
    try:
        from agent.workflow.runner import ResultParser
        
        # 模拟工作流结果
        mock_result = {
            "workflow": "test_workflow",
            "start_time": "2024-01-01T00:00:00",
            "end_time": "2024-01-01T00:05:00",
            "duration": 300.0,
            "status": "completed",
            "phases": [
                {
                    "phase": "test_phase",
                    "start_time": "2024-01-01T00:00:00",
                    "end_time": "2024-01-01T00:05:00",
                    "status": "completed",
                    "tasks": [
                        {
                            "task_id": "test_task",
                            "name": "Test Task",
                            "skill": "GeneralSkill.test",
                            "status": "completed",
                            "start_time": "2024-01-01T00:00:00",
                            "end_time": "2024-01-01T00:05:00",
                            "result": {
                                "discoveries": ["Test discovery 1", "Test discovery 2"]
                            }
                        }
                    ]
                }
            ],
            "report": {
                "summary": {
                    "total_tasks": 1,
                    "completed": 1,
                    "failed": 0,
                    "skipped": 0,
                    "success_rate": 1.0
                },
                "discoveries": ["Test discovery 1", "Test discovery 2"]
            }
        }
        
        # 测试解析
        parsed = ResultParser.parse(mock_result)
        logger.info(f"Parsed result: {parsed.keys()}")
        
        # 测试 Markdown 生成
        markdown = ResultParser.to_markdown(mock_result)
        logger.info(f"Generated markdown report ({len(markdown)} chars)")
        
        # 测试发现提取
        discoveries = ResultParser.get_discoveries(mock_result)
        logger.info(f"Extracted {len(discoveries)} discoveries")
        
        return {"status": "passed"}
        
    except Exception as e:
        logger.error(f"Result parser test failed: {e}")
        import traceback
        logger.error(traceback.format_exc())
        return {"status": "failed", "error": str(e)}


def test_agent_workflow_integration():
    """测试完整的 Agent + Workflow 集成"""
    logger.info("\n=== Testing Agent Workflow Integration ===")
    
    try:
        from agent.core.agent import SecurityExpertAgent
        from agent.workflow.runner import WorkflowRunner, ResultParser
        
        # Initialize agent with mock LLM
        agent = SecurityExpertAgent({
            "llm": {"provider": "mock"}
        })
        
        init_result = agent.initialize()
        logger.info(f"Agent initialized: {init_result.get('status')}")
        
        # Try to get brain
        brain = agent.brain
        
        if brain:
            state_tracker = agent.state_tracker
            runner = WorkflowRunner(brain, state_tracker)
            
            # List workflows
            workflows = runner.list_available_workflows()
            logger.info(f"Available workflows: {workflows}")
            
            # 运行简单的任务（而不是完整工作流，因为需要真实工具）
            logger.info("Testing brain task planning")
            
            # 测试 Brain 的执行
            test_result = brain.execute_skill("GeneralSkill.nmap_scan", {
                "params": {
                    "target": "127.0.0.1",
                    "flags": "-p 80"
                }
            })
            
            logger.info(f"Skill execution test result: {test_result.get('status', 'unknown')}")
        
        return {"status": "passed"}
        
    except Exception as e:
        logger.error(f"Agent workflow integration failed: {e}")
        import traceback
        logger.error(traceback.format_exc())
        return {"status": "failed", "error": str(e)}


def main():
    """运行所有测试"""
    logger.info("=" * 60)
    logger.info("Week 2 Integration Test Suite")
    logger.info("=" * 60)
    
    results = {
        "workflow_loader": test_workflow_loader(),
        "workflow_runner": test_workflow_runner(),
        "result_parser": test_result_parser(),
        "agent_integration": test_agent_workflow_integration()
    }
    
    logger.info("\n" + "=" * 60)
    logger.info("Test Results Summary")
    logger.info("=" * 60)
    
    all_passed = True
    for name, result in results.items():
        status = result.get("status", "unknown")
        status_icon = "✅" if status == "passed" else "❌"
        logger.info(f"{name}: {status_icon} {status}")
        
        if status != "passed":
            all_passed = False
            if "error" in result:
                logger.error(f"  Error: {result['error']}")
    
    logger.info("=" * 60)
    
    if all_passed:
        logger.info("\n✅ Week 2 integration tests passed!")
        return 0
    else:
        logger.error("\n❌ Some tests failed.")
        return 1


if __name__ == "__main__":
    sys.exit(main())

