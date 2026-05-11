"""
Report Generation Skills - 报告生成技能
供外部Agent调用
"""

from typing import Dict, List, Any, Optional
from datetime import datetime


def generate_markdown_report(
    findings: List[Dict[str, Any]],
    target_info: Optional[Dict[str, Any]] = None,
    title: str = "安全测试报告"
) -> str:
    """
    生成Markdown格式的安全测试报告

    Args:
        findings: 漏洞发现列表
        target_info: 目标信息
        title: 报告标题

    Returns:
        Markdown报告内容
    """
    target_info = target_info or {}

    report = f"# {title}\n\n"
    report += f"**生成时间**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"

    if target_info:
        report += "## 目标信息\n\n"
        for key, value in target_info.items():
            report += f"- **{key}**: {value}\n"
        report += "\n"

    if findings:
        report += f"## 漏洞发现 ({len(findings)}个)\n\n"

        # 按严重程度排序
        severity_order = {"critical": 0, "high": 1, "medium": 2, "low": 3, "info": 4}
        sorted_findings = sorted(
            findings,
            key=lambda x: severity_order.get(x.get("severity", "info"), 5)
        )

        for idx, finding in enumerate(sorted_findings, 1):
            report += f"### {idx}. {finding.get('title', '未命名漏洞')}\n\n"
            report += f"- **严重程度**: {finding.get('severity', 'info')}\n"
            report += f"- **CVSS**: {finding.get('cvss', 0.0)}\n"

            if finding.get('url'):
                report += f"- **影响URL**: {finding.get('url')}\n"

            report += f"\n**描述**:\n{finding.get('description', '无描述')}\n\n"

            if finding.get('evidence'):
                report += f"**证据**:\n```\n{finding.get('evidence')}\n```\n\n"

            if finding.get('remediation'):
                report += f"**修复建议**:\n{finding.get('remediation')}\n\n"

            report += "---\n\n"
    else:
        report += "## 漏洞发现\n\n未发现安全问题。\n\n"

    report += "## 总结\n\n"
    critical = len([f for f in findings if f.get('severity') == 'critical'])
    high = len([f for f in findings if f.get('severity') == 'high'])
    medium = len([f for f in findings if f.get('severity') == 'medium'])
    low = len([f for f in findings if f.get('severity') == 'low'])

    report += f"- Critical: {critical}\n"
    report += f"- High: {high}\n"
    report += f"- Medium: {medium}\n"
    report += f"- Low: {low}\n"

    return report


def generate_html_report(
    findings: List[Dict[str, Any]],
    target_info: Optional[Dict[str, Any]] = None,
    title: str = "安全测试报告"
) -> str:
    """
    生成HTML格式的安全测试报告

    Args:
        findings: 漏洞发现列表
        target_info: 目标信息
        title: 报告标题

    Returns:
        HTML报告内容
    """
    md_report = generate_markdown_report(findings, target_info, title)

    # 简单的HTML包装
    html = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>{title}</title>
    <style>
        body {{ font-family: Arial, sans-serif; max-width: 900px; margin: 40px auto; padding: 0 20px; }}
        h1 {{ color: #333; border-bottom: 2px solid #4CAF50; padding-bottom: 10px; }}
        h2 {{ color: #555; margin-top: 30px; }}
        h3 {{ color: #666; }}
        .critical {{ color: #ff0000; font-weight: bold; }}
        .high {{ color: #ff6600; font-weight: bold; }}
        .medium {{ color: #ffcc00; font-weight: bold; }}
        .low {{ color: #009933; font-weight: bold; }}
        .info {{ color: #0066cc; font-weight: bold; }}
    </style>
</head>
<body>
    <pre style="white-space: pre-wrap; word-wrap: break-word;">{md_report}</pre>
</body>
</html>
"""
    return html
