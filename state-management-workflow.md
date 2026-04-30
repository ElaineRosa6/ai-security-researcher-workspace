
# AI Agent状态管理与工作流系统

## 一、Agent认知循环

### 1.1 感知-思考-决策-行动循环 (PTDA Loop)

```
┌─────────────────────────────────────────────────────────────────┐
│  1. PERCEIVE (感知)                                             │
│  - 获取当前状态                                                 │
│  - 读取记忆系统                                                 │
│  - 查询知识图谱                                                 │
│  - 分析环境信息                                                 │
└────────────────────┬────────────────────────────────────────────┘
                     ↓
┌─────────────────────────────────────────────────────────────────┐
│  2. THINK (思考)                                                 │
│  - 理解当前局面                                                 │
│  - 识别问题与机会                                               │
│  - 生成多种选项                                                 │
│  - 评估选项风险                                                 │
└────────────────────┬────────────────────────────────────────────┘
                     ↓
┌─────────────────────────────────────────────────────────────────┐
│  3. DECIDE (决策)                                                │
│  - 选择最佳选项                                                 │
│  - 确认决策理由                                                 │
│  - 检查合规与授权                                               │
│  - 制定执行计划                                                 │
└────────────────────┬────────────────────────────────────────────┘
                     ↓
┌─────────────────────────────────────────────────────────────────┐
│  4. ACT (行动)                                                   │
│  - 执行选择的Skill/Harness                                      │
│  - 操作工具                                                     │
│  - 收集结果                                                     │
│  - 记录证据                                                     │
└────────────────────┬────────────────────────────────────────────┘
                     ↓
┌─────────────────────────────────────────────────────────────────┐
│  5. REFLECT (反思)                                               │
│  - 评估执行结果                                                 │
│  - 更新记忆系统                                                 │
│  - 学习经验教训                                                 │
│  - 调整下一步计划                                               │
└─────────────────────────────────────────────────────────────────┘
                     ↓ (回到 PERCEIVE，继续循环)
```

### 1.2 完整认知循环示例

让我通过一个具体场景来展示这个循环：

#### 场景：Agent正在进行Web渗透测试，刚刚完成了端口扫描

```
【PERCEIVE 感知】
→ 读取状态: 当前处于 SCANNING 阶段
→ 读取记忆: 已经发现了80、443端口
→ 读取知识: 80端口是HTTP，可能有Web应用
→ 分析环境: 目标服务器运行着 nginx

【THINK 思考】
→ 理解: 有Web应用在80端口
→ 识别: 应该进行Web应用扫描
→ 生成: 选项1 - 目录扫描；选项2 - CMS识别；选项3 - 漏洞扫描
→ 评估: 选项2先，先识别CMS版本，更有针对性

【DECIDE 决策】
→ 选择: 先识别CMS
→ 理由: 知道CMS后更有针对性
→ 检查: 在授权范围内
→ 计划: 使用WebSecuritySkill的cms_detection功能

【ACT 行动】
→ 执行: 调用WebSecuritySkill.cms_detection(target)
→ 操作: 运行指纹识别
→ 收集: 发现是 WordPress 5.7
→ 记录: 保存为discovery

【REFLECT 反思】
→ 评估: 成功识别CMS！
→ 更新: 记忆中添加WordPress信息
→ 学习: WordPress 5.7可能有CVE-2021-xxxx
→ 调整: 下一步应该直接检查这个漏洞！

→ 回到 PERCEIVE，开始下一轮循环...
```

## 二、状态上下文完整定义

### 2.1 当前状态查询模板

Agent每次醒来都会问自己："我现在在什么状态？"

```python
# Agent自我认知查询
current_situation = {
    "who_am_i": "专家级安全研究员Agent",
    "where_am_i": {
        "workflow_state": "SCANNING",  # 当前工作流状态
        "phase": "侦察与发现",         # 当前阶段
        "step": "Web服务识别",          # 当前步骤
        "target": "example.com"         # 当前目标
    },
    "what_have_i_done": [              # 已完成的事情
        {"id": "task_1", "name": "DNS枚举", "result": "发现3个子域名"},
        {"id": "task_2", "name": "端口扫描", "result": "发现80,443端口"}
    ],
    "what_do_i_know": {               # 已知信息
        "target_profile": {...},
        "discoveries": [...],
        "vulnerabilities": [...]
    },
    "what_do_i_not_know": [           # 不知道的信息
        "Web应用具体是什么？",
        "有什么漏洞？"
    ],
    "what_am_i_trying_to_do": {       # 目标
        "primary_goal": "完成渗透测试",
        "immediate_objective": "识别Web应用并寻找漏洞"
    },
    "what_are_my_options": [          # 可选的行动
        {"option": "目录扫描", "relevance": "high"},
        {"option": "CMS识别", "relevance": "high"}
    ],
    "what_should_i_do_next": "DECIDE" # 下一步行动
}
```

### 2.2 每个状态的完整上下文数据

#### 状态: INITIALIZED (初始化)
```
上下文:
{
    "status": "准备就绪",
    "description": "Agent已启动，等待任务",
    "pending_actions": [
        "等待用户输入",
        "验证授权"
    ],
    "required_inputs": [
        "任务描述",
        "授权文件"
    ]
}
```

#### 状态: REQUIREMENT_ANALYSIS (需求解析)
```
上下文:
{
    "status": "解析需求中",
    "user_input": "用户原始请求",
    "parsed_requirement": {
        "task_type": "渗透测试/安全研究/应急响应",
        "target": "目标描述",
        "scope": "范围",
        "constraints": [],
        "objectives": []
    },
    "ambiguities": [  # 不明确的地方
        "用户是否需要完整报告？",
        "范围包括内部网络吗？"
    ],
    "decisions": [
        "需要澄清的问题列表"
    ]
}
```

#### 状态: PLANNING (规划中)
```
上下文:
{
    "status": "制定计划",
    "information_gathered": {...},  # 已收集信息
    "missing_information": [],       # 缺失信息
    "draft_plan": {                  # 计划草案
        "phases": [],
        "tasks": [],
        "timeline": {}
    },
    "options_considered": [],        # 考虑过的选项
    "final_plan": null,              # 最终计划
    "plan_rating": 0                 # 计划评分
}
```

#### 状态: RECON (侦察)
```
上下文:
{
    "status": "信息收集中",
    "recon_type": "主动/被动",
    "target_profile_building": {
        "completeness": 0.3,  # 画像完成度30%
        "next_steps": ["DNS枚举", "WHOIS查询"]
    },
    "discoveries_so_far": [],
    "next_recon_tasks": []
}
```

#### 状态: SCANNING (扫描)
```
上下文:
{
    "status": "扫描进行中",
    "scan_type": "端口扫描/服务扫描/漏洞扫描",
    "scan_progress": {
        "total": 1000,
        "completed": 350,
        "percentage": 35
    },
    "services_found": [],
    "interesting_findings": []
}
```

#### 状态: VULN_ASSESS (漏洞评估)
```
上下文:
{
    "status": "漏洞评估中",
    "potential_vulnerabilities": [
        {
            "description": "可能的SQL注入",
            "confidence": 0.7,
            "needs_verification": true
        }
    ],
    "verified_vulnerabilities": [],
    "next_to_verify": []
}
```

#### 状态: EXPLOITATION (漏洞利用)
```
上下文:
{
    "status": "漏洞利用中",
    "target_vulnerability": "CVE-2021-xxxx",
    "exploit_options": [],
    "selected_exploit": null,
    "exploitation_attempts": [],
    "access_gained": false,
    "access_level": null  # "none"/"user"/"admin"/"system"
}
```

#### 状态: POST_EXPLOIT (后渗透)
```
上下文:
{
    "status": "后渗透中",
    "current_access": {
        "machine": "server1",
        "user": "www-data",
        "privilege": "user"
    },
    "objectives": [
        "权限提升",
        "横向移动",
        "数据收集"
    ],
    "post_exploit_actions": [],
    "sensitive_data_found": []
}
```

#### 状态: REPORTING (报告中)
```
上下文:
{
    "status": "生成报告",
    "findings_compiled": [],
    "report_sections": {
        "executive_summary": false,
        "technical_details": false,
        "recommendations": false,
        "appendices": false
    },
    "report_draft": null,
    "review_needed": true
}
```

#### 状态: COMPLETED (完成)
```
上下文:
{
    "status": "任务完成",
    "summary": "任务总结",
    "deliverables": [],
    "lessons_learned": [],
    "self_assessment": {},
    "archive_status": "pending"
}
```

## 三、智能状态转换系统

### 3.1 转换决策引擎

Agent不会盲目按顺序走，它会根据情况智能决定下一步！

```python
class SmartTransitionEngine:
    def decide_next_state(self, current_context):
        """智能决定下一个状态"""
        
        current_state = current_context["state"]
        
        # 获取当前情况的所有信息
        discoveries = current_context["discoveries"]
        remaining_tasks = current_context["remaining_tasks"]
        time_available = current_context["time_available"]
        priority_level = current_context["priority"]
        
        # 场景1: 在SCANNING状态发现了特定漏洞
        if current_state == "SCANNING":
            if self.found_high_value_vulnerability(discoveries):
                # 直接跳转到VULN_ASSESS，跳过继续扫描
                return "VULN_ASSESS"
        
        # 场景2: 在VULN_ASSESS发现需要更多信息
        if current_state == "VULN_ASSESS":
            if self.missing_critical_information(discoveries):
                # 回到RECON补信息
                return "RECON"
        
        # 场景3: 在POST_EXPLOIT发现新的高价值目标
        if current_state == "POST_EXPLOIT":
            if self.found_critical_asset(discoveries):
                # 可以继续深入，或者进入REPORTING
                return self.decide_between_options()
        
        # 默认: 使用标准转换规则
        return self.get_standard_transition(current_state)
```

### 3.2 实际转换示例

#### 示例1: 发现高危漏洞，跳过常规流程

```
原计划路径:
  RECON → SCANNING → VULN_ASSESS (全面评估) → ...

实际发生:
  1. SCANNING阶段
  2. 发现: WordPress 5.7 - 已知有CVE-2021-xxxx (高危！)
  
Agent智能决策:
  "既然发现了确定的高危漏洞，我应该直接去评估和利用这个！"
  "不需要继续全面扫描了，先搞定这个！"

实际路径:
  RECON → SCANNING → VULN_ASSESS (定向评估WordPress) → EXPLOITATION → ...
```

#### 示例2: 信息不足，回退

```
当前状态: VULN_ASSESS
发现: 可能有SQL注入，但证据不够充分

Agent决策:
  "我需要更多信息来确认这个漏洞。"
  "应该回到RECON，再收集一些数据。"

状态转换:
  VULN_ASSESS → RECON (补充信息) → VULN_ASSESS → ...
```

#### 示例3: 多条路径并行评估

```
Agent发现了:
- 漏洞A: Web应用SQL注入 (中危)
- 漏洞B: 开放的SMB服务 (高危)

Agent思考:
  "我可以先做哪个？"
  "漏洞B可能更快获得权限..."
  "或者两个并行评估？"

智能决策:
  1. 先评估漏洞B (SMB) - 可能更有价值
  2. 同时，也别放过漏洞A - 记录下来之后处理

状态: VULN_ASSESS (优先级调整)
```

## 四、记忆系统工作原理

### 4.1 Agent如何记住事情

```python
# 每次执行完动作，Agent都会做记忆更新

def update_memory_after_action(action, result):
    """执行动作后更新记忆"""
    
    # 1. 短期记忆: 刚刚发生的
    short_term.add({
        "action": action,
        "result": result,
        "timestamp": now()
    })
    
    # 2. 中期记忆: 有价值的发现
    if is_important_discovery(result):
        medium_term.add_discovery(result)
    
    # 3. 更新目标画像
    update_target_profile(result)
    
    # 4. 如果是重要经验，加入长期记忆
    if is_learning_experience(result):
        long_term.add_experience(result)
    
    # 5. 情景记忆: 记录整个情景
    episodic.record_episode(
        context_before=get_context(),
        action=action,
        result=result,
        context_after=get_new_context()
    )
```

### 4.2 记忆检索示例

当Agent需要决策时，它会回忆过去的经验！

```python
def retrieve_relevant_memories(current_situation):
    """检索相关记忆"""
    
    memories = {
        "similar_tasks": long_term.find_similar_tasks(current_situation),
        "same_target": medium_term.get_target_history(),
        "past_successes": episodic.find_successful_episodes(),
        "past_failures": episodic.find_failed_episodes(),
        "relevant_vulnerabilities": semantic.get_vulnerabilities_by_tech()
    }
    
    return memories

# 实际使用场景:
Agent: "我现在要测试WordPress站点..."
Agent回忆: "上次我也遇到WordPress 5.7，当时用了CVE-2021-xxxx..."
Agent回忆: "那个漏洞需要特定的条件..."
Agent决策: "好，我知道该怎么做了！"
```

### 4.3 记忆整合与遗忘

```python
def consolidate_memory():
    """定期整合记忆"""
    
    # 1. 从短期记忆提取有用信息到中期
    useful_info = short_term.extract_useful()
    medium_term.integrate(useful_info)
    
    # 2. 从经验中提取模式到长期记忆
    patterns = extract_patterns(medium_term)
    long_term.add_patterns(patterns)
    
    # 3. 清理过期的短期记忆
    short_term.cleanup()
    
    # 4. 更新语义网络
    semantic.update_relationships()
```

## 五、自我认知与反思系统

### 5.1 定期自我检查

Agent会定期停下来反思：

```python
def self_reflection():
    """自我反思"""
    
    # 问自己一系列问题
    questions = [
        "我在做正确的事情吗？",
        "有没有更高效的方法？",
        "我是不是漏掉了什么？",
        "我的假设都正确吗？",
        "需要调整计划吗？"
    ]
    
    # 评估当前路径
    current_path_score = evaluate_current_path()
    
    # 检查是否有更好的选择
    better_options = find_better_options()
    
    # 如果有，考虑改变方向
    if better_options:
        consider_course_correction(better_options)
    
    # 学习经验
    extract_lessons()
```

### 5.2 执行质量检查

每个操作完成后，Agent会检查质量：

```python
def check_execution_quality(execution_result):
    """检查执行质量"""
    
    quality_issues = []
    
    # 1. 完整性检查
    if not is_complete(execution_result):
        quality_issues.append("结果不完整")
    
    # 2. 准确性检查
    if has_inconsistencies(execution_result):
        quality_issues.append("有不一致的地方")
    
    # 3. 证据充分性
    if not has_sufficient_evidence(execution_result):
        quality_issues.append("证据不足")
    
    # 如果有问题，决定下一步
    if quality_issues:
        decision = decide_next_step(quality_issues)
        # 重试 / 补充 / 接受现有结果
```

## 六、Agent决策透明度

### 6.1 决策过程记录

Agent会记录自己的完整思维过程，让你知道它为什么这么做！

```python
# 每个决策都被记录
decision_record = {
    "decision_id": "uuid",
    "timestamp": "iso8601",
    "context": {
        "situation": "完整的情况描述",
        "options_considered": [
            {"option": "选项A", "pros": [...], "cons": [...], "score": 0.8},
            {"option": "选项B", "pros": [...], "cons": [...], "score": 0.6}
        ],
        "reasoning": "详细的推理过程",
        "evidence_used": ["证据1", "证据2"],
        "risks_considered": ["风险1", "风险2"]
    },
    "final_decision": "选择了选项A",
    "justification": "因为...",
    "expected_outcome": "预期会有...结果",
    "actual_outcome": "实际结果..."  # 之后回填
}
```

### 6.2 可解释的AI

用户可以随时问Agent：

```
用户: "你为什么选择先扫描这个端口？"

Agent:
"好问题！让我解释一下我的思考过程：

【我的考虑】
1. 我看到端口139和445开放，这是SMB服务
2. 从我的知识库中，我记得SMB经常有严重漏洞
3. 相比Web端口80/443，SMB可能更快获得系统访问
4. 所以我决定优先检查SMB

【我考虑过的其他选项】
- 先检查Web：得分0.6
- 先检查SMB：得分0.9 ← 我选的

【我的证据】
- nmap显示port 445开放
- banner显示是Windows Server 2019
- 记忆库中有针对这版本的已知漏洞

希望这样解释清楚了！"
```

## 七、工作流控制API

### 7.1 Agent可以调用的工作流接口

```python
# Agent控制工作流的API

workflow.get_current_state()
workflow.get_context()
workflow.can_transition_to(target_state)
workflow.transition_to(new_state, reason)
workflow.pause(reason)
workflow.resume()
workflow.rewind_to(previous_state)  # 回退
workflow.skip_state()              # 跳过
workflow.request_user_input(questions)
workflow.mark_step_completed(step_id)
workflow.get_possible_transitions()
```

### 7.2 状态事件监听

工作区会发出事件，Agent可以响应：

```python
# Agent可以监听状态变化
workflow.on("state_enter", callback)
workflow.on("state_exit", callback)
workflow.on("task_completed", callback)
workflow.on("discovery_made", callback)
workflow.on("blocked", callback)
```

## 八、完整的Agent思维对话示例

让我展示一个真正的AI安全研究员会怎么想！

```
======================================================================
【用户】
帮我测试 example.com

【Agent】 (状态: INITIALIZED → REQUIREMENT_ANALYSIS)
好的，让我先理解一下需求...

【Agent思考】
用户让我测试example.com，但信息不够完整
我需要问一些问题来明确范围
同时先验证授权

【Agent】
在开始之前，我需要确认一些事项：

1. 你有对example.com的书面授权吗？
2. 测试范围包括哪些？（只是Web？还有子域名？内部网络？）
3. 需要什么类型的报告？
4. 有时间限制吗？

让我先从基础的被动侦察开始，不会主动接触目标...

======================================================================
【用户】
已授权，测试Web应用就行，要完整报告。

【Agent】 (状态: REQUIREMENT_ANALYSIS → PLANNING)
好的，授权已确认。让我规划一下...

【Agent思考】
目标是example.com的Web应用
需要完整报告
方法论: 标准Web渗透测试流程

让我从被动信息收集开始...

【Agent】 (状态: PLANNING → RECON)
计划已制定。开始侦察阶段。

首先进行DNS枚举和OSINT收集...

======================================================================
【Agent执行】
调用WebSecuritySkill.dns_enum("example.com")

【结果】
发现子域名: www, api, admin
发现MX记录指向邮件服务器
注册信息显示是2018年创建

【Agent记忆更新】
短期记忆: 刚完成DNS枚举，发现3个子域名
中期记忆: 目标画像更新
情景记忆: 记录这次侦察

【Agent思考】
好的，有几个子域名。www看起来是主站，应该先看这个。
让我检查一下这些Web服务...

【Agent】 (状态: RECON → SCANNING)
侦察完成，发现3个子域名。现在扫描Web服务...

======================================================================
【Agent执行】
调用WebSecuritySkill.service_scan("www.example.com")

【结果】
端口80: nginx 1.20.1
端口443: HTTPS
返回头显示: WordPress/5.7

【Agent记忆更新】
发现: WordPress 5.7
知识图谱: WordPress 5.7关联到CVE-2021-xxxx

【Agent思考】
哦，WordPress 5.7！我记得这个版本有SQL注入漏洞(CVE-2021-xxxx)
我的标准流程是继续全面扫描，但既然已经找到了这个，是不是应该优先验证？
让我想想：

选项1: 继续全面扫描 → 可能发现更多，但需要时间
选项2: 先验证这个WordPress漏洞 → 如果成功，快速获得结果
选项3: 两个并行 → 先看这个，同时不停止其他

评估: 选项2看起来更好，因为这个漏洞是已知高危
而且WordPress很常见，证据已经很明确了

决定: 跳转到VULN_ASSESS，直接验证这个漏洞！

【Agent】 (状态: SCANNING → VULN_ASSESS) [智能跳转！]
扫描发现WordPress 5.7，这个版本有已知高危漏洞(CVE-2021-xxxx)
我决定优先评估这个漏洞，暂时跳过全面扫描。

现在验证这个WordPress漏洞...

======================================================================
【Agent执行】
调用WebSecuritySkill.verify_wordpress_sqli("www.example.com")

【结果】
✅ 漏洞确认存在！
可通过 /wp-json/wp/v2/posts?per_page=1 触发
可以提取用户表数据

【Agent思考】
太好了，漏洞确认！
这是一个高危漏洞，应该优先利用
但按照方法论，我需要确保证据充分...
让我做完整的验证记录...

【Agent】 (状态: VULN_ASSESS → EXPLOITATION)
漏洞确认！存在SQL注入。

现在准备漏洞利用...

======================================================================
(继续...)
```

---

**这就是AI安全研究员的工作方式！**

关键特性:
- ✅ 有记忆，记得过去的事情
- ✅ 有上下文，知道自己在哪
- ✅ 会思考，不是盲目按流程
- ✅ 能调整，根据情况灵活变化
- ✅ 有理由，每一步都能解释
