
# AI Agent工作区完整目录结构

## 完整文件树

```
pen-test-workspace/
│
├── README.md                          # 总览文档
├── LICENSE                            # 许可证
├── .gitignore                         # Git忽略配置
├── .env.example                       # 环境变量示例
│
├── agent/                             # AI Agent核心系统 ⭐ 新增
│   ├── __init__.py
│   ├── core/                          # 核心模块
│   │   ├── __init__.py
│   │   ├── agent.py                   # Agent主类
│   │   ├── brain.py                   # 智能决策中心
│   │   ├── planner.py                 # 任务规划器
│   │   ├── executor.py                # 执行控制器
│   │   ├── evaluator.py               # 评估器
│   │   ├── reasoner.py                # 推理引擎
│   │   └── decision_maker.py          # 决策器
│   │
│   ├── memory/                        # 记忆系统
│   │   ├── __init__.py
│   │   ├── memory_manager.py          # 记忆管理器
│   │   ├── short_term.py              # 短期记忆
│   │   ├── medium_term.py             # 中期记忆
│   │   ├── long_term.py               # 长期记忆
│   │   ├── episodic.py                # 情景记忆
│   │   └── semantic.py                # 语义记忆
│   │
│   ├── knowledge/                     # 知识图谱
│   │   ├── __init__.py
│   │   ├── graph.py                   # 知识图谱实现
│   │   ├── vulnerability_db/          # 漏洞知识库
│   │   │   ├── cve_database.json
│   │   │   ├── exploit_db.json
│   │   │   └── vulnerability_patterns.json
│   │   ├── attack_patterns/           # 攻击模式库
│   │   │   ├── web_attacks.json
│   │   │   ├── binary_exploits.json
│   │   │   └── post_exploitation.json
│   │   ├── tool_knowledge/            # 工具知识库
│   │   │   ├── tools_index.json
│   │   │   ├── nmap_usage.json
│   │   │   ├── burp_usage.json
│   │   │   └── metasploit_usage.json
│   │   └── methodology/               # 方法论库
│   │       ├── web_pentest.json
│   │       ├── mobile_pentest.json
│   │       ├── domain_pentest.json
│   │       └── incident_response.json
│   │
│   ├── workflow/                      # 智能工作流引擎
│   │   ├── __init__.py
│   │   ├── engine.py                  # 工作流引擎
│   │   ├── state_tracker.py           # 状态追踪器
│   │   ├── transition.py              # 状态转换器
│   │   ├── dynamic_adapter.py         # 动态适配器
│   │   └── definitions/               # 工作流定义
│   │       ├── web_pentest.yaml
│   │       ├── incident_response.yaml
│   │       ├── forensics.yaml
│   │       └── domain_pentest.yaml
│   │
│   ├── quality/                       # 质量控制层
│   │   ├── __init__.py
│   │   ├── validator.py               # 验证器
│   │   ├── checker.py                 # 检查器
│   │   ├── auditor.py                 # 审计器
│   │   └── self_assessment.py         # 自我评估
│   │
│   ├── awareness/                     # 自我认知系统
│   │   ├── __init__.py
│   │   ├── state_awareness.py         # 状态感知
│   │   ├── context_awareness.py       # 上下文感知
│   │   └── decision_guide.py          # 决策引导
│   │
│   ├── prompts/                       # 提示工程体系
│   │   ├── system/                    # 系统提示词
│   │   │   ├── identity.txt           # 角色定义
│   │   │   ├── methodology.txt        # 方法论
│   │   │   └── principles.txt         # 原则
│   │   ├── task/                      # 任务提示词
│   │   │   ├── requirement_analysis.txt
│   │   │   ├── planning.txt
│   │   │   ├── execution.txt
│   │   │   └── reporting.txt
│   │   ├── tool/                      # 工具提示词
│   │   │   ├── nmap.txt
│   │   │   ├── burp.txt
│   │   │   ├── sqlmap.txt
│   │   │   └── metasploit.txt
│   │   ├── reasoning/                 # 推理提示词
│   │   │   ├── chain_of_thought.txt
│   │   │   ├── decision_making.txt
│   │   │   └── problem_solving.txt
│   │   └── quality/                   # 质量提示词
│   │       ├── self_check.txt
│   │       ├── evidence_validation.txt
│   │       └── final_review.txt
│   │
│   ├── meta/                          # 元系统
│   │   ├── __init__.py
│   │   ├── monitor.py                 # 自我监控
│   │   ├── learning.py                # 学习系统
│   │   ├── improvement.py             # 持续改进
│   │   └── telemetry.py               # 遥测系统
│   │
│   └── start.py                       # Agent启动脚本
│
├── red-team/                          # 红队攻击场景
│   ├── web-security/                  # Web安全
│   │   ├── tools/                     # Web安全工具
│   │   ├── exploits/                  # Web利用代码
│   │   ├── payloads/                  # Web载荷
│   │   ├── wordlists/                 # 字典
│   │   └── templates/                 # 模板
│   ├── binary-security/               # 二进制安全
│   │   ├── pwn/                      # PWN
│   │   ├── reverse-engineering/       # 逆向工程
│   │   ├── fuzzing/                   # 模糊测试
│   │   └── debugger/                  # 调试器配置
│   ├── mobile-app/                    # 移动应用安全
│   │   ├── android/
│   │   ├── ios/
│   │   └── frida-scripts/
│   ├── miniprogram/                   # 微信小程序安全
│   │   ├── unpack/
│   │   ├── audit/
│   │   └── hooks/
│   ├── domain-pentest/                # 域渗透
│   │   ├── enumeration/
│   │   ├── lateral-movement/
│   │   ├── privilege-escalation/
│   │   └── persistence/
│   ├── phishing/                      # 钓鱼
│   │   ├── templates/
│   │   ├── payload-generators/
│   │   └── delivery/
│   ├── anonymity/                     # 匿名与代理 ⭐ 新增
│   │   ├── proxies/                   # 代理工具
│   │   ├── chains/                    # 代理链
│   │   ├── tor/                       # Tor配置
│   │   ├── i2p/                       # I2P配置
│   │   └── vpn/                       # VPN配置
│   └── infrastructure/                # 基础设施攻击
│       ├── cloud/
│       ├── network/
│       └── wireless/
│
├── blue-team/                         # 蓝队防御场景
│   ├── incident-response/             # 应急响应
│   │   ├── playbooks/
│   │   ├── forensics/
│   │   ├── malware-analysis/
│   │   └── reporting/
│   ├── threat-intel/                  # 威胁情报
│   │   ├── feeds/
│   │   ├── analysis/
│   │   └── indicators/
│   ├── monitoring/                    # 监控
│   │   ├── logs/
│   │   ├── alerts/
│   │   └── dashboards/
│   └── hardening/                     # 加固
│       ├── benchmarks/
│       ├── checklists/
│       └── scripts/
│
├── purple-team/                       # 紫队协作场景
│   ├── attack-simulation/             # 攻击模拟
│   ├── defense-validation/            # 防御验证
│   ├── forensics/                     # 溯源取证
│   │   ├── disk-forensics/
│   │   ├── memory-forensics/
│   │   ├── network-forensics/
│   │   └── timeline/
│   └── training/                      # 训练
│
├── compliance/                        # 合规与记录 ⭐ 新增
│   ├── recordings/                    # 录屏文件
│   │   ├── screen/                    # 屏幕录制
│   │   ├── terminal/                  # 终端录制
│   │   └── network/                   # 网络流量录制
│   ├── logs/                          # 操作日志
│   │   ├── audit/                     # 审计日志
│   │   ├── command/                   # 命令日志
│   │   └── session/                   # 会话日志
│   ├── evidence/                      # 证据管理
│   │   ├── chain-of-custody/          # 证据链
│   │   ├── hashes/                    # 文件哈希
│   │   └── signatures/                # 数字签名
│   ├── policies/                      # 合规策略
│   └── checklists/                    # 合规检查清单
│
├── shared/                            # 共享资源
│   ├── tools/                         # 通用工具
│   ├── wordlists/                     # 字典
│   ├── templates/                     # 模板
│   ├── datasets/                      # 数据集
│   └── documentation/                 # 文档
│
├── ai-agent/                          # Skills和Harness
│   ├── skills/                        # Skills模块
│   │   ├── red_team/
│   │   │   ├── web_security.py
│   │   │   ├── binary_security.py
│   │   │   ├── mobile_security.py
│   │   │   ├── domain_pentest.py
│   │   │   └── anonymity.py          # 匿名Skill ⭐ 新增
│   │   ├── blue_team/
│   │   │   ├── incident_response.py
│   │   │   └── threat_intel.py
│   │   ├── purple_team/
│   │   │   ├── forensics.py
│   │   │   └── attack_simulation.py
│   │   ├── compliance/                # 合规Skills ⭐ 新增
│   │   │   ├── recording.py
│   │   │   ├── evidence.py
│   │   │   └── compliance.py
│   │   ├── general/
│   │   │   ├── tools.py
│   │   │   └── reporting.py
│   │   └── __init__.py
│   │
│   ├── harness/                       # Harness框架
│   │   ├── web_security_harness.py
│   │   ├── binary_harness.py
│   │   ├── domain_pentest_harness.py
│   │   ├── incident_response_harness.py
│   │   ├── forensics_harness.py
│   │   ├── anonymity_harness.py      # 匿名Harness ⭐ 新增
│   │   ├── compliance_harness.py     # 合规Harness ⭐ 新增
│   │   ├── session_harness.py        # 会话Harness ⭐ 新增
│   │   ├── generic_harness.py
│   │   └── __init__.py
│   │
│   ├── prompts/                       # 提示词
│   └── workflows/                     # 工作流定义
│       ├── web_pentest.yaml
│       ├── incident_response.yaml
│       ├── forensics.yaml
│       ├── domain_pentest.yaml
│       ├── full_session.yaml          # 完整会话工作流 ⭐ 新增
│       └── anonymity_test.yaml        # 匿名测试工作流 ⭐ 新增
│
├── workspace-data/                    # 工作区数据 ⭐ 新增
│   ├── current-session/               # 当前会话数据
│   │   ├── state.json                 # 当前状态
│   │   ├── context.json               # 上下文数据
│   │   ├── memory.json                # 记忆快照
│   │   ├── target_profile.json        # 目标画像
│   │   ├── discoveries.json           # 发现
│   │   └── execution.log              # 执行日志
│   ├── sessions-history/              # 历史会话
│   │   ├── session_001/
│   │   ├── session_002/
│   │   └── ...
│   └── knowledge-base/                # 知识库
│       ├── vulnerabilities/
│       ├── techniques/
│       ├── best_practices/
│       └── learned_lessons/
│
├── config/                            # 配置文件
│   ├── agent/                         # Agent配置 ⭐ 新增
│   │   ├── core.yaml                  # 核心配置
│   │   ├── memory.yaml                # 记忆系统配置
│   │   ├── workflow.yaml              # 工作流配置
│   │   ├── quality.yaml               # 质量配置
│   │   └── prompt_templates.yaml      # 提示模板配置
│   ├── tools/                         # 工具配置
│   ├── environment/                   # 环境配置
│   ├── proxy/                         # 代理配置 ⭐ 新增
│   │   ├── tor.yaml
│   │   ├── proxychains.yaml
│   │   └── vpn.yaml
│   ├── compliance/                    # 合规配置 ⭐ 新增
│   │   ├── recording.yaml
│   │   ├── evidence.yaml
│   │   └── session.yaml
│   └── profiles/                      # 配置文件
│       ├── default.yaml
│       ├── stealth.yaml
│       └── full_audit.yaml
│
├── output/                            # 输出目录
│   ├── reports/                       # 报告
│   ├── logs/                          # 日志
│   ├── artifacts/                     # 工件
│   └── screenshots/                   # 截图
│
└── docs/                              # 文档
    ├── agent-guide.md                 # Agent使用指南
    ├── workflow-guide.md              # 工作流指南
    ├── skill-reference.md             # Skill参考
    ├── prompt-engineering.md          # 提示工程指南
    └── faq.md                         # 常见问题
```

## 目录详细说明

### 1. agent/ - AI Agent核心系统

这是整个工作区的大脑！让AI Agent能够像专家一样思考。

```
agent/
├── core/             # Agent核心智能
├── memory/           # 记忆系统 - 短期/中期/长期/情景/语义
├── knowledge/        # 知识图谱 - 漏洞/攻击模式/工具知识
├── workflow/         # 智能工作流 - 状态管理/动态调整
├── quality/          # 质量控制 - 验证/审计/自我评估
├── awareness/        # 自我认知 - 状态感知/上下文理解
├── prompts/          # 提示工程 - 系统/任务/工具/推理提示词
└── meta/             # 元系统 - 自我监控/学习/改进
```

### 2. compliance/ - 合规与记录

确保所有操作都合规、可审计、有完整证据链。

```
compliance/
├── recordings/       # 录制 - 屏幕/终端/网络
├── logs/             # 日志 - 审计/命令/会话
├── evidence/         # 证据 - 证据链/哈希/签名
├── policies/         # 策略
└── checklists/       # 检查清单
```

### 3. workspace-data/ - 工作区数据

Agent运行时的数据存储区。

```
workspace-data/
├── current-session/  # 当前会话 - 状态/上下文/记忆/目标画像
├── sessions-history/ # 历史会话
└── knowledge-base/   # 知识库 - 持久化的学习成果
```

### 4. config/ - 配置文件

```
config/
├── agent/           # Agent配置
│   ├── core.yaml    # 核心设置
│   ├── memory.yaml  # 记忆系统设置
│   └── ...
├── proxy/           # 代理配置
│   ├── tor.yaml
│   ├── proxychains.yaml
│   └── vpn.yaml
└── compliance/      # 合规配置
    ├── recording.yaml
    ├── evidence.yaml
    └── session.yaml
```

## Agent如何与工作区交互

### Agent启动流程

```python
# Agent启动时会:

1. 读取配置
   config = load_config("config/agent/core.yaml")

2. 初始化记忆系统
   memory = MemoryManager(config)

3. 初始化知识图谱
   knowledge = KnowledgeGraph()
   knowledge.load_from("agent/knowledge/")

4. 初始化工作流引擎
   workflow = WorkflowEngine(config, memory)

5. 启动合规记录
   compliance = ComplianceHarness(config)
   compliance.start_recording()

6. 配置匿名网络
   anonymity = AnonymityHarness(config)
   anonymity.setup()

7. 准备就绪，等待任务！
   agent = SecurityAgent(memory, workflow, knowledge, ...)
```

### Agent执行任务时的数据流

```
用户请求
  ↓
Agent感知当前状态
  ↓ (读取 memory/state_tracker)
Agent理解上下文
  ↓ (读取 knowledge graph / target profile)
Agent思考决策
  ↓ (使用 prompts 进行推理)
Agent选择Skill
  ↓
Agent执行Skill
  ↓ (使用 ai-agent/skills/)
结果写入记忆
  ↓
证据存入 compliance/evidence/
日志写入 compliance/logs/
  ↓
Agent评估结果
  ↓
Agent决定下一步
  ↓ (回到感知，继续循环...)
```

## 配置文件示例

### agent/core.yaml (Agent核心配置)

```yaml
agent:
  name: "SecurityExpertAgent"
  version: "1.0"
  role: "expert_pentester"

  capabilities:
    - web_security
    - binary_security
    - mobile_security
    - domain_pentest
    - incident_response
    - forensics

  behavior:
    autonomous: true              # 自主决策
    ask_for_confirmation: false  # 不需要每次都问
    risk_aversion: "balanced"    # 平衡风险
    thoroughness: "high"         # 彻底性高
    explain_decisions: true      # 解释决策过程

  personality:
    curiosity: high              # 好奇心强
    thoroughness: high           # 仔细
    attention_to_detail: high    # 注重细节
    creativity: high             # 创造性
```

### compliance/session.yaml (会话配置)

```yaml
session:
  auto_start: true
  auto_archive: true
  retention_days: 90

  recording:
    screen: true
    terminal: true
    network: false  # 可选，流量太大

  evidence:
    auto_hash: true
    auto_sign: true
    hash_algorithm: "sha256"

  pre_session_checklist:
    - verify_authorization
    - check_anonymity_settings
    - test_recording_tools
    - confirm_target_scope

  post_session_checklist:
    - verify_all_recordings
    - generate_hashes
    - seal_evidence
    - create_report
    - archive_session
```

## 关键文件说明

### Agent相关的关键文件

| 文件 | 用途 |
|------|------|
| agent/core/agent.py | Agent主类 |
| agent/memory/memory_manager.py | 记忆管理 |
| agent/workflow/engine.py | 工作流引擎 |
| agent/knowledge/graph.py | 知识图谱 |
| agent/awareness/state_awareness.py | 状态感知 |

### 合规相关的关键文件

| 文件 | 用途 |
|------|------|
| compliance/evidence/chain-of-custody/ | 证据链存储 |
| ai-agent/harness/compliance_harness.py | 合规Harness |
| ai-agent/skills/compliance/evidence.py | 证据Skill |

### 匿名相关的关键文件

| 文件 | 用途 |
|------|------|
| red-team/anonymity/ | 匿名工具配置 |
| ai-agent/harness/anonymity_harness.py | 匿名Harness |
| ai-agent/skills/red_team/anonymity.py | 匿名Skill |

## 数据持久化策略

### 记忆数据

- 短期记忆: 内存，会话结束后丢弃
- 中期记忆: workspace-data/current-session/
- 长期记忆: workspace-data/knowledge-base/ (持久保存)

### 会话数据

每个会话都会创建独立目录:

```
workspace-data/sessions-history/session_20240430_143022/
├── state_history.json      # 状态变化历史
├── decision_log.json       # 决策日志
├── evidence/              # 证据
└── report/                # 报告
```

---

**这就是完整的AI Agent专用工作区结构！**
