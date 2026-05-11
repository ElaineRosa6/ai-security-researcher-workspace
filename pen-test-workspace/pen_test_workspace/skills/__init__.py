"""
Skills Library - 所有可用的安全测试技能
"""

# 导出主要技能，方便外部Agent调用
from .web import (
    scan_website,
    test_xss,
    test_sql_injection,
    crawl
)
from .network import (
    nmap_scan,
    port_scan,
    service_discovery
)
from .report import (
    generate_markdown_report,
    generate_html_report
)

__all__ = [
    # Web
    'scan_website',
    'test_xss',
    'test_sql_injection',
    'crawl',
    # Network
    'nmap_scan',
    'port_scan',
    'service_discovery',
    # Report
    'generate_markdown_report',
    'generate_html_report'
]
