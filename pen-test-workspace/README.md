# Pen Test Workspace - Skills Library

> 供 Claude Code / Codex / 其他 Agent 调用的安全测试技能库

## 概述

这个分支是**纯Skills库**，没有自主Agent逻辑，没有内置LLM。提供简单、清晰的API，供外部Agent控制使用。

```python
from pen_test_workspace.skills import scan_website, nmap_scan

# 外部LLM可以这样调用我们的技能
result = scan_website("https://example.com")
# 外部LLM自己分析结果，做决策
```

---

## 快速开始

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 导入并使用技能

```python
from pen_test_workspace.skills import (
    scan_website,
    test_xss,
    test_sql_injection,
    nmap_scan,
    generate_markdown_report
)

# 扫描网站
scan_result = scan_website("https://example.com")

# 扫描端口
nmap_result = nmap_scan("192.168.1.1")

# 生成报告
report = generate_markdown_report(
    findings=scan_result["findings"],
    target_info={"url": "https://example.com"}
)
```

更多示例见 [USAGE_EXAMPLE.md](./USAGE_EXAMPLE.md)

---

## 可用的技能

### Web安全
| 技能 | 说明 |
|-----|------|
| `scan_website(url)` | 扫描网站基础安全问题 |
| `test_xss(url, param)` | 测试XSS漏洞 |
| `test_sql_injection(url, param)` | 测试SQL注入漏洞 |
| `crawl(start_url)` | 爬取网站链接 |

### 网络安全
| 技能 | 说明 |
|-----|------|
| `nmap_scan(target, ports)` | Nmap扫描 |
| `port_scan(target, port_list)` | 快速端口扫描 |
| `service_discovery(target)` | 服务发现 |

### 报告
| 技能 | 说明 |
|-----|------|
| `generate_markdown_report(findings)` | 生成Markdown报告 |
| `generate_html_report(findings)` | 生成HTML报告 |

---

## 目录结构

```
pen-test-workspace/
├── pen_test_workspace/       # ✅ 主要技能库 (新增)
│   ├── __init__.py
│   └── skills/
│       ├── __init__.py
│       ├── web.py            # Web安全技能
│       ├── network.py        # 网络安全技能
│       └── report.py         # 报告生成技能
│
├── ai-agent/                 # (保留，可用于参考)
│   ├── skills/               # 原有技能实现
│   └── harness/              # 工具封装
│
├── USAGE_EXAMPLE.md          # ✅ 使用示例
├── BRANCH_README.md          # 分支说明
├── requirements.txt
└── README.md                 # (本文件)
```

---

## 分支说明

| 分支 | 用途 |
|-----|------|
| `skills-library` | (当前) 纯Skills库，供外部Agent调用 |
| `autonomous-agent` | 完整的自主AI Agent，内置LLM |
| `master` | 主分支，作为基础 |

---

## 免责声明

仅用于授权的安全测试、研究和教育目的。用户必须:
- 在测试前获得明确的书面授权
- 遵守所有适用的法律法规
- 最小化潜在的损害
- 及时报告发现的所有漏洞
