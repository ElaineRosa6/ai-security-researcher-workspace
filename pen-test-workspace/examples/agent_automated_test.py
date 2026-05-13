#!/usr/bin/env python3
"""
示例：使用 Agent 自动化安全测试

这个示例展示如何使用 SecurityExpertAgent 进行自动化安全测试。
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from agent.core.agent import SecurityExpertAgent


def automated_security_test(target: str, use_real_llm: bool = False):
    """
    使用 Agent 执行自动化安全测试
    
    Args:
        target: 目标 URL 或 IP
        use_real_llm: 是否使用真实 LLM (需要配置 API Key)
    """
    print("=" * 60)
    print("AI Security Researcher - 自动化安全测试")
    print("=" * 60)
    
    # 配置 Agent
    config = {
        "llm": {
            "provider": "openai" if use_real_llm else "mock",
            "model": "gpt-4o" if use_real_llm else None
        }
    }
    
    # 创建 Agent
    print("\n[*] 初始化 Agent...")
    agent = SecurityExpertAgent(config)
    
    # 初始化
    init_result = agent.initialize()
    print(f"    状态: {init_result['status']}")
    print(f"    会话ID: {init_result['session_id']}")
    print(f"    已注册技能: {init_result['skills_count']}")
    print(f"    已加载 Harness: {init_result['harnesses_count']}")
    
    # 列出已注册的技能
    print("\n[*] 已注册技能:")
    for skill_name in agent.brain.skills_registry.keys():
        print(f"    - {skill_name}")
    
    # 启动安全测试任务
    print(f"\n[*] 开始安全测试: {target}")
    print("-" * 60)
    
    result = agent.start_task(f"对 {target} 进行全面安全测试")
    
    # 显示结果
    print("\n" + "=" * 60)
    print("测试结果")
    print("=" * 60)
    
    print(f"\n会话ID: {result['session_id']}")
    print(f"状态: {result['status']}")
    
    # 执行摘要
    if 'report' in result:
        print(f"\n执行摘要:")
        print(result['report']['executive_summary'])
    
    # 发现的问题
    discoveries = result.get('discoveries', [])
    print(f"\n发现的问题: {len(discoveries)}")
    
    if discoveries:
        print("\n问题列表:")
        for i, finding in enumerate(discoveries[:10], 1):  # 显示前10个
            print(f"  {i}. {finding.get('title', '未知问题')}")
            print(f"     严重程度: {finding.get('severity', 'unknown')}")
    
    # 建议
    if 'report' in result and result['report'].get('recommendations'):
        print("\n建议:")
        for rec in result['report']['recommendations']:
            print(f"  - {rec}")
    
    return result


if __name__ == "__main__":
    target = "https://example.com"
    use_real_llm = False
    
    # 解析命令行参数
    args = sys.argv[1:]
    for arg in args:
        if arg.startswith("--target="):
            target = arg.split("=", 1)[1]
        elif arg == "--real-llm":
            use_real_llm = True
    
    print(f"目标: {target}")
    print(f"使用真实 LLM: {use_real_llm}")
    
    result = automated_security_test(target, use_real_llm)
