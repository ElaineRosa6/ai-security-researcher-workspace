# 使用指南

本文档详细介绍如何使用 AI Security Researcher Workspace。

---

## 目录

1. [快速开始](#快速开始)
2. [安装配置](#安装配置)
3. [Agent 模式使用](#agent-模式使用)
4. [Skills 模式使用](#skills-模式使用)
5. [API 参考](#api-参考)
6. [示例代码](#示例代码)
7. [常见问题](#常见问题)

---

## 快速开始

### 环境要求

- Python 3.10+
- pip 包管理器

### 安装

```bash
# 克隆仓库
git clone https://github.com/ElaineRosa6/ai-security-researcher-workspace.git
cd ai-security-researcher-workspace

# 安装依赖
pip install -r requirements.txt
```

### 快速测试

```bash
# 测试 Agent 初始化
python -c "
import sys
sys.path.insert(0, '.')
from agent.core.agent import SecurityExpertAgent
agent = SecurityExpertAgent({})
result = agent.initialize()
print(f'状态: {result[\"status\"]}')
print(f'技能数: {result[\"skills_count\"]}')
"
```

---

## 安装配置

### 1. 基础配置

复制配置模板：

```bash
cp .env.example .env
```

编辑 `.env` 文件：

```env
# LLM 配置 (选择一个)
OPENAI_API_KEY=your-openai-api-key
# ANTHROPIC_API_KEY=your-anthropic-api-key

# LLM 提供者选择
LLM_PROVIDER=openai  # 可选: openai, anthropic, mock
LLM_MODEL=gpt-4o     # 或 claude-3-opus-20240229
```

### 2. 工具安装

运行工具安装脚本：

```bash
chmod +x scripts/install_tools.sh
./scripts/install_tools.sh
```

---

## Agent 模式使用

### 初始化 Agent

```python
import sys
sys.path.insert(0, '.')

from agent.core.agent import SecurityExpertAgent

# 创建 Agent 实例
config = {
    "llm": {
        "provider": "mock",  # 使用 mock 模式测试
        "model": None
    }
}

agent = SecurityExpertAgent(config)

# 初始化
result = agent.initialize()
print(f"初始化状态: {result['status']}")
print(f"已注册技能: {result['skills_count']}")
```

### 执行安全测试任务

```python
# 启动一个 Web 渗透测试任务
result = agent.start_task("对 https://example.com 进行 Web 安全测试")

# 查看结果
print(f"会话ID: {result['session_id']}")
print(f"状态: {result['status']}")
print(f"发现数: {len(result['discoveries'])}")

# 查看报告
print(result['report']['executive_summary'])
```

### 使用 LLM 进行决策

```python
# 配置真实 LLM
config = {
    "llm": {
        "provider": "openai",
        "model": "gpt-4o"
    }
}

agent = SecurityExpertAgent(config)

# 使用 LLM 分析
response = agent.llm.ask("分析这个网站可能存在的安全风险: https://example.com")
print(response)
```

---

## Skills 模式使用

Skills 模式适合被 Claude Code、Codex 或其他 Agent 调用。

### 导入技能

```python
from skills import (
    scan_website,
    test_xss,
    test_sql_injection,
    nmap_scan,
    generate_markdown_report
)
```

### Web 安全测试

```python
# 扫描网站
result = scan_website("https://example.com")
print(result["summary"])

# 测试 XSS
xss_result = test_xss("https://example.com/search", "q")
print(f"XSS 漏洞: {xss_result['vulnerable']}")

# 测试 SQL 注入
sqli_result = test_sql_injection("https://example.com/product", "id")
print(f"SQL 注入: {sqli_result['vulnerable']}")
```

### 网络扫描

```python
# Nmap 扫描
result = nmap_scan("192.168.1.1", ports="1-1000")
for port in result["results"]:
    print(f"端口 {port['port']}: {port['service']}")

# 快速端口扫描
quick_result = port_scan("192.168.1.1")
print(f"开放端口: {quick_result['open_ports']}")
```

### 生成报告

```python
# 收集发现
findings = [
    {
        "title": "XSS 漏洞",
        "severity": "high",
        "description": "搜索参数存在反射型 XSS",
        "url": "https://example.com/search?q=test",
        "cvss": 7.5
    }
]

# 生成 Markdown 报告
report = generate_markdown_report(
    findings=findings,
    target_info={"url": "https://example.com"},
    title="安全测试报告"
)

# 保存报告
with open("report.md", "w", encoding="utf-8") as f:
    f.write(report)
```

---

## API 参考

### Agent API

#### `SecurityExpertAgent(config)`

创建安全专家 Agent 实例。

**参数:**
- `config` (dict): 配置字典
  - `llm.provider`: LLM 提供者 ("openai", "anthropic", "mock")
  - `llm.model`: 模型名称

**返回:**
- SecurityExpertAgent 实例

#### `agent.initialize()`

初始化 Agent，注册所有技能和组件。

**返回:**
```python
{
    "status": "initialized",
    "session_id": "session_20260512_123456",
    "skills_count": 6,
    "harnesses_count": 9
}
```

#### `agent.start_task(requirement)`

启动安全测试任务。

**参数:**
- `requirement` (str): 任务需求描述

**返回:**
```python
{
    "session_id": "...",
    "status": "completed",
    "discoveries": [...],
    "report": {...}
}
```

### Skills API

#### `scan_website(target_url, options=None)`

扫描网站安全漏洞。

**参数:**
- `target_url` (str): 目标 URL
- `options` (dict, optional): 配置选项

**返回:**
```python
{
    "target": "https://example.com",
    "status": "completed",
    "findings": [...],
    "summary": "扫描完成，发现 X 个潜在问题"
}
```

#### `test_xss(url, param, payloads=None)`

测试 XSS 漏洞。

**参数:**
- `url` (str): 目标 URL
- `param` (str): 参数名
- `payloads` (list, optional): XSS payload 列表

**返回:**
```python
{
    "url": "...",
    "param": "...",
    "vulnerable": False,
    "details": "XSS测试完成"
}
```

#### `nmap_scan(target, ports=None, options=None)`

执行 Nmap 扫描。

**参数:**
- `target` (str): 目标 IP 或域名
- `ports` (str, optional): 端口范围
- `options` (dict, optional): 扫描选项

**返回:**
```python
{
    "target": "192.168.1.1",
    "results": [
        {"port": 22, "service": "ssh", "version": "OpenSSH 8.4"},
        {"port": 80, "service": "http", "version": "nginx 1.20"}
    ]
}
```

---

## 示例代码

### 完整的 Web 渗透测试流程

```python
#!/usr/bin/env python3
"""
完整的 Web 渗透测试示例
"""

import sys
sys.path.insert(0, '.')

from skills import (
    scan_website,
    test_xss,
    test_sql_injection,
    crawl,
    generate_markdown_report
)

def web_pentest(target_url):
    """执行完整的 Web 渗透测试"""
    
    print(f"[*] 开始对 {target_url} 进行安全测试")
    
    all_findings = []
    
    # 1. 网站扫描
    print("[*] 阶段 1: 网站扫描...")
    scan_result = scan_website(target_url)
    all_findings.extend(scan_result.get("findings", []))
    print(f"    发现 {len(scan_result.get('findings', []))} 个问题")
    
    # 2. 爬取网站
    print("[*] 阶段 2: 网站爬取...")
    crawl_result = crawl(target_url)
    print(f"    发现 {crawl_result['pages_found']} 个页面")
    
    # 3. 测试 XSS
    print("[*] 阶段 3: XSS 测试...")
    for url in crawl_result["urls"][:5]:  # 测试前5个URL
        xss_result = test_xss(url, "q")
        if xss_result["vulnerable"]:
            all_findings.append({
                "title": "XSS 漏洞",
                "severity": "high",
                "url": url
            })
    
    # 4. 测试 SQL 注入
    print("[*] 阶段 4: SQL 注入测试...")
    for url in crawl_result["urls"][:5]:
        sqli_result = test_sql_injection(url, "id")
        if sqli_result["vulnerable"]:
            all_findings.append({
                "title": "SQL 注入漏洞",
                "severity": "critical",
                "url": url
            })
    
    # 5. 生成报告
    print("[*] 阶段 5: 生成报告...")
    report = generate_markdown_report(
        findings=all_findings,
        target_info={"url": target_url},
        title=f"{target_url} 安全测试报告"
    )
    
    # 保存报告
    report_file = f"report_{target_url.replace('://', '_').replace('/', '')}.md"
    with open(report_file, "w", encoding="utf-8") as f:
        f.write(report)
    
    print(f"[+] 测试完成！发现 {len(all_findings)} 个问题")
    print(f"[+] 报告已保存: {report_file}")
    
    return {
        "target": target_url,
        "findings": all_findings,
        "report_file": report_file
    }

if __name__ == "__main__":
    target = "https://example.com"
    if len(sys.argv) > 1:
        target = sys.argv[1]
    
    result = web_pentest(target)
```

### 使用 Agent 自动化测试

```python
#!/usr/bin/env python3
"""
使用 Agent 自动化安全测试
"""

import sys
sys.path.insert(0, '.')

from agent.core.agent import SecurityExpertAgent

def automated_test(target):
    """使用 Agent 自动化测试"""
    
    # 配置 Agent
    config = {
        "llm": {
            "provider": "mock"  # 使用 mock 模式
        }
    }
    
    # 创建并初始化 Agent
    agent = SecurityExpertAgent(config)
    agent.initialize()
    
    # 启动任务
    result = agent.start_task(f"对 {target} 进行全面安全测试")
    
    # 输出结果
    print("\n" + "="*60)
    print("安全测试报告")
    print("="*60)
    print(f"目标: {target}")
    print(f"会话ID: {result['session_id']}")
    print(f"状态: {result['status']}")
    print(f"\n执行摘要:")
    print(result['report']['executive_summary'])
    print(f"\n发现的问题: {len(result['discoveries'])}")
    
    return result

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "https://example.com"
    automated_test(target)
```

---

## 常见问题

### Q: 如何配置真实的 LLM？

A: 编辑 `.env` 文件或直接在代码中配置：

```python
config = {
    "llm": {
        "provider": "openai",
        "model": "gpt-4o"
    }
}
```

### Q: Mock 模式是什么？

A: Mock 模式用于测试，不调用真实 LLM API，返回模拟响应。

### Q: 如何添加自定义技能？

A: 在 `skills/` 目录创建新模块，然后在 `skills/__init__.py` 中导入。

### Q: 支持哪些 LLM 提供者？

A: 目前支持：
- OpenAI (GPT-4, GPT-4o)
- Anthropic (Claude 3)
- Mock (测试用)

---

## 更多资源

- [API 文档](./docs/api.md)
- [配置指南](./docs/configuration.md)
- [开发指南](./docs/development.md)
- [GitHub 仓库](https://github.com/ElaineRosa6/ai-security-researcher-workspace)
