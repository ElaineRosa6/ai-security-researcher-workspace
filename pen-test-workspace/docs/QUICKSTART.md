# 快速入门指南

本指南帮助您在 5 分钟内开始使用 AI Security Researcher Workspace。

---

## 1. 安装 (2分钟)

```bash
# 克隆仓库
git clone https://github.com/ElaineRosa6/ai-security-researcher-workspace.git
cd ai-security-researcher-workspace

# 安装依赖
pip install -r requirements.txt
```

---

## 2. 验证安装 (1分钟)

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

---

## 3. 运行第一个测试 (2分钟)

### 方式一：使用 Skills（推荐新手）

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

### 方式二：使用 Agent

```python
from agent.core.agent import SecurityExpertAgent

# 创建 Agent
agent = SecurityExpertAgent({"llm": {"provider": "mock"}})
agent.initialize()

# 执行任务
result = agent.start_task("测试 https://example.com 的 Web 安全")
print(f"状态: {result['status']}")
print(f"发现: {len(result['discoveries'])} 个问题")
```

---

## 4. 下一步

- 📖 阅读 [完整使用指南](./USAGE_GUIDE.md)
- 🔧 配置 [LLM API](./docs/configuration.md)
- 📚 查看 [API 参考](./docs/api.md)
- 💡 浏览 [示例代码](./examples/)

---

## 常用命令

```bash
# 运行测试
python -m pytest tests/

# 使用 CLI
python agent/cli.py test
python agent/cli.py start "测试 https://example.com"

# 安装安全工具
./scripts/install_tools.sh
```

---

## 需要帮助？

- 查看 [常见问题](./USAGE_GUIDE.md#常见问题)
- 提交 [Issue](https://github.com/ElaineRosa6/ai-security-researcher-workspace/issues)
