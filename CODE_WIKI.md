# AI安全研究员工作区 - Code Wiki

> **项目名称**: 专家级渗透测试与安全研究员AI Agent工作区
> **文档版本**: 1.0
> **最后更新**: 2026-05-11

---

## 目录

1. [项目概述](#1-项目概述)
2. [项目架构](#2-项目架构)
3. [核心模块详解](#3-核心模块详解)
4. [目录结构](#4-目录结构)
5. [主要类与函数说明](#5-主要类与函数说明)
6. [Skills系统](#6-skills系统)
7. [Harness框架](#7-harness框架)
8. [工作流引擎](#8-工作流引擎)
9. [记忆系统](#9-记忆系统)
10. [知识图谱](#10-知识图谱)
11. [质量控制与自我评估](#11-质量控制与自我评估)
12. [提示工程体系](#12-提示工程体系)
13. [依赖关系](#13-依赖关系)
14. [运行方式](#14-运行方式)
15. [配置文件说明](#15-配置文件说明)
16. [合规与安全](#16-合规与安全)

---

## 1. 项目概述

### 1.1 项目目标

本项目是一个**AI Agent专用渗透测试与安全研究工作区规划**，旨在构建一个让AI Agent能够像顶级人类安全专家一样自主工作的完整系统。

### 1.2 核心设计理念

```
用户需求 → Agent理解 → Agent规划 → Agent执行 → Agent反思 → Agent改进
                ↓
      全程合规记录 + 证据链
```

### 1.3 主要特性

| 特性 | 说明 |
|------|------|
| 🧠 Agent智能系统 | 记忆/知识图谱/自我认知 |
| 🕵️ 匿名与代理 | 完整的匿名网络支持 |
| 📝 合规记录 | 全程录制/证据链/审计 |
| 🔍 质量控制 | 自我验证/自我评估/持续改进 |
| 💡 提示工程 | 完整的提示词体系 |

---

## 2. 项目架构

### 2.1 系统层次架构

```
┌─────────────────────────────────────────────────────────────────┐
│                      Agent交互层                                │
│  需求解析 → 任务规划 → 执行控制 → 结果总结 → 报告生成          │
└─────────────────────────────────────────────────────────────────┘
                                ↓
┌─────────────────────────────────────────────────────────────────┐
│                    智能工作流引擎                                │
│  状态管理 → 流程控制 → 上下文切换 → 动态调整 → 异常处理        │
└─────────────────────────────────────────────────────────────────┘
                                ↓
┌─────────────────────────────────────────────────────────────────┐
│                    记忆系统 (Memory System)                       │
├─────────────────────────────────────────────────────────────────┤
│  短期记忆 │ 中期记忆 │ 长期记忆 │ 情景记忆 │ 语义记忆         │
└─────────────────────────────────────────────────────────────────┘
                                ↓
┌─────────────────────────────────────────────────────────────────┐
│                    知识图谱与上下文管理                          │
│  目标画像 │ 漏洞知识库 │ 攻击链 │ 证据链 │ 威胁情报           │
└─────────────────────────────────────────────────────────────────┘
                                ↓
┌─────────────────────────────────────────────────────────────────┐
│                    任务执行层                                    │
│  Skills调用 │ Harness执行 │ 工具集成 │ 数据处理               │
└─────────────────────────────────────────────────────────────────┘
                                ↓
┌─────────────────────────────────────────────────────────────────┐
│                    质量控制与评估层                              │
│  准确性检查 │ 完整性验证 │ 风险评估 │ 合规审计 │ 自我评估     │
└─────────────────────────────────────────────────────────────────┘
                                ↓
┌─────────────────────────────────────────────────────────────────┐
│                    基础设施层                                    │
│  配置管理 │ 日志系统 │ 存储系统 │ 监控系统 │ 调度系统         │
└─────────────────────────────────────────────────────────────────┘
```

### 2.2 状态流转图

```
状态定义：
┌─────────────────┐
│   INITIALIZED   │  初始化完成
└────────┬────────┘
         ↓
┌─────────────────┐
│   REQUIREMENT   │  需求解析中
│   ANALYSIS      │
└────────┬────────┘
         ↓
┌─────────────────┐
│   PLANNING      │  任务规划中
└────────┬────────┘
         ↓
┌─────────────────┐
│   RECON         │  侦察阶段
└────────┬────────┘
         ↓
┌─────────────────┐
│   SCANNING      │  扫描阶段
└────────┬────────┘
         ↓
┌─────────────────┐
│   VULN_ASSESS   │  漏洞评估
└────────┬────────┘
         ↓
┌─────────────────┐
│   EXPLOITATION  │  漏洞利用
└────────┬────────┘
         ↓
┌─────────────────┐
│   POST_EXPLOIT  │  后渗透
└────────┬────────┘
         ↓
┌─────────────────┐
│   REPORTING     │  报告阶段
└────────┬────────┘
         ↓
┌─────────────────┐
│   COMPLETED     │  完成
└─────────────────┘
```

---

## 3. 核心模块详解

### 3.1 Agent核心模块 (`agent/`)

| 模块 | 说明 |
|------|------|
| `core/` | Agent核心智能：规划器、执行器、评估器、推理引擎、决策器 |
| `memory/` | 记忆系统：短期/中期/长期/情景/语义记忆管理 |
| `knowledge/` | 知识图谱：漏洞库、攻击模式、工具知识、方法论 |
| `workflow/` | 智能工作流：状态追踪、转换规则、动态适配 |
| `quality/` | 质量控制：验证器、检查器、审计器、自我评估 |
| `awareness/` | 自我认知：状态感知、上下文感知、决策引导 |
| `prompts/` | 提示工程：系统提示、任务提示、推理提示、工具提示 |
| `meta/` | 元系统：自我监控、学习、持续改进、遥测 |

### 3.2 安全测试场景模块

| 模块 | 说明 |
|------|------|
| `red-team/` | 红队攻击：Web安全、二进制安全、移动安全、域渗透、钓鱼、匿名 |
| `blue-team/` | 蓝队防御：应急响应、威胁情报、监控、加固 |
| `purple-team/` | 紫队协作：攻击模拟、防御验证、溯源取证 |

### 3.3 支持模块

| 模块 | 说明 |
|------|------|
| `compliance/` | 合规记录：录屏、终端录制、日志、证据管理、策略 |
| `ai-agent/` | Skills与Harness：技能模块和测试框架 |
| `shared/` | 共享资源：工具、字典、模板、数据集 |

---

## 4. 目录结构

```
pen-test-workspace/
│
├── README.md                          # 总览文档
├── LICENSE                            # 许可证
├── .env.example                       # 环境变量示例
│
├── agent/                             # AI Agent核心系统 ⭐
│   ├── __init__.py
│   ├── core/                          # 核心模块
│   │   ├── agent.py                  # Agent主类
│   │   ├── brain.py                  # 智能决策中心
│   │   ├── planner.py                # 任务规划器
│   │   ├── executor.py               # 执行控制器
│   │   ├── evaluator.py               # 评估器
│   │   ├── reasoner.py               # 推理引擎
│   │   └── decision_maker.py         # 决策器
│   │
│   ├── memory/                        # 记忆系统
│   │   ├── memory_manager.py         # 记忆管理器
│   │   ├── short_term.py             # 短期记忆
│   │   ├── medium_term.py            # 中期记忆
│   │   ├── long_term.py              # 长期记忆
│   │   ├── episodic.py                # 情景记忆
│   │   └── semantic.py               # 语义记忆
│   │
│   ├── knowledge/                     # 知识图谱
│   │   ├── graph.py                  # 知识图谱实现
│   │   ├── vulnerability_db/         # 漏洞知识库
│   │   ├── attack_patterns/          # 攻击模式库
│   │   ├── tool_knowledge/          # 工具知识库
│   │   └── methodology/             # 方法论库
│   │
│   ├── workflow/                      # 智能工作流引擎
│   │   ├── engine.py                 # 工作流引擎
│   │   ├── state_tracker.py          # 状态追踪器
│   │   ├── transition.py             # 状态转换器
│   │   ├── dynamic_adapter.py       # 动态适配器
│   │   └── definitions/              # 工作流定义
│   │
│   ├── quality/                       # 质量控制层
│   │   ├── validator.py              # 验证器
│   │   ├── checker.py                # 检查器
│   │   ├── auditor.py                # 审计器
│   │   └── self_assessment.py        # 自我评估
│   │
│   ├── awareness/                     # 自我认知系统
│   │   ├── state_awareness.py        # 状态感知
│   │   ├── context_awareness.py      # 上下文感知
│   │   └── decision_guide.py         # 决策引导
│   │
│   ├── prompts/                       # 提示工程体系
│   │   ├── system/                   # 系统提示词
│   │   ├── task/                     # 任务提示词
│   │   ├── tool/                     # 工具提示词
│   │   ├── reasoning/                # 推理提示词
│   │   └── quality/                  # 质量提示词
│   │
│   ├── meta/                          # 元系统
│   │   ├── monitor.py                # 自我监控
│   │   ├── learning.py               # 学习系统
│   │   ├── improvement.py            # 持续改进
│   │   └── telemetry.py              # 遥测系统
│   │
│   └── start.py                       # Agent启动脚本
│
├── red-team/                          # 红队攻击场景
│   ├── web-security/                  # Web安全
│   ├── binary-security/               # 二进制安全
│   ├── mobile-app/                    # 移动应用安全
│   ├── miniprogram/                   # 微信小程序安全
│   ├── domain-pentest/                # 域渗透
│   ├── phishing/                      # 钓鱼
│   ├── anonymity/                     # 匿名与代理
│   └── infrastructure/                # 基础设施攻击
│
├── blue-team/                         # 蓝队防御场景
│   ├── incident-response/            # 应急响应
│   ├── threat-intel/                  # 威胁情报
│   ├── monitoring/                    # 监控
│   └── hardening/                     # 加固
│
├── purple-team/                       # 紫队协作场景
│   ├── attack-simulation/            # 攻击模拟
│   ├── defense-validation/            # 防御验证
│   ├── forensics/                     # 溯源取证
│   └── training/                      # 训练
│
├── compliance/                        # 合规与记录 ⭐
│   ├── recordings/                   # 录屏文件
│   │   ├── screen/                   # 屏幕录制
│   │   ├── terminal/                  # 终端录制
│   │   └── network/                  # 网络流量录制
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
│   ├── wordlists/                    # 字典
│   ├── templates/                     # 模板
│   ├── datasets/                      # 数据集
│   └── documentation/                 # 文档
│
├── ai-agent/                          # Skills和Harness
│   ├── skills/                        # Skills模块
│   │   ├── red_team/                 # 红队Skills
│   │   ├── blue_team/               # 蓝队Skills
│   │   ├── purple_team/             # 紫队Skills
│   │   ├── compliance/               # 合规Skills
│   │   └── general/                  # 通用Skills
│   │
│   ├── harness/                       # Harness框架
│   │   ├── web_security_harness.py
│   │   ├── binary_harness.py
│   │   ├── domain_pentest_harness.py
│   │   ├── incident_response_harness.py
│   │   ├── forensics_harness.py
│   │   ├── anonymity_harness.py
│   │   ├── compliance_harness.py
│   │   ├── session_harness.py
│   │   └── generic_harness.py
│   │
│   ├── prompts/                       # 提示词
│   └── workflows/                     # 工作流定义
│
├── workspace-data/                    # 工作区数据 ⭐
│   ├── current-session/              # 当前会话数据
│   ├── sessions-history/             # 历史会话
│   └── knowledge-base/               # 知识库
│
├── config/                            # 配置文件 ⭐
│   ├── agent/                        # Agent配置
│   ├── tools/                        # 工具配置
│   ├── environment/                  # 环境配置
│   ├── proxy/                        # 代理配置
│   ├── compliance/                   # 合规配置
│   └── profiles/                     # 配置文件
│
├── output/                            # 输出目录
│   ├── reports/                      # 报告
│   ├── logs/                         # 日志
│   ├── artifacts/                    # 工件
│   └── screenshots/                  # 截图
│
└── docs/                             # 文档
```

---

## 5. 主要类与函数说明

### 5.1 记忆系统

#### MemoryManager - 记忆管理器

```python
class MemoryManager:
    def __init__(self):
        self.short_term = ShortTermMemory()
        self.medium_term = MediumTermMemory()
        self.long_term = LongTermMemory()
        self.episodic = EpisodicMemory()
        self.semantic = SemanticMemory()
    
    def store(self, data, memory_type):
        """存储数据到指定记忆层"""
    
    def retrieve(self, query, memory_type=None):
        """根据查询检索记忆"""
    
    def update(self, data_id, updates, memory_type):
        """更新记忆数据"""
    
    def consolidate(self):
        """记忆整合 - 将短期记忆合并到中期/长期记忆"""
    
    def forget(self, criteria):
        """选择性遗忘"""
    
    def get_context(self):
        """获取当前上下文"""
```

#### 记忆数据模型

**短期记忆结构**:
```python
{
    "session_id": "uuid",
    "timestamp": "iso8601",
    "current_task": "任务描述",
    "current_step": "当前步骤",
    "recent_actions": [...],
    "active_context": {...},
    "working_memory": "临时工作数据"
}
```

**中期记忆结构**:
```python
{
    "session_id": "uuid",
    "discoveries": [...],
    "attack_history": [],
    "target_profile": {...},
    "decision_history": [],
    "failure_analysis": []
}
```

**长期记忆结构**:
```python
{
    "knowledge_base": {...},
    "pattern_recognition": {...},
    "experience": {...},
    "best_practices": []
}
```

### 5.2 工作流引擎

#### WorkflowEngine - 工作流引擎

```python
class WorkflowEngine:
    def __init__(self, state_tracker, memory_manager):
        self.state_tracker = state_tracker
        self.memory_manager = memory_manager
        self.transition_rules = self.load_transition_rules()
        self.dynamic_adapters = []
    
    def execute_workflow(self, task_definition):
        """执行工作流"""
    
    def execute_state_actions(self, state):
        """执行状态对应的动作"""
    
    def decide_next_state(self):
        """智能决定下一个状态"""
    
    def register_dynamic_adapter(self, adapter):
        """注册动态适配器"""
```

#### StateTracker - 状态追踪器

```python
class StateTracker:
    def __init__(self):
        self.current_state = "INITIALIZED"
        self.state_history = []
        self.state_context = {}
        self.state_metadata = {}
    
    def get_current_state(self):
        """获取当前状态"""
    
    def transition_to(self, new_state, reason=None):
        """状态转换"""
    
    def update_context(self, key, value):
        """更新状态上下文"""
    
    def should_continue(self):
        """判断是否应该继续执行"""
    
    def is_state_completed(self, state):
        """判断状态是否已完成"""
```

### 5.3 任务规划与执行

#### TaskPlanner - 任务规划器

```python
class TaskPlanner:
    def __init__(self, memory_manager, knowledge_graph):
        self.memory_manager = memory_manager
        self.knowledge_graph = knowledge_graph
    
    def parse_requirement(self, requirement_text):
        """解析用户需求"""
        return {
            "task_type": "...",
            "target": "...",
            "scope": "...",
            "constraints": "...",
            "objectives": [],
            "deliverables": "..."
        }
    
    def create_task_plan(self, requirement):
        """创建任务计划"""
    
    def refine_plan(self, current_plan, new_information):
        """基于新信息细化计划"""
    
    def identify_missing_information(self, plan):
        """识别缺少的信息"""
    
    def prioritize_tasks(self, tasks):
        """任务优先级排序"""
```

#### ExecutionController - 执行控制器

```python
class ExecutionController:
    def __init__(self, workflow_engine, memory_manager, skills_registry):
        self.workflow_engine = workflow_engine
        self.memory_manager = memory_manager
        self.skills_registry = skills_registry
        self.execution_history = []
    
    def execute_task(self, task):
        """执行单个任务"""
    
    def select_appropriate_skill(self, task):
        """选择合适的Skill"""
    
    def prepare_execution_context(self, task):
        """准备执行上下文"""
    
    def handle_execution_failure(self, execution_record):
        """处理执行失败"""
```

### 5.4 知识图谱

#### ContextGraph - 上下文图谱

```python
class ContextGraph:
    def __init__(self):
        self.graph = {"nodes": [], "edges": []}
    
    def add_node(self, node_id, node_type, properties):
        """添加节点"""
    
    def add_edge(self, from_node, to_node, relation_type, properties=None):
        """添加边"""
    
    def query(self, query_pattern):
        """查询图谱"""
    
    def find_path(self, start_node, end_node):
        """查找节点间路径"""
    
    def get_subgraph(self, center_node, radius=2):
        """获取子图"""
    
    def get_target_profile(self, target_id):
        """获取目标画像"""
```

### 5.5 质量控制

#### Validator - 验证器

```python
class Validator:
    def validate_result(self, result, expected_criteria):
        """验证结果"""
        return {
            "is_valid": True,
            "issues": [],
            "quality_score": 0,
            "confidence": 0
        }
    
    def check_completeness(self, result):
        """检查完整性"""
    
    def check_accuracy(self, result):
        """检查准确性"""
    
    def check_consistency(self, result):
        """检查一致性"""
```

#### SelfAssessment - 自我评估

```python
class SelfAssessment:
    def __init__(self, execution_history, memory_manager):
        self.execution_history = execution_history
        self.memory_manager = memory_manager
    
    def assess_performance(self):
        """评估性能"""
        return {
            "overall_score": 0,
            "strengths": [],
            "weaknesses": [],
            "recommendations": [],
            "lessons_learned": []
        }
    
    def calculate_completion_rate(self):
        """计算完成率"""
    
    def assess_result_quality(self):
        """评估结果质量"""
    
    def generate_improvements(self):
        """生成改进建议"""
```

### 5.6 自我认知

#### AgentAwareness - Agent自我感知

```python
class AgentAwareness:
    def __init__(self, state_tracker, memory_manager):
        self.state_tracker = state_tracker
        self.memory_manager = memory_manager
    
    def get_self_status(self):
        """获取自身状态"""
        return {
            "current_state": ...,
            "context": ...,
            "memory_snapshot": ...,
            "capabilities": ...,
            "current_focus": ...,
            "open_tasks": ...,
            "missing_info": ...
        }
    
    def should_ask_for_clarification(self):
        """判断是否需要向用户澄清"""
```

#### DecisionGuide - 决策引导

```python
class DecisionGuide:
    def __init__(self, knowledge_base, pattern_recognizer):
        self.knowledge_base = knowledge_base
        self.pattern_recognizer = pattern_recognizer
    
    def generate_options(self, context):
        """生成选项列表"""
    
    def evaluate_options(self, options, criteria):
        """评估选项"""
    
    def make_recommendation(self, evaluations):
        """做出推荐"""
```

---

## 6. Skills系统

### 6.1 Red Team Skills

#### WebSecuritySkill - Web安全技能

```python
class WebSecuritySkill:
    def scan_target(self, target: str) -> dict:
        """扫描目标Web应用"""
    
    def sql_injection_test(self, url: str) -> dict:
        """SQL注入测试"""
    
    def xss_test(self, url: str) -> dict:
        """XSS测试"""
    
    def directory_bruteforce(self, url: str, wordlist: str) -> list:
        """目录爆破"""
    
    def exploit_vulnerability(self, vuln_id: str, target: str) -> dict:
        """利用漏洞"""
```

#### BinarySecuritySkill - 二进制安全技能

```python
class BinarySecuritySkill:
    def analyze_binary(self, binary_path: str) -> dict:
        """分析二进制文件"""
    
    def fuzz_binary(self, binary_path: str, iterations: int) -> dict:
        """模糊测试"""
    
    def find_rop_gadgets(self, binary_path: str) -> list:
        """查找ROP gadgets"""
    
    def generate_exploit(self, binary_path: str, exploit_type: str) -> str:
        """生成Exploit"""
```

#### MobileSecuritySkill - 移动应用安全技能

```python
class MobileSecuritySkill:
    def decompile_apk(self, apk_path: str) -> str:
        """反编译APK"""
    
    def static_analysis(self, apk_path: str) -> dict:
        """静态分析"""
    
    def dynamic_analysis(self, apk_path: str, frida_script: str) -> dict:
        """动态分析"""
    
    def hook_function(self, function_name: str, script: str) -> dict:
        """Hook函数"""
    
    def extract_secrets(self, apk_path: str) -> dict:
        """提取敏感信息"""
```

#### DomainPentestSkill - 域渗透技能

```python
class DomainPentestSkill:
    def enumerate_domain(self, domain: str) -> dict:
        """枚举域信息"""
    
    def dump_credentials(self, target: str) -> dict:
        """转储凭证"""
    
    def lateral_movement(self, source: str, target: str) -> dict:
        """横向移动"""
    
    def escalate_privileges(self, target: str) -> dict:
        """权限提升"""
    
    def establish_persistence(self, target: str, method: str) -> dict:
        """建立持久化"""
```

#### AnonymitySkill - 匿名与代理技能

```python
class AnonymitySkill:
    def setup_tor(self, config: dict) -> dict:
        """配置Tor"""
    
    def setup_proxy_chain(self, proxies: list) -> dict:
        """配置代理链"""
    
    def setup_vpn(self, config: dict) -> dict:
        """配置VPN"""
    
    def change_mac_address(self, interface: str, mac: str = None) -> dict:
        """修改MAC地址"""
    
    def route_traffic(self, tool: str, proxy: str) -> dict:
        """路由工具流量"""
    
    def check_anonymity(self) -> dict:
        """检查匿名状态"""
```

### 6.2 Blue Team Skills

#### IncidentResponseSkill - 应急响应技能

```python
class IncidentResponseSkill:
    def triage_incident(self, incident_data: dict) -> dict:
        """事件分类"""
    
    def collect_evidence(self, target: str) -> dict:
        """收集证据"""
    
    def analyze_memory_dump(self, dump_path: str) -> dict:
        """分析内存转储"""
    
    def analyze_logs(self, log_paths: list) -> dict:
        """分析日志"""
    
    def generate_report(self, findings: dict) -> str:
        """生成报告"""
```

#### ThreatIntelSkill - 威胁情报技能

```python
class ThreatIntelSkill:
    def search_ioc(self, ioc: str) -> dict:
        """搜索IOC"""
    
    def enrich_data(self, data: dict) -> dict:
        """数据富化"""
    
    def generate_yara_rule(self, sample_path: str) -> str:
        """生成Yara规则"""
    
    def correlate_incidents(self, incidents: list) -> dict:
        """关联事件"""
    
    def track_actor(self, actor_id: str) -> dict:
        """追踪威胁行为者"""
```

### 6.3 Purple Team Skills

#### ForensicsSkill - 溯源取证技能

```python
class ForensicsSkill:
    def analyze_disk_image(self, image_path: str) -> dict:
        """分析磁盘镜像"""
    
    def recover_deleted_files(self, image_path: str) -> list:
        """恢复删除文件"""
    
    def build_timeline(self, evidence_paths: list) -> dict:
        """构建时间线"""
    
    def analyze_network_traffic(self, pcap_path: str) -> dict:
        """分析网络流量"""
    
    def trace_attribution(self, evidence: dict) -> dict:
        """追踪归因"""
```

#### AttackSimulationSkill - 攻击模拟技能

```python
class AttackSimulationSkill:
    def run_atomic_test(self, test_id: str, target: str) -> dict:
        """运行原子测试"""
    
    def simulate_attack(self, scenario: str, target: str) -> dict:
        """模拟攻击"""
    
    def validate_defense(self, attack_result: dict, defense_config: dict) -> dict:
        """验证防御"""
    
    def generate_assessment(self, simulation_data: dict) -> dict:
        """生成评估"""
```

### 6.4 Compliance Skills

#### RecordingSkill - 记录与录制技能

```python
class RecordingSkill:
    def start_screen_recording(self, output_path: str, config: dict) -> str:
        """开始屏幕录制"""
    
    def stop_screen_recording(self, recording_id: str) -> dict:
        """停止屏幕录制"""
    
    def start_terminal_recording(self, output_path: str) -> str:
        """开始终端录制"""
    
    def start_network_capture(self, output_path: str, filter: str) -> str:
        """开始网络抓包"""
    
    def enable_audit_logging(self, config: dict) -> dict:
        """启用审计日志"""
```

#### EvidenceSkill - 证据管理技能

```python
class EvidenceSkill:
    def generate_hash(self, file_path: str, algorithm: str = "sha256") -> str:
        """生成文件哈希"""
    
    def verify_hash(self, file_path: str, expected_hash: str) -> bool:
        """验证文件哈希"""
    
    def sign_file(self, file_path: str, key_path: str) -> str:
        """签名文件"""
    
    def create_chain_of_custody(self, evidence: dict) -> dict:
        """创建证据链"""
    
    def seal_evidence(self, evidence_path: str, output_path: str) -> str:
        """封存证据"""
```

#### ComplianceSkill - 合规检查技能

```python
class ComplianceSkill:
    def run_compliance_check(self, standard: str) -> dict:
        """运行合规检查"""
    
    def generate_compliance_report(self, findings: dict) -> str:
        """生成合规报告"""
    
    def verify_evidence_integrity(self, evidence_list: list) -> dict:
        """验证证据完整性"""
    
    def check_log_integrity(self, log_paths: list) -> dict:
        """检查日志完整性"""
    
    def archive_session(self, session_id: str, output_path: str) -> dict:
        """归档会话"""
```

### 6.5 General Skills

#### ToolsSkill - 通用工具技能

```python
class ToolsSkill:
    def run_nmap(self, target: str, flags: str) -> dict:
        """运行Nmap扫描"""
    
    def execute_command(self, command: str, timeout: int) -> dict:
        """执行命令"""
    
    def parse_tool_output(self, tool: str, output: str) -> dict:
        """解析工具输出"""
```

#### ReportingSkill - 报告生成技能

```python
class ReportingSkill:
    def generate_pentest_report(self, findings: list) -> str:
        """生成渗透测试报告"""
    
    def create_executive_summary(self, data: dict) -> str:
        """创建执行摘要"""
    
    def export_findings(self, findings: list, format: str) -> str:
        """导出发现"""
```

---

## 7. Harness框架

### 7.1 WebSecurityHarness - Web安全测试Harness

```python
class WebSecurityHarness:
    def __init__(self, config: dict):
        self.config = config
        self.target = config.get('target')
        self.results = []
    
    def run_full_scan(self):
        """运行完整扫描流程"""
    
    def test_sqli(self):
        """测试SQL注入"""
    
    def test_xss(self):
        """测试XSS"""
    
    def test_csrf(self):
        """测试CSRF"""
    
    def test_ssrf(self):
        """测试SSRF"""
    
    def get_results(self):
        """获取结果"""
```

### 7.2 BinaryHarness - 二进制安全Harness

```python
class BinaryHarness:
    def __init__(self, binary_path: str, config: dict):
        self.binary_path = binary_path
        self.config = config
        self.crashes = []
    
    def fuzz(self, iterations: int = 1000):
        """模糊测试"""
    
    def analyze_crash(self, crash_input: bytes):
        """分析崩溃"""
    
    def generate_exploit_template(self, crash_info: dict):
        """生成Exploit模板"""
    
    def verify_exploit(self, exploit: str):
        """验证Exploit"""
```

### 7.3 DomainPentestHarness - 域渗透Harness

```python
class DomainPentestHarness:
    def __init__(self, domain_config: dict):
        self.domain = domain_config.get('domain')
        self.username = domain_config.get('username')
        self.password = domain_config.get('password')
        self.loot = {}
    
    def reconnaissance(self):
        """侦察阶段"""
    
    def initial_access(self):
        """初始访问"""
    
    def privilege_escalation(self):
        """权限提升"""
    
    def lateral_movement(self):
        """横向移动"""
    
    def persistence(self):
        """持久化"""
```

### 7.4 IncidentResponseHarness - 应急响应Harness

```python
class IncidentResponseHarness:
    def __init__(self, incident_config: dict):
        self.incident_id = incident_config.get('incident_id')
        self.evidence = []
        self.timeline = []
    
    def preparation(self):
        """准备阶段"""
    
    def identification(self):
        """识别阶段"""
    
    def containment(self):
        """遏制阶段"""
    
    def eradication(self):
        """根除阶段"""
    
    def recovery(self):
        """恢复阶段"""
    
    def lessons_learned(self):
        """经验总结"""
```

### 7.5 ForensicsHarness - 取证分析Harness

```python
class ForensicsHarness:
    def __init__(self, case_config: dict):
        self.case_id = case_config.get('case_id')
        self.artifacts = []
        self.timeline = []
    
    def acquire_evidence(self, source: str, type: str):
        """获取证据"""
    
    def validate_integrity(self, evidence_path: str):
        """验证完整性"""
    
    def process_artifacts(self):
        """处理人工制品"""
    
    def build_timeline(self):
        """构建时间线"""
    
    def generate_report(self):
        """生成报告"""
```

### 7.6 AnonymityHarness - 匿名与代理Harness

```python
class AnonymityHarness:
    def __init__(self, config: dict):
        self.config = config
        self.active_proxies = []
        self.active_vpn = None
        self.anonymity_level = 0
    
    def setup_tor_network(self):
        """配置Tor网络"""
    
    def setup_proxy_chain(self, proxy_list: list):
        """配置代理链"""
    
    def connect_vpn(self, vpn_config: dict):
        """连接VPN"""
    
    def check_ip_leak(self):
        """检查IP泄露"""
    
    def check_dns_leak(self):
        """检查DNS泄露"""
    
    def route_tool_traffic(self, tool_name: str):
        """路由工具流量"""
```

### 7.7 ComplianceHarness - 合规记录Harness

```python
class ComplianceHarness:
    def __init__(self, session_config: dict):
        self.session_id = session_config.get('session_id')
        self.start_time = None
        self.end_time = None
        self.recordings = {}
        self.evidence = {}
        self.chain_of_custody = []
    
    def start_session(self):
        """开始会话"""
    
    def start_all_recordings(self):
        """开始所有录制"""
    
    def stop_all_recordings(self):
        """停止所有录制"""
    
    def collect_evidence(self, source: str, type: str):
        """收集证据"""
    
    def verify_evidence_integrity(self):
        """验证证据完整性"""
    
    def seal_session_evidence(self):
        """封存会话证据"""
    
    def archive_session(self, output_path: str):
        """归档会话"""
```

### 7.8 SessionHarness - 渗透测试会话Harness

```python
class SessionHarness:
    def __init__(self, config: dict):
        self.config = config
        self.session_id = None
        self.anonymity_harness = None
        self.compliance_harness = None
    
    def initialize(self):
        """初始化会话"""
    
    def setup_anonymity(self, anonymity_config: dict):
        """配置匿名环境"""
    
    def start_compliance_recording(self):
        """开始合规记录"""
    
    def execute_test(self, test_config: dict):
        """执行测试"""
    
    def finalize_session(self):
        """完成会话"""
    
    def generate_final_report(self):
        """生成最终报告"""
```

### 7.9 GenericHarness - 通用测试Harness

```python
class GenericHarness:
    def __init__(self, config: dict):
        self.config = config
        self.state = 'initialized'
        self.logs = []
    
    def setup(self):
        """设置"""
    
    def execute(self):
        """执行"""
    
    def teardown(self):
        """清理"""
    
    def validate(self):
        """验证"""
    
    def run_workflow(self, workflow: list):
        """运行工作流"""
```

---

## 8. 工作流引擎

### 8.1 状态转换规则

```python
TRANSITION_RULES = {
    "INITIALIZED": ["REQUIREMENT_ANALYSIS"],
    "REQUIREMENT_ANALYSIS": ["PLANNING"],
    "PLANNING": ["RECON", "ERROR"],
    "RECON": ["SCANNING", "PLANNING"],
    "SCANNING": ["VULN_ASSESS", "RECON"],
    "VULN_ASSESS": ["EXPLOITATION", "RECON", "SCANNING"],
    "EXPLOITATION": ["POST_EXPLOIT", "VULN_ASSESS", "REPORTING"],
    "POST_EXPLOIT": ["REPORTING", "EXPLOITATION", "VULN_ASSESS"],
    "REPORTING": ["COMPLETED"]
}
```

### 8.2 工作流定义示例 (YAML)

**Web渗透测试工作流**:
```yaml
# ai-agent/workflows/web_pentest.yaml
name: Web Penetration Test
stages:
  - name: Reconnaissance
    skills:
      - WebSecuritySkill.scan_target
      - ToolsSkill.run_nmap
  - name: Vulnerability Assessment
    skills:
      - WebSecuritySkill.directory_bruteforce
      - WebSecuritySkill.sql_injection_test
      - WebSecuritySkill.xss_test
  - name: Exploitation
    skills:
      - WebSecuritySkill.exploit_vulnerability
  - name: Reporting
    skills:
      - ReportingSkill.generate_pentest_report
```

**完整渗透测试会话工作流**:
```yaml
# ai-agent/workflows/full_pentest_session.yaml
name: Full Penetration Test Session
stages:
  - name: Session Initialization
    skills:
      - SessionHarness.initialize
      - ComplianceHarness.start_session
  - name: Anonymity Setup
    skills:
      - AnonymitySkill.setup_tor
      - AnonymitySkill.setup_proxy_chain
      - ComplianceHarness.start_all_recordings
  - name: Reconnaissance
    skills:
      - WebSecuritySkill.scan_target
  - name: Vulnerability Assessment
    skills:
      - WebSecuritySkill.directory_bruteforce
  - name: Exploitation
    skills:
      - WebSecuritySkill.exploit_vulnerability
      - EvidenceSkill.generate_hash
  - name: Reporting
    skills:
      - ReportingSkill.generate_pentest_report
  - name: Session Completion
    skills:
      - ComplianceHarness.stop_all_recordings
      - AnonymityHarness.cleanup
```

---

## 9. 记忆系统

### 9.1 记忆层次结构

| 记忆类型 | 存储位置 | 生命周期 | 容量 | 用途 |
|---------|---------|---------|------|------|
| 短期记忆 | 内存 | 会话 | 100项 | 当前任务、最近操作、工作数据 |
| 中期记忆 | session-db | 会话-30天 | 每会话 | 发现、目标画像、攻击历史 |
| 长期记忆 | knowledge-db | 持久 | 无限 | 漏洞库、工具知识、经验 |
| 情景记忆 | episode-db | 持久 | 无限 | 完整攻击场景、学习经历 |
| 语义记忆 | knowledge-db | 持久 | 无限 | 概念、关系、领域知识 |

### 9.2 记忆管理流程

```
┌─────────────┐
│   新数据    │
└──────┬──────┘
       ↓
┌─────────────┐
│  判断记忆层 │
└──────┬──────┘
       ↓
┌─────────────┐
│   存储记忆  │
└──────┬──────┘
       ↓
┌─────────────┐
│  记忆整合   │  (定期执行)
│  Consolidation│
└──────┬──────┘
       ↓
┌─────────────┐
│  选择性遗忘 │  (按策略)
│   Forget    │
└─────────────┘
```

### 9.3 记忆检索策略

1. **上下文检索**: 基于当前任务上下文检索相关记忆
2. **相似度检索**: 使用嵌入向量计算相似度
3. **时间检索**: 基于时间范围检索
4. **类型检索**: 按记忆类型过滤

---

## 10. 知识图谱

### 10.1 知识库组成

| 知识库 | 内容 | 更新频率 |
|-------|------|---------|
| vulnerability_db | CVE、漏洞模式、利用代码 | 持续更新 |
| attack_patterns | 攻击链、技术手法 | 定期更新 |
| tool_knowledge | 工具使用、参数、技巧 | 按需更新 |
| methodology | 测试方法论、最佳实践 | 定期更新 |

### 10.2 目标画像结构

```json
{
    "target_id": "example.com",
    "profile": {
        "basic_info": {
            "domain": "example.com",
            "ips": ["192.168.1.1"],
            "organization": "Example Corp"
        },
        "services": [...],
        "technologies": [...],
        "vulnerabilities": [...],
        "attack_surface": {
            "attack_paths": [],
            "entry_points": [],
            "critical_assets": []
        }
    }
}
```

---

## 11. 质量控制与自我评估

### 11.1 质量评估维度

| 维度 | 说明 | 权重 |
|------|------|------|
| 完整性 | 是否覆盖所有必要检查项 | 30% |
| 准确性 | 结果是否正确可信 | 30% |
| 一致性 | 结果内部是否一致 | 20% |
| 可重复性 | 结果是否可以复现 | 20% |

### 11.2 自我评估指标

```python
METRICS = {
    "task_completion_rate": 0,      # 任务完成率
    "average_task_time": 0,          # 平均任务时间
    "success_rate": 0,               # 成功率
    "self_correction_count": 0,      # 自我纠正次数
    "knowledge_application_rate": 0, # 知识应用率
    "decision_quality_score": 0      # 决策质量分数
}
```

---

## 12. 提示工程体系

### 12.1 提示词分类

| 类型 | 位置 | 用途 |
|------|------|------|
| 系统提示词 | `agent/prompts/system/` | Agent角色定义、原则、方法论 |
| 任务提示词 | `agent/prompts/task/` | 需求解析、规划、执行、报告 |
| 工具提示词 | `agent/prompts/tool/` | 工具使用说明、参数、示例 |
| 推理提示词 | `agent/prompts/reasoning/` | 思维链、决策、问题解决 |
| 质量提示词 | `agent/prompts/quality/` | 自检、验证、审查 |

### 12.2 Agent角色定义

```
你是一位专家级渗透测试师和安全研究员，拥有以下专业能力：

【核心能力】
- 精通各类漏洞识别与利用技术
- 熟悉红队/蓝队/紫队全流程
- 具备高级恶意代码分析能力
- 擅长移动应用和微信小程序安全
- 精通域渗透和复杂网络环境
- 具备专业的应急响应和溯源能力

【工作原则】
1. 严格遵守授权范围和法律法规
2. 全程保持合规记录与证据链完整
3. 系统化的方法论驱动工作
4. 持续自我评估与优化

【思考方式】
- 使用思维链(Chain of Thought)逐步推理
- 持续回顾与反思工作进展
- 基于证据做出决策
```

### 12.3 任务提示词模板

**需求解析提示词**:
```
【任务】解析安全测试需求
【当前状态】{state_description}
【用户需求】{user_requirement}
【请回答】
1. 理解用户真实需求
2. 确定任务类型
3. 明确任务目标
4. 定义范围边界
5. 识别约束条件
```

**规划提示词**:
```
【任务】制定测试计划
【已知信息】{target_profile}
【请回答】
1. 阶段划分
2. 具体任务
3. 依赖关系
4. 工具选择
5. 风险评估
```

---

## 13. 依赖关系

### 13.1 模块依赖图

```
┌─────────────────────────────────────────────────────────────────┐
│                        Agent主类                                │
│                     (agent/core/agent.py)                       │
└────────────────────────────┬────────────────────────────────────┘
                             │
        ┌────────────────────┼────────────────────┐
        ↓                    ↓                    ↓
┌───────────────┐    ┌───────────────┐    ┌───────────────┐
│   Planner     │    │   Executor    │    │   Evaluator   │
└───────┬───────┘    └───────┬───────┘    └───────┬───────┘
        │                    │                    │
        └────────────────────┼────────────────────┘
                             ↓
                    ┌─────────────────┐
                    │  Memory Manager │
                    └────────┬────────┘
                             │
        ┌────────────────────┼────────────────────┐
        ↓                    ↓                    ↓
┌───────────────┐    ┌───────────────┐    ┌───────────────┐
│  Short/Medium │    │     Long      │    │   Episodic    │
│    Term       │    │     Term      │    │    Memory     │
└───────────────┘    └───────────────┘    └───────────────┘

┌─────────────────────────────────────────────────────────────────┐
│                    Knowledge Graph                              │
│                  (agent/knowledge/graph.py)                     │
└─────────────────────────────────────────────────────────────────┘
                             ↓
┌─────────────────────────────────────────────────────────────────┐
│                    Workflow Engine                              │
│                   (agent/workflow/engine.py)                     │
└─────────────────────────────────────────────────────────────────┘
                             ↓
┌─────────────────────────────────────────────────────────────────┐
│                        Skills                                   │
│                     (ai-agent/skills/)                           │
└─────────────────────────────────────────────────────────────────┘
                             ↓
┌─────────────────────────────────────────────────────────────────┐
│                       Harness                                   │
│                     (ai-agent/harness/)                          │
└─────────────────────────────────────────────────────────────────┘
```

### 13.2 外部依赖工具

**红队工具**:
- Burp Suite, OWASP ZAP, sqlmap (Web安全)
- GDB, pwndbg, Ghidra, radare2 (二进制安全)
- Frida, objection, MobSF (移动安全)
- Impacket, BloodHound, Mimikatz (域渗透)
- Tor, Proxychains, VPN工具 (匿名)

**蓝队工具**:
- Volatility, Autopsy (应急响应)
- MISP, YARA (威胁情报)
- Wazuh, Lynis (监控加固)

**录制与取证**:
- ffmpeg, OBS (屏幕录制)
- asciinema, ttyrec (终端录制)
- hashdeep, gpg (证据管理)

---

## 14. 运行方式

### 14.1 Agent启动流程

```python
# agent/start.py
def start_agent(user_requirement, config=None):
    """启动AI安全研究员"""
    
    # 1. 加载配置
    config = load_config(config)
    
    # 2. 初始化所有组件
    memory_manager = MemoryManager()
    state_tracker = StateTracker()
    knowledge_graph = ContextGraph()
    task_planner = TaskPlanner(memory_manager, knowledge_graph)
    workflow_engine = WorkflowEngine(state_tracker, memory_manager)
    execution_controller = ExecutionController(workflow_engine, memory_manager, skills_registry)
    quality_checker = QualityControl()
    self_assessment = SelfAssessment(execution_controller.execution_history, memory_manager)
    
    # 3. 初始化Agent核心
    agent = SecurityExpertAgent(
        memory_manager,
        state_tracker,
        task_planner,
        workflow_engine,
        execution_controller,
        quality_checker,
        self_assessment
    )
    
    # 4. 启动合规记录
    agent.start_compliance_recording()
    
    # 5. 配置匿名网络
    agent.setup_anonymity()
    
    # 6. 解析需求并开始工作
    return agent.start_task(user_requirement)
```

### 14.2 完整会话流程

```
1. 会话初始化
   ├── 验证授权
   ├── 配置工作区
   └── 生成会话ID

2. 匿名配置
   ├── 配置Tor/代理
   ├── 修改MAC地址
   └── 验证匿名性

3. 开始录制
   ├── 启动屏幕录制
   ├── 启动终端录制
   ├── 启动网络捕获
   └── 启用审计日志

4. 执行测试
   ├── 执行预定测试用例
   ├── 记录发现和证据
   └── 生成证据哈希

5. 完成测试
   ├── 停止所有录制
   ├── 验证证据完整性
   ├── 创建证据链
   └── 生成测试报告

6. 归档会话
   ├── 加密敏感数据
   ├── 打包所有证据
   └── 数字签名
```

### 14.3 数据流

```
用户请求
  ↓
Agent感知当前状态 (读取 memory/state_tracker)
  ↓
Agent理解上下文 (读取 knowledge graph / target profile)
  ↓
Agent思考决策 (使用 prompts 进行推理)
  ↓
Agent选择Skill
  ↓
Agent执行Skill (使用 ai-agent/skills/)
  ↓
结果写入记忆
  ↓
证据存入 compliance/evidence/
日志写入 compliance/logs/
  ↓
Agent评估结果
  ↓
Agent决定下一步 (回到感知，继续循环...)
```

---

## 15. 配置文件说明

### 15.1 Agent核心配置

```yaml
# config/agent/core.yaml
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
    autonomous: true
    ask_for_confirmation: false
    risk_aversion: "balanced"
    thoroughness: "high"
    explain_decisions: true

memory:
  short_term:
    max_size: 100
    retention_hours: 24
  
  medium_term:
    max_sessions: 10
    retention_days: 30
  
  long_term:
    persistent: true
    learning_enabled: true

workflow:
  auto_adapt: true
  state_review_frequency: "after_each_action"
  fallback_mechanism: true

quality:
  validation_enabled: true
  self_assessment: true
  evidence_requirements: "strict"
```

### 15.2 合规配置

```yaml
# config/compliance/recording.yaml
screen_recording:
  enabled: true
  output_directory: ${COMPLIANCE_PATH}/recordings/screen
  format: mp4
  fps: 30

terminal_recording:
  enabled: true
  output_directory: ${COMPLIANCE_PATH}/recordings/terminal
  format: cast

network_capture:
  enabled: true
  output_directory: ${COMPLIANCE_PATH}/recordings/network
  format: pcap

audit_logging:
  enabled: true
  log_directory: ${COMPLIANCE_PATH}/logs/audit
  include_commands: true
```

### 15.3 代理配置

```yaml
# config/proxy/tor.yml
enabled: true
socks_port: 9050
control_port: 9051
control_password: your_control_password

# config/proxy/proxychains.yml
enabled: true
chain_type: dynamic
proxy_dns: true
proxies:
  - type: socks5
    host: 127.0.0.1
    port: 9050
```

---

## 16. 合规与安全

### 16.1 授权验证流程

```
1. 任务开始前强制检查授权
2. 验证授权范围
3. 确认授权时间有效性
4. 记录授权信息
5. 启动不可篡改的合规记录
6. 全程记录所有操作
7. 证据链完整维护
8. 最终签名与封存
```

### 16.2 操作审计要求

每一个Agent决策和操作都会被记录:
- 决策时间
- 决策原因
- 执行的操作
- 操作结果
- 证据链接
- 时间戳
- 完整的思维链记录

### 16.3 合规检查清单

| 检查项 | 说明 |
|-------|------|
| 授权文件已验证 | 确认有书面授权 |
| 屏幕录制已启动 | 全程录制屏幕 |
| 终端录制已启动 | 记录所有命令 |
| 审计日志已启用 | 记录所有操作 |
| 匿名配置已确认 | 确保身份隐藏 |
| 测试范围已确认 | 不超出授权范围 |
| 证据哈希已生成 | SHA256哈希 |
| 证据链已创建 | 完整记录处理过程 |
| 最终报告已生成 | 专业格式报告 |
| 会话已安全归档 | 加密存储 |

---

## 附录

### A. 参考文档

| 文档 | 说明 |
|------|------|
| [README.md](README.md) | 项目总览 |
| [spec.md](spec.md) | 完整规划文档 |
| [agent-workspace-spec.md](agent-workspace-spec.md) | Agent工作区完整设计 |
| [agent-workspace-structure.md](agent-workspace-structure.md) | 目录结构详解 |
| [state-management-workflow.md](state-management-workflow.md) | 状态管理与工作流 |
| [prompt-engineering-system.md](prompt-engineering-system.md) | 提示工程体系 |
| [checklist.md](checklist.md) | 实施检查清单 |
| [tasks.md](tasks.md) | 实施任务清单 |

### B. 工具清单

详见 [spec.md](spec.md) 第三节：工具清单

### C. 合规标准参考

- OWASP 渗透测试标准
- PTES (渗透测试执行标准)
- NIST SP 800-115
- ISO 27001
- 当地法律法规要求

---

**文档结束**
