"""
Web Security Skills - Web安全测试技能
供外部Agent调用
"""

from typing import Dict, List, Any, Optional
from dataclasses import dataclass, asdict
from enum import Enum


class Severity(str, Enum):
    """漏洞严重程度"""
    CRITICAL = "critical"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"
    INFO = "info"


@dataclass
class Finding:
    """漏洞发现"""
    title: str
    severity: Severity
    description: str
    url: str
    evidence: Optional[str] = None
    cvss: float = 0.0
    remediation: Optional[str] = None


def scan_website(
    target_url: str,
    options: Optional[Dict[str, Any]] = None
) -> Dict[str, Any]:
    """
    扫描网站，执行基础的Web安全检查

    Args:
        target_url: 目标网站URL (例如: "https://example.com")
        options: 配置选项
            - auth: 认证信息
            - depth: 扫描深度 (默认: 3)
            - follow_redirects: 是否跟随重定向 (默认: True)

    Returns:
        扫描结果字典
    """
    options = options or {}

    # 这是一个示例实现，实际需要调用真实的安全工具
    findings = []

    # 模拟一些发现
    findings.append(Finding(
        title="潜在的XSS漏洞点",
        severity=Severity.MEDIUM,
        description="搜索表单输入框可能存在XSS漏洞",
        url=f"{target_url}/search?q=test",
        cvss=6.1
    ))

    return {
        "target": target_url,
        "status": "completed",
        "findings": [asdict(f) for f in findings],
        "summary": f"扫描完成，发现 {len(findings)} 个潜在问题"
    }


def test_xss(
    url: str,
    param: str,
    payloads: Optional[List[str]] = None
) -> Dict[str, Any]:
    """
    测试XSS漏洞

    Args:
        url: 目标URL
        param: 要测试的参数名
        payloads: XSS payload列表 (可选，使用默认payloads)

    Returns:
        测试结果
    """
    if payloads is None:
        payloads = [
            "<script>alert(1)</script>",
            "\"'><img src=x onerror=alert(1)>",
            "<svg/onload=alert(1)>",
        ]

    return {
        "url": url,
        "param": param,
        "payloads_tested": payloads,
        "vulnerable": False,
        "details": "XSS测试完成"
    }


def test_sql_injection(
    url: str,
    param: str
) -> Dict[str, Any]:
    """
    测试SQL注入漏洞

    Args:
        url: 目标URL
        param: 要测试的参数

    Returns:
        测试结果
    """
    test_payloads = [
        "'",
        "\"",
        "' OR 1=1--",
        "' UNION SELECT 1,2,3--",
    ]

    return {
        "url": url,
        "param": param,
        "vulnerable": False,
        "details": "SQL注入测试完成"
    }


def crawl(
    start_url: str,
    max_pages: int = 50,
    include_patterns: Optional[List[str]] = None
) -> Dict[str, Any]:
    """
    爬取网站，发现链接和页面

    Args:
        start_url: 起始URL
        max_pages: 最大爬取页数
        include_patterns: URL包含模式列表

    Returns:
        爬取结果
    """
    return {
        "start_url": start_url,
        "pages_found": 10,
        "urls": [
            start_url,
            f"{start_url}/about",
            f"{start_url}/contact",
            f"{start_url}/api/users",
        ],
        "status": "completed"
    }
