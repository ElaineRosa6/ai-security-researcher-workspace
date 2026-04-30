
# 专家级AI安全研究员工作区规划

## 一、系统架构总览

### 核心设计理念
本工作区的设计目标是让AI Agent能够**自主理解、自主规划、自主执行、自主评估**专家级渗透测试和安全研究工作，无需人工干预。

### 系统层次架构

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

## 二、目录架构（AI Agent专用版）

```
pen-test-workspace/
├── README.md
├── .env.example
├── .gitignore
│
├── agent/                                      # AI Agent核心系统
│   ├── brain/                                  # 智能决策中心
│   │   ├── planner.py                          # 任务规划器
│   │   ├── executor.py                         # 执行控制器
│   │   ├── evaluator.py                        # 评估器
│   │   ├── reasoner.py                         # 推理引擎
│   │   └── decision_maker.py                   # 决策器
│   ├── memory/                                 # 记忆系统
│   │   ├── short_term.py                       # 短期记忆
│   │   ├── medium_term.py                      # 中期记忆
│   │   ├── long_term.py                        # 长期记忆
│   │   ├── episodic.py                         # 情景记忆
│   │   ├── semantic.py                         # 语义记忆
│   │   └── memory_manager.py                   # 记忆管理器
│   ├── knowledge/                              # 知识图谱
│   │   ├── vulnerability_db/                   # 漏洞知识库
│   │   ├── attack_patterns/                    # 攻击模式库
│   │   ├── tool_knowledge/                     # 工具知识库
│   │   ├── methodology/                        # 方法论库
│   │   └── context_graph.py                    # 上下文图谱
│   ├── workflow/                               # 智能工作流引擎
│   │   ├── engine.py                           # 工作流引擎
│   │   ├── state_tracker.py                    # 状态追踪器
│   │   ├── transition.py                       # 状态转换器
│   │   └── dynamic_adapter.py                  # 动态适配器
│   ├── quality/                                # 质量控制层
│   │   ├── validator.py                        # 验证器
│   │   ├── checker.py                          # 检查器
│   │   ├── auditor.py                          # 审计器
│   │   └── self_assessment.py                  # 自我评估
│   └── prompts/                                # 提示工程体系
│       ├── system_prompts/                     # 系统提示词
│       ├── task_prompts/                       # 任务提示词
│       ├── tool_prompts/                       # 工具提示词
│       ├── reasoning_prompts/                  # 推理提示词
│       └── chain_of_thought/                   # 思维链提示
│
├── red-team/                                   # 红队攻击场景
│   ├── web-security/                          # Web安全
│   ├── binary-security/                       # 二进制安全
│   ├── mobile-app/                            # 移动应用安全
│   ├── miniprogram/                           # 微信小程序安全
│   ├── domain-pentest/                        # 域渗透
│   ├── phishing/                              # 钓鱼
│   ├── anonymity/                             # 匿名与代理
│   └── infrastructure/                        # 基础设施攻击
│
├── blue-team/                                  # 蓝队防御场景
│   ├── incident-response/                     # 应急响应
│   ├── threat-intel/                          # 威胁情报
│   ├── monitoring/                            # 监控
│   └── hardening/                             # 加固
│
├── purple-team/                                # 紫队协作场景
│   ├── attack-simulation/                     # 攻击模拟
│   ├── defense-validation/                    # 防御验证
│   ├── forensics/                             # 溯源取证
│   └── training/                              # 训练
│
├── compliance/                                 # 合规与记录
│   ├── recordings/                            # 录屏文件
│   ├── logs/                                  # 操作日志
│   ├── evidence/                              # 证据管理
│   ├── policies/                              # 合规策略
│   └── checklists/                            # 合规检查清单
│
├── shared/                                     # 共享资源
│   ├── tools/                                 # 通用工具
│   ├── wordlists/                             # 字典
│   ├── templates/                             # 模板
│   ├── datasets/                              # 数据集
│   └── documentation/                         # 文档
│
├── ai-agent/                                   # Skills和Harness
│   ├── skills/                                # Skills模块
│   ├── harness/                               # Harness框架
│   ├── prompts/                               # 提示词
│   └── workflows/                             # 工作流定义
│
├── workspace-data/                             # 工作区数据
│   ├── current-session/                       # 当前会话数据
│   │   ├── state.json                         # 当前状态
│   │   ├── context.json                       # 上下文数据
│   │   ├── memory.json                        # 记忆快照
│   │   └── execution.log                      # 执行日志
│   ├── sessions-history/                      # 历史会话
│   └── knowledge-base/                        # 知识库
│
├── config/                                     # 配置文件
│   ├── agent/                                 # Agent配置
│   ├── tools/                                 # 工具配置
│   ├── environment/                           # 环境配置
│   ├── proxy/                                 # 代理配置
│   ├── compliance/                            # 合规配置
│   └── profiles/                              # 配置文件
│
└── output/                                     # 输出目录
    ├── reports/                               # 报告
    ├── logs/                                  # 日志
    ├── artifacts/                             # 工件
    └── screenshots/                           # 截图
```

## 三、记忆系统设计 (Memory System)

### 3.1 记忆层次结构

#### 短期记忆 (Short-Term Memory)
```python
{
    "session_id": "uuid",
    "timestamp": "iso8601",
    "current_task": "任务描述",
    "current_step": "当前步骤",
    "recent_actions": [
        {
            "action_id": "uuid",
            "action_type": "技能调用/工具执行/决策",
            "content": "操作内容",
            "result": "操作结果",
            "timestamp": "iso8601"
        }
    ],
    "active_context": {
        "target_info": "目标信息",
        "current_focus": "当前焦点",
        "open_questions": [],
        "pending_tasks": []
    },
    "working_memory": "临时工作数据"
}
```

#### 中期记忆 (Medium-Term Memory)
```python
{
    "session_id": "uuid",
    "discoveries": [
        {
            "discovery_id": "uuid",
            "type": "漏洞/信息/凭证",
            "content": "发现内容",
            "evidence": "证据链接",
            "confidence": 0.9,
            "timestamp": "iso8601"
        }
    ],
    "attack_history": [],
    "target_profile": {
        "services": [],
        "technologies": [],
        "vulnerabilities": [],
        "credentials": []
    },
    "decision_history": [],
    "failure_analysis": []
}
```

#### 长期记忆 (Long-Term Memory)
```python
{
    "knowledge_base": {
        "vulnerabilities": {},
        "techniques": {},
        "tools": {},
        "methodologies": {}
    },
    "pattern_recognition": {
        "common_attack_paths": [],
        "typical_configurations": [],
        "vulnerability_patterns": []
    },
    "experience": {
        "successful_attacks": [],
        "failed_attempts": [],
        "lessons_learned": []
    },
    "best_practices": []
}
```

#### 情景记忆 (Episodic Memory)
```python
{
    "episodes": [
        {
            "episode_id": "uuid",
            "type": "侦察/扫描/漏洞利用/后渗透",
            "description": "情景描述",
            "context": "上下文信息",
            "actions": [],
            "outcomes": [],
            "timestamp": "iso8601",
            "related_episodes": []
        }
    ],
    "episode_timeline": []
}
```

#### 语义记忆 (Semantic Memory)
```python
{
    "concepts": {},
    "relationships": {},
    "categories": {},
    "taxonomy": {},
    "domain_knowledge": {}
}
```

### 3.2 记忆管理器 (Memory Manager)

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
        pass
    
    def retrieve(self, query, memory_type=None):
        """根据查询检索记忆"""
        pass
    
    def update(self, data_id, updates, memory_type):
        """更新记忆数据"""
        pass
    
    def consolidate(self):
        """记忆整合 - 将短期记忆合并到中期/长期记忆"""
        pass
    
    def forget(self, criteria):
        """选择性遗忘"""
        pass
    
    def get_context(self):
        """获取当前上下文"""
        pass
```

## 四、智能工作流引擎设计

### 4.1 状态定义与状态图

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

异常状态：
┌─────────────────┐
│   PAUSED        │  暂停
└─────────────────┘
┌─────────────────┐
│   BLOCKED       │  阻塞
└─────────────────┘
┌─────────────────┐
│   ERROR         │  错误
└─────────────────┘
```

### 4.2 状态追踪器 (State Tracker)

```python
class StateTracker:
    def __init__(self):
        self.current_state = "INITIALIZED"
        self.state_history = []
        self.state_context = {}
        self.state_metadata = {}
    
    def get_current_state(self):
        """获取当前状态"""
        return self.current_state
    
    def transition_to(self, new_state, reason=None):
        """状态转换"""
        self.state_history.append({
            "from": self.current_state,
            "to": new_state,
            "reason": reason,
            "timestamp": datetime.now().isoformat()
        })
        self.current_state = new_state
    
    def update_context(self, key, value):
        """更新状态上下文"""
        self.state_context[key] = value
    
    def get_context(self, key=None):
        """获取状态上下文"""
        if key:
            return self.state_context.get(key)
        return self.state_context
    
    def should_continue(self):
        """判断是否应该继续执行"""
        pass
    
    def is_state_completed(self, state):
        """判断状态是否已完成"""
        pass
```

### 4.3 工作流引擎 (Workflow Engine)

```python
class WorkflowEngine:
    def __init__(self, state_tracker, memory_manager):
        self.state_tracker = state_tracker
        self.memory_manager = memory_manager
        self.transition_rules = self.load_transition_rules()
        self.dynamic_adapters = []
    
    def execute_workflow(self, task_definition):
        """执行工作流"""
        while not self.is_workflow_completed():
            current_state = self.state_tracker.get_current_state()
            
            # 1. 检查是否可以继续
            if not self.state_tracker.should_continue():
                self.handle_pause_or_block()
                continue
            
            # 2. 执行当前状态的动作
            self.execute_state_actions(current_state)
            
            # 3. 判断下一步状态
            next_state = self.decide_next_state()
            
            # 4. 执行状态转换
            self.state_tracker.transition_to(next_state)
            
            # 5. 更新记忆
            self.update_memory_with_state_transition()
    
    def execute_state_actions(self, state):
        """执行状态对应的动作"""
        actions = self.get_actions_for_state(state)
        for action in actions:
            self.execute_action(action)
    
    def decide_next_state(self):
        """智能决定下一个状态"""
        # 基于：
        # 1. 当前状态
        # 2. 已完成的任务
        # 3. 发现的新信息
        # 4. 剩余任务
        # 5. 风险评估
        pass
    
    def load_transition_rules(self):
        """加载状态转换规则"""
        return {
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
    
    def register_dynamic_adapter(self, adapter):
        """注册动态适配器"""
        self.dynamic_adapters.append(adapter)
```

## 五、任务规划与执行框架

### 5.1 任务规划器 (Task Planner)

```python
class TaskPlanner:
    def __init__(self, memory_manager, knowledge_graph):
        self.memory_manager = memory_manager
        self.knowledge_graph = knowledge_graph
    
    def parse_requirement(self, requirement_text):
        """解析用户需求"""
        return {
            "task_type": "渗透测试/安全研究/应急响应",
            "target": "目标描述",
            "scope": "范围定义",
            "constraints": "约束条件",
            "objectives": "目标列表",
            "deliverables": "交付物"
        }
    
    def create_task_plan(self, requirement):
        """创建任务计划"""
        plan = {
            "phases": [
                {
                    "phase_name": "侦察",
                    "tasks": [],
                    "dependencies": [],
                    "estimated_effort": 0
                },
                {
                    "phase_name": "扫描",
                    "tasks": [],
                    "dependencies": ["侦察"],
                    "estimated_effort": 0
                }
                # ... 更多阶段
            ],
            "task_graph": "有向无环图",
            "resource_allocation": {},
            "timeline": {},
            "risk_assessment": {}
        }
        return plan
    
    def refine_plan(self, current_plan, new_information):
        """基于新信息细化计划"""
        pass
    
    def identify_missing_information(self, plan):
        """识别缺少的信息"""
        pass
    
    def prioritize_tasks(self, tasks):
        """任务优先级排序"""
        pass
```

### 5.2 执行控制器 (Execution Controller)

```python
class ExecutionController:
    def __init__(self, workflow_engine, memory_manager, skills_registry):
        self.workflow_engine = workflow_engine
        self.memory_manager = memory_manager
        self.skills_registry = skills_registry
        self.execution_history = []
    
    def execute_task(self, task):
        """执行单个任务"""
        execution_record = {
            "task_id": task.get("id"),
            "task_name": task.get("name"),
            "start_time": datetime.now().isoformat(),
            "status": "IN_PROGRESS",
            "actions": []
        }
        
        try:
            # 1. 选择合适的Skill
            skill = self.select_appropriate_skill(task)
            
            # 2. 准备执行上下文
            context = self.prepare_execution_context(task)
            
            # 3. 执行Skill
            result = skill.execute(context)
            
            # 4. 处理结果
            self.process_execution_result(result, execution_record)
            
            execution_record["status"] = "COMPLETED"
            
        except Exception as e:
            execution_record["status"] = "FAILED"
            execution_record["error"] = str(e)
            self.handle_execution_failure(execution_record)
        
        execution_record["end_time"] = datetime.now().isoformat()
        self.execution_history.append(execution_record)
        
        return execution_record
    
    def select_appropriate_skill(self, task):
        """选择合适的Skill"""
        pass
    
    def prepare_execution_context(self, task):
        """准备执行上下文"""
        pass
    
    def process_execution_result(self, result, execution_record):
        """处理执行结果"""
        pass
    
    def handle_execution_failure(self, execution_record):
        """处理执行失败"""
        # 1. 记录失败
        # 2. 分析失败原因
        # 3. 尝试恢复/重试
        # 4. 调整计划
        pass
    
    def execute_next_task(self, plan):
        """执行下一个任务"""
        pass
```

## 六、知识图谱与上下文管理

### 6.1 上下文图谱 (Context Graph)

```python
class ContextGraph:
    def __init__(self):
        self.graph = {
            "nodes": [],
            "edges": []
        }
    
    def add_node(self, node_id, node_type, properties):
        """添加节点"""
        self.graph["nodes"].append({
            "id": node_id,
            "type": node_type,
            "properties": properties
        })
    
    def add_edge(self, from_node, to_node, relation_type, properties=None):
        """添加边"""
        self.graph["edges"].append({
            "from": from_node,
            "to": to_node,
            "type": relation_type,
            "properties": properties or {}
        })
    
    def query(self, query_pattern):
        """查询图谱"""
        pass
    
    def find_path(self, start_node, end_node):
        """查找节点间路径"""
        pass
    
    def get_subgraph(self, center_node, radius=2):
        """获取子图"""
        pass
    
    def get_target_profile(self, target_id):
        """获取目标画像"""
        pass
```

### 6.2 目标画像示例

```json
{
    "target_id": "example.com",
    "profile": {
        "basic_info": {
            "domain": "example.com",
            "ips": ["192.168.1.1"],
            "organization": "Example Corp"
        },
        "services": [
            {
                "port": 80,
                "service": "HTTP",
                "banner": "nginx/1.20.1",
                "technology": "WordPress 5.7"
            }
        ],
        "technologies": [
            {
                "name": "WordPress",
                "version": "5.7",
                "confidence": 0.95
            }
        ],
        "vulnerabilities": [
            {
                "id": "CVE-2021-xxxx",
                "description": "SQL注入漏洞",
                "severity": "CRITICAL",
                "exploitable": true
            }
        ],
        "attack_surface": {
            "attack_paths": [],
            "entry_points": [],
            "critical_assets": []
        }
    }
}
```

## 七、质量控制与自我评估系统

### 7.1 验证器 (Validator)

```python
class Validator:
    def validate_result(self, result, expected_criteria):
        """验证结果"""
        validation_result = {
            "is_valid": True,
            "issues": [],
            "quality_score": 0,
            "confidence": 0
        }
        
        # 1. 完整性检查
        completeness_score = self.check_completeness(result)
        
        # 2. 准确性检查
        accuracy_score = self.check_accuracy(result)
        
        # 3. 一致性检查
        consistency_score = self.check_consistency(result)
        
        # 4. 计算综合质量分数
        validation_result["quality_score"] = self.calculate_overall_score(
            completeness_score, accuracy_score, consistency_score
        )
        
        return validation_result
    
    def check_completeness(self, result):
        """检查完整性"""
        pass
    
    def check_accuracy(self, result):
        """检查准确性"""
        pass
    
    def check_consistency(self, result):
        """检查一致性"""
        pass
```

### 7.2 自我评估系统 (Self-Assessment)

```python
class SelfAssessment:
    def __init__(self, execution_history, memory_manager):
        self.execution_history = execution_history
        self.memory_manager = memory_manager
    
    def assess_performance(self):
        """评估性能"""
        assessment = {
            "overall_score": 0,
            "strengths": [],
            "weaknesses": [],
            "recommendations": [],
            "lessons_learned": []
        }
        
        # 1. 评估任务完成率
        completion_rate = self.calculate_completion_rate()
        
        # 2. 评估结果质量
        quality_score = self.assess_result_quality()
        
        # 3. 评估效率
        efficiency_score = self.assess_efficiency()
        
        # 4. 评估决策质量
        decision_quality = self.assess_decision_quality()
        
        # 5. 生成改进建议
        assessment["recommendations"] = self.generate_improvements()
        
        return assessment
    
    def calculate_completion_rate(self):
        """计算完成率"""
        pass
    
    def assess_result_quality(self):
        """评估结果质量"""
        pass
    
    def assess_efficiency(self):
        """评估效率"""
        pass
    
    def assess_decision_quality(self):
        """评估决策质量"""
        pass
    
    def generate_improvements(self):
        """生成改进建议"""
        pass
```

## 八、提示工程体系

### 8.1 系统提示词 (System Prompts)

#### Agent角色定义
```
你是一位专家级渗透测试师和安全研究员，拥有以下专业能力：

【核心能力】
- 精通各类漏洞识别与利用技术
- 熟悉红队/蓝队/紫队全流程
- 具备高级恶意代码分析能力
- 擅长移动应用和微信小程序安全
- 精通域渗透和复杂网络环境
- 具备专业的应急响应和溯源能力
- 深厚的理论基础和实践经验

【工作原则】
1. 严格遵守授权范围和法律法规
2. 全程保持合规记录与证据链完整
3. 系统化的方法论驱动工作
4. 持续自我评估与优化
5. 全面的风险评估与控制

【思考方式】
- 使用思维链(Chain of Thought)逐步推理
- 持续回顾与反思工作进展
- 主动识别信息缺口
- 基于证据做出决策
- 考虑多种可能性并评估风险

【输出格式】
- 清晰的结构化输出
- 明确标注思考过程和决策依据
- 完整记录发现的漏洞与证据
- 可执行的后续建议
```

### 8.2 任务提示词模板

#### 需求解析提示词
```
【任务】解析安全测试需求

【当前状态】{state_description}

【用户需求】
{user_requirement}

【请回答】
1. 首先理解用户的真实需求是什么？
2. 这是什么类型的任务？(渗透测试/安全研究/应急响应/...)
3. 任务的目标是什么？
4. 任务的范围和边界是什么？
5. 有什么约束条件？
6. 应该使用什么方法论？
7. 识别任何不明确的地方，列出需要澄清的问题

【思考过程】
请使用思维链方式展示你的思考
```

#### 规划提示词
```
【任务】制定测试计划

【已知信息】
{target_profile}
{discoveries}
{constraints}

【请回答】
1. 基于当前信息，应该分几个阶段进行？
2. 每个阶段的具体任务是什么？
3. 任务之间的依赖关系如何？
4. 推荐使用哪些工具和技术？
5. 可能的风险点有哪些？
6. 需要什么额外信息？

【输出格式】
- 阶段列表
- 任务列表
- 优先级排序
- 资源需求
- 风险评估
```

#### 执行提示词
```
【任务】执行当前步骤

【当前状态】{current_state}
【当前任务】{current_task}
【已知信息】{context_info}
【可用工具】{tools_list}
【记忆回顾】{memory_summary}

【请回答】
1. 当前任务的目标是什么？
2. 应该使用什么方法/工具？
3. 具体如何执行？
4. 需要注意什么？
5. 预期结果是什么？
6. 如果成功，下一步是什么？
7. 如果失败，备选方案是什么？

【执行决策】
请明确选择执行方案并说明理由
```

#### 评估提示词
```
【任务】评估执行结果

【执行记录】{execution_record}
【结果数据】{result_data}

【请回答】
1. 结果是否符合预期？
2. 结果的质量如何？(准确/完整/可靠)
3. 有什么重要发现？
4. 发现是否有足够证据支持？
5. 需要进一步验证吗？
6. 对任务目标有什么影响？
7. 下一步应该如何决策？

【质量评估】
- 完整性: 高/中/低
- 准确性: 高/中/低
- 置信度: 0-1
- 建议:
```

### 8.3 工具使用提示词

```
【工具】{tool_name}

【功能描述】{tool_description}

【使用场景】
- {scenario_1}
- {scenario_2}

【参数说明】
- {param_1}: {description}
- {param_2}: {description}

【示例用法】
{examples}

【注意事项】
- {note_1}
- {note_2}

【当前任务】{task_description}
【请判断】这个工具是否适合当前任务？如果适合，应该如何使用？
```

## 九、Agent引导系统 (Agent Guidance)

### 9.1 状态感知与自我认知

```python
class AgentAwareness:
    def __init__(self, state_tracker, memory_manager):
        self.state_tracker = state_tracker
        self.memory_manager = memory_manager
    
    def get_self_status(self):
        """获取自身状态"""
        return {
            "current_state": self.state_tracker.get_current_state(),
            "context": self.state_tracker.get_context(),
            "memory_snapshot": self.memory_manager.get_summary(),
            "capabilities": self.get_capabilities(),
            "current_focus": self.get_current_focus(),
            "open_tasks": self.get_open_tasks(),
            "missing_info": self.identify_missing_info()
        }
    
    def get_capabilities(self):
        """获取当前可用能力"""
        pass
    
    def get_current_focus(self):
        """获取当前焦点"""
        pass
    
    def get_open_tasks(self):
        """获取待办任务"""
        pass
    
    def identify_missing_info(self):
        """识别缺失的信息"""
        pass
    
    def should_ask_for_clarification(self):
        """判断是否需要向用户澄清"""
        pass
```

### 9.2 动态决策引导

```python
class DecisionGuide:
    def __init__(self, knowledge_base, pattern_recognizer):
        self.knowledge_base = knowledge_base
        self.pattern_recognizer = pattern_recognizer
    
    def generate_options(self, context):
        """生成选项列表"""
        options = []
        
        # 1. 基于知识生成标准选项
        standard_options = self.get_standard_options(context)
        
        # 2. 基于模式识别生成创新选项
        innovative_options = self.generate_innovative_options(context)
        
        # 3. 基于风险生成备选方案
        fallback_options = self.generate_fallback_options(context)
        
        options = standard_options + innovative_options + fallback_options
        
        return options
    
    def evaluate_options(self, options, criteria):
        """评估选项"""
        evaluations = []
        for option in options:
            evaluation = {
                "option": option,
                "score": self.calculate_score(option, criteria),
                "risks": self.identify_risks(option),
                "benefits": self.identify_benefits(option),
                "feasibility": self.assess_feasibility(option)
            }
            evaluations.append(evaluation)
        
        return sorted(evaluations, key=lambda x: x["score"], reverse=True)
    
    def make_recommendation(self, evaluations):
        """做出推荐"""
        pass
```

## 十、元系统 (Meta System)

### 10.1 自我监控与日志

```python
class MetaSystem:
    def __init__(self):
        self.agent_telemetry = []
        self.performance_metrics = {}
        self.improvement_suggestions = []
    
    def monitor_agent(self):
        """监控Agent运行状态"""
        pass
    
    def collect_metrics(self):
        """收集性能指标"""
        metrics = {
            "task_completion_rate": 0,
            "average_task_time": 0,
            "success_rate": 0,
            "self_correction_count": 0,
            "knowledge_application_rate": 0,
            "decision_quality_score": 0
        }
        return metrics
    
    def identify_improvements(self):
        """识别改进点"""
        pass
    
    def update_best_practices(self):
        """更新最佳实践"""
        pass
    
    def learn_from_failure(self, failure_record):
        """从失败中学习"""
        pass
    
    def learn_from_success(self, success_record):
        """从成功中学习"""
        pass
```

## 十一、核心工作流示例（完整会话）

### 阶段1: 初始化与需求解析

```
用户请求: "帮我对example.com做一次完整的渗透测试"

Agent处理流程:
1. 验证授权与合规
2. 解析需求 → 确定为Web应用渗透测试
3. 初始化记忆系统
4. 启动合规记录(屏幕录制、终端录制)
5. 配置匿名网络
6. 进入REQUIREMENT_ANALYSIS状态
```

### 阶段2: 任务规划

```
Agent规划:
1. 从知识库加载Web渗透测试方法论
2. 制定多阶段计划:
   - 侦察阶段(信息收集)
   - 扫描阶段(端口扫描、服务识别)
   - 漏洞评估
   - 漏洞利用
   - 后渗透
   - 报告生成
3. 识别所需信息缺口
4. 创建任务依赖图
5. 进入PLANNING状态 → RECON状态
```

### 阶段3: 侦察执行

```
执行步骤:
1. 使用WebSecuritySkill进行DNS枚举
2. 使用OSINT工具收集信息
3. 发现子域名: www, api, admin
4. 构建目标画像
5. 更新记忆系统
6. 发现: 有WordPress站点在5.7版本
7. 进入SCANNING状态
```

### 阶段4: 智能状态调整

```
Agent决策:
- 基于侦察发现，WordPress 5.7可能有已知漏洞
- 决定跳过全面扫描，先进行定向漏洞检查
- 使用VULN_ASSESS阶段专门检查WordPress漏洞
- 这是一个动态决策！
```

### 阶段5: 漏洞评估与利用

```
发现CVE-2021-xxxx SQL注入:
1. 验证漏洞存在
2. 评估可利用性
3. 准备EXPLOITATION阶段
4. 使用适当的Exploit
5. 获取访问权限
6. 完整记录证据链
```

### 阶段6: 后渗透与报告

```
执行后渗透:
1. 权限提升尝试
2. 横向移动
3. 数据收集
4. 生成专业报告
5. 完成合规归档
6. 自我评估与改进
```

## 十二、配置文件示例

### Agent核心配置

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
  compliance_checks: true
```

### 记忆系统配置

```yaml
# config/agent/memory.yaml
memory_layers:
  short_term:
    storage: "in_memory"
    capacity: "1000_items"
    items:
      - "recent_actions"
      - "active_context"
      - "working_memory"
  
  medium_term:
    storage: "session_db"
    capacity: "per_session"
    items:
      - "discoveries"
      - "target_profile"
      - "attack_history"
      - "decision_history"
  
  long_term:
    storage: "knowledge_db"
    persistent: true
    items:
      - "vulnerability_db"
      - "techniques"
      - "tool_knowledge"
      - "best_practices"
      - "experience"
  
  episodic:
    storage: "episode_db"
    items:
      - "attack_episodes"
      - "investigation_episodes"
      - "learning_episodes"
```

## 十三、启动与初始化流程

### Agent启动脚本

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

## 十四、Agent与工作区交互协议

### 状态查询API

```python
# Agent可以随时查询工作区状态
workspace.get_current_state()
workspace.get_current_task()
workspace.get_memory_summary()
workspace.get_target_profile()
workspace.get_discoveries()
workspace.get_open_tasks()
workspace.get_next_actions()
workspace.get_available_tools()
```

### 决策与执行API

```python
# Agent可以执行的操作
workspace.select_skill(skill_name)
workspace.execute_skill(skill, params)
workspace.make_decision(decision, reasoning)
workspace.store_in_memory(data, memory_type)
workspace.transition_to_new_state(new_state)
workspace.record_discovery(discovery)
workspace.ask_user_clarification(question)
workspace.pause_execution(reason)
workspace.resume_execution()
```

## 十五、安全与合规

### 授权检查流程

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

### 操作审计

```
每一个Agent决策和操作都会被记录:
- 决策时间
- 决策原因
- 执行的操作
- 操作结果
- 证据链接
- 时间戳
- 完整的思维链记录
```

---

**本工作区的设计目标：让AI Agent能够像人类专家一样思考、规划、执行、评估安全工作！**
