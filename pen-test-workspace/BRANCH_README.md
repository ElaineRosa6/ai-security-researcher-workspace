# 项目分支说明

## 🌿 分支结构

### 1. `autonomous-agent` - 自主AI Agent分支
**用途**：完整的自主AI安全专家Agent
- 内置LLMClient
- 自主推理、决策、执行
- 完整的Agent架构（Brain、Memory、Workflows等）
- 可以独立运行，完成安全测试任务

```python
# 使用方式
from agent.core.agent import SecurityExpertAgent
agent = SecurityExpertAgent(config)
result = agent.start_task("测试 https://example.com")
```

---

### 2. `skills-library` - Skills化分支
**用途**：供Claude Code/Codex/其他Agent调用的纯技能库
- 无自主Agent逻辑
- 无内置LLM
- 提供简单、清晰的API
- 被外部Agent控制使用

```python
# 使用方式
from pen_test_workspace.skills.web import scan_website
result = scan_website("https://example.com")
# 外部LLM自己分析result
```

---

### 3. `master` - 主分支
- 保留当前状态
- 作为两个分支的基础
