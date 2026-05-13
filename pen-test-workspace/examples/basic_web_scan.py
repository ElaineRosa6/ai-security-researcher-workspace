#!/usr/bin/env python3
"""
示例：基础 Web 安全扫描

这个示例展示如何使用 Skills 进行基础的 Web 安全扫描。
"""

import sys
import os

# 添加项目根目录到路径
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from skills import (
    scan_website,
    test_xss,
    test_sql_injection,
    generate_markdown_report
)


def basic_web_scan(target_url: str):
    """
    执行基础 Web 安全扫描
    
    Args:
        target_url: 目标网站 URL
    """
    print(f"[*] 开始扫描: {target_url}")
    print("-" * 50)
    
    # 1. 网站扫描
    print("[1] 执行网站扫描...")
    scan_result = scan_website(target_url)
    print(f"    状态: {scan_result['status']}")
    print(f"    发现: {len(scan_result.get('findings', []))} 个问题")
    
    # 2. XSS 测试
    print("\n[2] 测试 XSS 漏洞...")
    xss_result = test_xss(f"{target_url}/search", "q")
    print(f"    测试参数: q")
    print(f"    结果: {'存在漏洞' if xss_result['vulnerable'] else '未发现漏洞'}")
    
    # 3. SQL 注入测试
    print("\n[3] 测试 SQL 注入...")
    sqli_result = test_sql_injection(f"{target_url}/product", "id")
    print(f"    测试参数: id")
    print(f"    结果: {'存在漏洞' if sqli_result['vulnerable'] else '未发现漏洞'}")
    
    # 4. 生成报告
    print("\n[4] 生成报告...")
    all_findings = scan_result.get('findings', [])
    
    report = generate_markdown_report(
        findings=all_findings,
        target_info={"url": target_url},
        title=f"{target_url} 安全扫描报告"
    )
    
    # 保存报告
    report_file = f"scan_report_{target_url.replace('://', '_').replace('/', '')}.md"
    with open(report_file, "w", encoding="utf-8") as f:
        f.write(report)
    
    print(f"    报告已保存: {report_file}")
    
    # 打印摘要
    print("\n" + "=" * 50)
    print("扫描完成!")
    print("=" * 50)
    print(f"目标: {target_url}")
    print(f"发现: {len(all_findings)} 个问题")
    print(f"报告: {report_file}")


if __name__ == "__main__":
    # 默认目标
    target = "https://example.com"
    
    # 从命令行参数获取目标
    if len(sys.argv) > 1:
        target = sys.argv[1]
    
    basic_web_scan(target)
