#!/usr/bin/env python3
"""
Simple CLI for the Security Expert Agent
"""
import sys
import os
import argparse
import logging

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from agent.core.agent import SecurityExpertAgent
from agent.core.llm_client import LLMClient
from agent.prompts import PromptLoader


def test_llm_client():
    """Test the LLM client (uses mock)"""
    print("=== Testing LLMClient...")
    llm = LLMClient(provider='mock')
    resp = llm.ask("Hello, are you working?")
    print(f"Response: {resp}")
    return llm


def test_prompt_loader():
    """Test prompt loader"""
    print("\n=== Testing PromptLoader...")
    try:
        from agent.prompts import PromptLoader
        loader = PromptLoader()
        sys_prompt = loader.get("system_prompt")
        print(f"System prompt loaded, length: {len(sys_prompt) if sys_prompt else 0}")
        return loader
    except Exception as e:
        print(f"Warning: {e}")
        return None


def test_agent_init():
    """Initialize and test the agent"""
    print("\n=== Testing Agent Initialization...")
    config = {
        "llm": {"provider": "mock"}
    }
    agent = SecurityExpertAgent(config)
    init_result = agent.initialize()
    print(f"Agent initialized: {init_result}")
    return agent


def main():
    parser = argparse.ArgumentParser(
        description="Security Expert Agent CLI")
    
    subparsers = parser.add_subparsers(title="Commands", dest="cmd")
    
    # Test command
    test_parser = subparsers.add_parser("test", help="Run tests")
    
    # Start task
    start_parser = subparsers.add_parser("start", help="Start a task")
    start_parser.add_argument("requirement", nargs="*", help="Task requirement")
    
    args = parser.parse_args()
    
    logging.basicConfig(level=logging.INFO)
    
    if args.cmd == "test":
        print("Running quick test...")
        test_llm_client()
        test_prompt_loader()
        test_agent_init()
        print("\n✅ All basic components available!")
    elif args.cmd == "start":
        req = ' '.join(args.requirement)
        if not req:
            req = input("Enter security testing requirement: ")
        
        agent = test_agent_init()
        result = agent.start_task(req)
        print(f"\nTask result: {result.get('status')}")
        print(f"Discoveries: {len(result.get('discoveries', []))}")
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
