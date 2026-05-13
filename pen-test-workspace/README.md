# AI Security Researcher Workspace

> AI 驱动的安全测试工作空间，支持自主 Agent 模式和 Skills 库模式

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

---

## 项目简介

AI Security Researcher Workspace 是一个全面的安全测试平台，提供两种使用模式：

| 模式 | 说明 | 适用场景 |
|------|------|----------|
| **autonomous-agent** | 自主 AI Agent，内置 LLM 推理 | 独立运行安全测试 |
| **skills-library** | 纯 Skills 库，供外部 Agent 调用 | Claude Code / Codex 集成 |

---

## 功能特性

- 🤖 **LLM 集成** - 支持 OpenAI、Claude 和 Mock 测试模式
- 🔧 **6+ 安全技能** - Web 安全、网络扫描、事件响应等
- 📊 **9+ 测试框架** - 完整的 Harness 测试框架
- 📝 **报告生成** - Markdown / HTML 格式报告
- 🔌 **易于集成** - 简单的 API，便于外部调用

---

## 快速开始

### 安装

```bash
git clone https://github.com/ElaineRosa6/ai-security-researcher-workspace.git
cd ai-security-researcher-workspace
pip install -r requirements.txt
```

### 验证安装

```bash
python -c "
import sys
sys.path.insert(0, '.')
from agent.core.agent import SecurityExpertAgent
agent = SecurityExpertAgent({})
result = agent.initialize()
print('✅ 安装成功!' if result['status'] == 'initialized' else '❌ 安装失败')
"
```

### 运行测试

```bash
# 使用 CLI
python agent/cli.py test

# 运行示例
python examples/basic_web_scan.py https://example.com
```

---

## 使用方式

### 方式一：Skills 模式（推荐新手）

```python
from skills import scan_website, generate_markdown_report

# 扫描网站
result = scan_website("https://example.com")
print(result["summary"])

# 生成报告
report = generate_markdown_report(
    findings=result["findings"],
    target_info={"url": "https://example.com"}
)
print(report)
```

### 方式二：Agent 模式

```python
from agent.core.agent import SecurityExpertAgent

# 创建并初始化 Agent
agent = SecurityExpertAgent({"llm": {"provider": "mock"}})
agent.initialize()

# 执行安全测试
result = agent.start_task("测试 https://example.com 的 Web 安全")
print(f"发现: {len(result['discoveries'])} 个问题")
```

---

## 项目结构

```
ai-security-researcher-workspace/
├── agent/                 # Agent 核心模块
│   ├── core/             # 核心组件 (Agent, Brain, LLM)
│   ├── skills/           # 技能管理
│   ├── harness/          # 测试框架
│   ├── prompts/          # 提示词系统
│   └── workflow/         # 工作流引擎
├── skills/               # Skills 库 (独立使用)
│   ├── web.py           # Web 安全技能
│   ├── network.py       # 网络安全技能
│   └── report.py        # 报告生成
├── ai-agent/            # 原始 Skills 实现
│   ├── skills/          # 完整技能模块
│   ├── harness/         # 测试 Harness
│   └── workflows/       # YAML 工作流
├── examples/            # 示例代码
├── docs/                # 文档
├── tests/               # 测试
└── scripts/             # 工具脚本
```

---

## 可用技能

### Web 安全
| 技能 | 说明 |
|------|------|
| `scan_website(url)` | 网站安全扫描 |
| `test_xss(url, param)` | XSS 漏洞测试 |
| `test_sql_injection(url, param)` | SQL 注入测试 |
| `crawl(start_url)` | 网站爬取 |

### 网络安全
| 技能 | 说明 |
|------|------|
| `nmap_scan(target, ports)` | Nmap 扫描 |
| `port_scan(target)` | 快速端口扫描 |
| `service_discovery(target)` | 服务发现 |

### 报告生成
| 技能 | 说明 |
|------|------|
| `generate_markdown_report(findings)` | 生成 Markdown 报告 |
| `generate_html_report(findings)` | 生成 HTML 报告 |

---

## 配置

### LLM 配置

创建 `.env` 文件：

```env
# OpenAI
OPENAI_API_KEY=your-api-key
LLM_PROVIDER=openai
LLM_MODEL=gpt-4o

# 或 Anthropic
# ANTHROPIC_API_KEY=your-api-key
# LLM_PROVIDER=anthropic
# LLM_MODEL=claude-3-opus-20240229
```

### 使用 Mock 模式（测试用）

```python
config = {"llm": {"provider": "mock"}}
agent = SecurityExpertAgent(config)
```

---

## 文档

- [快速入门指南](docs/QUICKSTART.md)
- [完整使用指南](docs/USAGE_GUIDE.md)
- [API 参考](docs/api.md)
- [配置指南](docs/configuration.md)

---

## 示例

查看 `examples/` 目录：

- `basic_web_scan.py` - 基础 Web 安全扫描
- `agent_automated_test.py` - Agent 自动化测试

---

## 分支说明

| 分支 | 说明 |
|------|------|
| `master` | 主分支，稳定版本 |
| `autonomous-agent` | 自主 Agent 实现 |
| `skills-library` | 纯 Skills 库版本 |

---

## 开发

### 运行测试

```bash
python -m pytest tests/ -v
```

### 代码风格

```bash
# 格式化代码
black .

# 类型检查
mypy agent/
```

---

## 贡献

欢迎贡献！请查看 [贡献指南](CONTRIBUTING.md)。

---

## 许可证

MIT License - 详见 [LICENSE](LICENSE) 文件

---

## 免责声明

⚠️ **重要提示**

本项目仅供授权的安全测试、研究和教育目的。使用者必须：

- 在测试前获得明确的书面授权
- 遵守所有适用的法律法规
- 最小化潜在的损害
- 及时报告发现的所有漏洞

**未经授权的安全测试是违法的。**

---

## 联系方式

- GitHub: [https://github.com/ElaineRosa6/ai-security-researcher-workspace](https://github.com/ElaineRosa6/ai-security-researcher-workspace)
- Issues: [提交问题](https://github.com/ElaineRosa6/ai-security-researcher-workspace/issues)
