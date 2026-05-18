# AI Security Researcher Workspace - 下一步实施计划

> **文档版本**: 2.0  
> **更新日期**: 2026-05-18  
> **基于**: 代码审查和项目现状分析  
> **当前分支**: master  
> **最新提交**: de45312c6a92aed5a4614e5099f39cded580401b (2026-05-14)

---

## 📊 项目当前状态总览

### ✅ 已完成的核心模块

| 模块 | 完成度 | 状态 | 说明 |
|------|--------|------|------|
| **Agent核心系统** | 95% | ✅ | 完整的Agent框架，包含LLM集成 |
| **Skills技能库** | 85% | ✅ | 11个技能模块，覆盖红蓝紫队 |
| **Brain决策引擎** | 95% | ✅ | 需求解析、任务规划、技能执行 |
| **LLM客户端** | 95% | ✅ | OpenAI/Claude/Mock完整实现 |
| **提示词系统** | 90% | ✅ | 所有提示词文件就位 |
| **工作流引擎** | 85% | ✅ | 状态机和YAML工作流 |
| **质量控制系统** | 90% | ✅ | Validator/Auditor/SelfAssessment |
| **记忆系统** | 90% | ✅ | 5层记忆架构 |
| **知识图谱** | 80% | ✅ | 漏洞库、攻击模式库 |
| **文档和测试** | 70% | ⚠️ | 基础文档完成，待完善 |

### 🔴 待完善的关键功能

| 功能 | 优先级 | 依赖 | 预计工时 |
|------|--------|------|----------|
| **Skills实际集成** | P0 | Agent初始化 | 4h |
| **工具执行引擎** | P0 | 无 | 8h |
| **工作流YAML执行** | P0 | 状态机 | 6h |
| **完整测试覆盖** | P1 | 基础功能 | 8h |
| **CLI完整接口** | P1 | 无 | 4h |
| **报告模板系统** | P1 | 无 | 6h |
| **持久化层** | P2 | 无 | 6h |
| **CI/CD集成** | P2 | 无 | 4h |

---

## 🎯 下一阶段实施计划（4-6周）

### 第一阶段：核心功能补全（Week 1-2）

#### 🔴 Week 1: Skills集成和工具执行引擎

**目标**：让Skills能被Agent正确调用，实现真正的工具执行

| Day | 任务 | 文件 | 输出 |
|-----|------|------|------|
| 1-2 | 实现SkillsManager | `agent/skills/__init__.py` | 技能注册管理 |
| 3-4 | 实现工具执行器基础 | `ai-agent/harness/tool_executor.py` | 命令执行框架 |
| 5-7 | Nmap/SQLMap集成 | `ai-agent/harness/tool_executor.py` | 工具调用能力 |

**关键代码**：

```python
# agent/skills/__init__.py
class SkillsManager:
    def __init__(self, config):
        self.config = config
        self.skills = {}
    
    def register_all(self, brain):
        from ai_agent.skills.red_team.web_security import WebSecuritySkill
        brain.register_skill('WebSecuritySkill', WebSecuritySkill())
        # ... 其他技能
```

```python
# ai-agent/harness/tool_executor.py
class ToolExecutor:
    def execute_nmap(self, target, flags='-sV -sC'):
        """执行Nmap扫描"""
        cmd = ['nmap'] + flags.split() + [target]
        result = subprocess.run(cmd, capture_output=True, timeout=300)
        return self.parse_nmap_output(result.stdout)
```

#### 🟡 Week 2: 工作流执行和结果解析

**目标**：让YAML工作流能被实际执行

| Day | 任务 | 文件 | 输出 |
|-----|------|------|------|
| 8-9 | 完善YAML加载器 | `agent/workflow/yaml_loader.py` | 工作流加载验证 |
| 10-11 | 实现任务调度器 | `agent/workflow/runner.py` | 任务执行引擎 |
| 12-14 | 结果解析系统 | `agent/workflow/result_parser.py` | 结构化输出 |

---

### 第二阶段：用户体验完善（Week 3-4）

#### 🟡 Week 3: CLI和报告系统

**目标**：提供完整的命令行接口和报告生成

| Day | 任务 | 文件 | 输出 |
|-----|------|------|------|
| 15-16 | 完善CLI命令 | `agent/cli.py` | 完整命令集 |
| 17-18 | 报告模板 | `agent/reporting/templates/` | Markdown模板 |
| 19-21 | HTML/PDF导出 | `agent/reporting/exporter.py` | 多格式报告 |

**CLI命令设计**：

```bash
# 启动Agent进行渗透测试
python agent/cli.py start "对 https://example.com 进行Web渗透测试"

# 查看工作流列表
python agent/cli.py list-workflows

# 查看会话状态
python agent/cli.py status <session-id>

# 生成报告
python agent/cli.py report <session-id> --format md
```

#### 🟡 Week 4: 测试覆盖和CI/CD

**目标**：达到80%+测试覆盖率

| Day | 任务 | 文件 | 输出 |
|-----|------|------|------|
| 22-23 | 补充集成测试 | `tests/integration/` | Skills/Harness测试 |
| 24-25 | E2E测试 | `tests/e2e/` | 完整工作流测试 |
| 26-28 | CI/CD配置 | `.github/workflows/` | GitHub Actions |

---

### 第三阶段：生产环境准备（Week 5-6）

#### 🟢 Week 5: 持久化和Docker化

**目标**：支持数据持久化和容器化部署

| Day | 任务 | 文件 | 输出 |
|-----|------|------|------|
| 29-31 | 数据库集成 | `agent/persistence/` | SQLite/PostgreSQL |
| 32-33 | Docker配置 | `Dockerfile`, `docker-compose.yml` | 容器化部署 |
| 34-35 | 配置管理 | `config/` | 环境配置系统 |

#### 🟢 Week 6: 文档完善和发布

**目标**：完整的用户和开发者文档

| Day | 任务 | 文件 | 输出 |
|-----|------|------|------|
| 36-38 | API文档 | `docs/api.md` | Sphinx autodoc |
| 39-40 | 用户手册 | `docs/user-guide/` | 使用指南 |
| 41-42 | 发布准备 | GitHub Release | 版本发布 |

---

## 📋 详细任务清单

### P0 必须完成（才能运行）

```markdown
agent/skills/__init__.py
├── [ ] SkillsManager类
│   ├── register_all(brain)方法
│   ├── get_skill(name)方法
│   └── list_skills()方法
├── [ ] 技能导入
│   ├── WebSecuritySkill
│   ├── ThreatIntelSkill
│   ├── IncidentResponseSkill
│   └── ... 其他技能
└── [ ] 单元测试

ai-agent/harness/tool_executor.py
├── [ ] ToolExecutor基类
│   ├── execute_command(cmd)方法
│   ├── set_timeout(seconds)方法
│   └── parse_output(tool, output)方法
├── [ ] Nmap集成
│   ├── execute_nmap(target, flags)方法
│   └── parse_nmap_output(xml)方法
├── [ ] SQLMap集成
│   ├── execute_sqlmap(url, params)方法
│   └── parse_sqlmap_output(text)方法
└── [ ] Burp Suite集成
    ├── start_burp()方法
    └── scan_target(url)方法

agent/workflow/runner.py
├── [ ] WorkflowRunner类
│   ├── load_workflow(name)方法
│   ├── execute(workflow)方法
│   ├── pause()方法
│   └── resume()方法
├── [ ] 任务调度器
│   ├── add_task(task)方法
│   ├── execute_next()方法
│   └── handle_dependencies()方法
└── [ ] 状态持久化
    ├── save_state()方法
    └── load_state()方法
```

### P1 重要功能

```markdown
agent/cli.py
├── [ ] start命令
├── [ ] status命令
├── [ ] report命令
├── [ ] list-workflows命令
└── [ ] config命令

agent/reporting/
├── [ ] templates/pentest_report.md
├── [ ] templates/incident_report.md
├── [ ] generator.py
├── [ ] exporter.py (HTML/PDF)
└── [ ] templates/executive_summary.md

tests/
├── [ ] integration/test_skills.py (补充)
├── [ ] integration/test_workflow.py
├── [ ] e2e/test_web_pentest.py
├── [ ] e2e/test_incident_response.py
└── [ ] fixtures/sample_targets.py
```

### P2 优化功能

```markdown
agent/persistence/
├── [ ] models.py (SQLAlchemy)
├── [ ] session_store.py
├── [ ] findings_store.py
└── [ ] alembic migrations/

.github/workflows/
├── [ ] ci.yml (测试)
├── [ ] cd.yml (发布)
└── [ ] security.yml (安全扫描)

Docker/
├── [ ] Dockerfile
├── [ ] docker-compose.yml
└── [ ] .dockerignore
```

---

## 🎯 里程碑计划

### M1: 可运行MVP (Week 2结束)
- [ ] Skills能被Agent正确调用
- [ ] Nmap/SQLMap工具可执行
- [ ] 基础Web渗透测试工作流可运行
- [ ] 基础报告生成

**验收标准**：
```bash
python agent/cli.py start "测试 https://example.com"
# 应该能执行完整的渗透测试并生成报告
```

### M2: 测试达标 (Week 4结束)
- [ ] 测试覆盖率 > 80%
- [ ] 所有单元测试通过
- [ ] E2E测试覆盖主要场景
- [ ] CI/CD流程就绪

**验收标准**：
```bash
pytest tests/ --cov=agent --cov-report=html
# 覆盖率报告 > 80%
```

### M3: 生产就绪 (Week 6结束)
- [ ] 持久化层完整
- [ ] Docker化完成
- [ ] 文档完整
- [ ] 发布v1.0.0

---

## 🔧 实施建议

### 1. 开发流程

```bash
# 每日开发
git checkout -b feature/skill-integration
# 开发...
git add .
git commit -m "feat: implement skills registration"
# 推送并创建PR
git push origin feature/skill-integration
```

### 2. 代码规范

- **Python**: PEP 8 + Black格式化
- **测试**: pytest + pytest-cov
- **文档**: Markdown + Sphinx
- **配置**: YAML

### 3. 质量标准

| 指标 | 目标 |
|------|------|
| 测试覆盖率 | > 80% |
| 文档覆盖率 | 100% |
| 所有测试通过 | 必须 |
| P0功能完成 | 必须 |

### 4. 代码审查要点

- LLM集成安全性（API密钥管理）
- 工具执行安全性（命令注入防护）
- 敏感信息处理
- 错误处理和日志记录

---

## 📈 项目进度追踪

### 当前完成度：约 75-80%

```
完成度进度条：
[████████████████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░] 75-80%

各模块状态：
✅ Agent核心框架    [████████████████████████████] 95%
✅ Skills技能库     [████████████████████████░░░░] 85%
✅ Brain决策引擎    [████████████████████████████] 95%
✅ LLM客户端        [████████████████████████████] 95%
✅ 提示词系统       [██████████████████████████░░░] 90%
✅ 工作流引擎       [████████████████████████░░░░] 85%
✅ 质量控制         [██████████████████████████░░░] 90%
✅ 记忆系统         [██████████████████████████░░░] 90%
⚠️ 工具执行         [████████████░░░░░░░░░░░░░░░░░] 50%
⚠️ 测试覆盖         [███████████░░░░░░░░░░░░░░░░░░] 60%
⚠️ CLI接口          [██████████░░░░░░░░░░░░░░░░░░░] 50%
⚠️ 报告系统         [██████████░░░░░░░░░░░░░░░░░░░] 50%
⚠️ 文档             [███████████░░░░░░░░░░░░░░░░░░] 70%
```

---

## 🚀 快速启动指南

### 本周立即开始的任务

1. **创建SkillsManager**
   ```bash
   # 创建文件: agent/skills/__init__.py
   # 实现技能注册和管理
   ```

2. **实现工具执行器**
   ```bash
   # 创建文件: ai-agent/harness/tool_executor.py
   # 实现命令执行和结果解析
   ```

3. **补充集成测试**
   ```bash
   # 完善: tests/integration/test_skills.py
   # 完善: tests/integration/test_harness.py
   ```

---

## 📝 相关文档

- [README.md](README.md) - 项目简介
- [IMPLEMENTATION_REPORT.md](IMPLEMENTATION_REPORT.md) - 实现状态报告
- [CRITICAL_MISSING_COMPONENTS.md](CRITICAL_MISSING_COMPONENTS.md) - 关键缺失组件
- [NEXT_PHASE_PLAN.md](NEXT_PHASE_PLAN.md) - 上一版计划（存档）

---

**文档维护**：
- 每周更新进度
- 每两周审查计划
- 里程碑达成后更新版本号

**最后更新**: 2026-05-18
**下次审查**: 2026-05-25
