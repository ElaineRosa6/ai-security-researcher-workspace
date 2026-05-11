# MVP 实施路线图

## 🎯 目标：6周内打造可运行的产品

### 第1周：LLM集成与Brain核心逻辑

#### 第1-2天：LLMClient实现
**文件**：`agent/core/llm_client.py`

```python
# 核心功能
- OpenAI API 客户端
- Claude API 支持
- 本地模型支持 (Ollama)
- Token 计数
- 成本追踪
- 重试机制
- 错误处理
```

#### 第3-4天：提示词管理系统
**文件**：`agent/prompts/__init__.py`，`agent/prompts/loader.py`

```python
# 核心功能
- 从文件加载提示词
- Jinja2 模板渲染
- 提示词版本管理
- 提示词组合和链
```

#### 第5-7天：Brain核心方法
**文件**：`agent/core/brain.py`（完善现有）

```python
# 需要实现的方法
- parse_requirement(): 需求解析
- create_task_plan(): 任务规划
- execute_skill(): 技能执行
- evaluate_result(): 结果评估
```

---

### 第2周：工具执行与工作流引擎

#### 第1-3天：工具执行引擎
**文件**：`ai-agent/harness/tool_executor.py`

```python
# 核心功能
- 安全命令执行
- 沙箱环境
- 超时和资源限制
- 输出解析器基类
- Nmap输出解析
- SQLMap输出解析
```

#### 第4-7天：工作流执行引擎
**文件**：`agent/workflow/yaml_loader.py`，`agent/workflow/runner.py`

```python
# 核心功能
- 工作流YAML加载和验证
- 任务调度器
- 依赖关系管理
- 状态持久化
- 暂停/恢复
```

---

### 第3周：报告与接口

#### 第1-3天：报告系统
**文件**：`agent/reporting/generator.py`，`agent/reporting/templates/`

```python
# 核心功能
- Markdown报告模板
- 发现渲染
- 证据关联
- HTML/PDF导出
- 合规性检查
```

#### 第4-7天：CLI接口
**文件**：`cli/__init__.py`，`cli/main.py`

```python
# 命令列表
- agent start <requirement>
- agent list-workflows
- agent status <session-id>
- agent report <session-id> [--format md|html|pdf]
- agent config
```

---

### 第4周：持久化与部署

#### 第1-3天：数据库集成
**文件**：`agent/persistence/__init__.py`，`agent/persistence/models.py`

```python
# 核心功能
- SQLite/PostgreSQL支持
- 会话存储
- 发现存储
- 证据元数据
- Alembic迁移
```

#### 第4-7天：Docker化
**文件**：`Dockerfile`，`docker-compose.yml`，`.dockerignore`

```yaml
# 服务组件
- agent: 主服务
- postgres: 数据库 (可选)
- tools: 安全工具容器
```

---

### 第5-6周：测试、文档与完善

- 测试覆盖率达到80%+
- CI/CD 集成
- 完整用户文档
- 开发者文档

---

## 📝 具体实施步骤清单

### 优先级P0（必须完成）

#### 1. LLM集成
- [ ] 创建 `agent/core/llm_client.py`
  - [ ] OpenAI API 集成
  - [ ] 聊天补全接口
  - [ ] 流式响应支持
  - [ ] Token使用统计
  - [ ] 重试和错误处理
- [ ] 更新 `agent/core/__init__.py` 导出
- [ ] 创建单元测试 `tests/unit/test_llm_client.py`

#### 2. 提示词加载系统
- [ ] 创建 `agent/prompts/loader.py`
  - [ ] 从目录加载所有提示词
  - [ ] Jinja2模板渲染
  - [ ] 提示词组合
- [ ] 更新现有 `agent/prompts/__init__.py`

#### 3. Brain核心逻辑实现
- [ ] 完善 `agent/core/brain.py`
  - [ ] `parse_requirement()` 完整实现
  - [ ] `create_task_plan()` 完整实现
  - [ ] `execute_skill()` 完整实现
  - [ ] 集成LLMClient
- [ ] 更新单元测试

#### 4. 工具执行引擎
- [ ] 创建 `ai-agent/harness/tool_executor.py`
  - [ ] 命令执行基类
  - [ ] Nmap执行器
  - [ ] SQLMap执行器
  - [ ] 输出解析器
- [ ] 创建单元测试

#### 5. 工作流执行引擎
- [ ] 创建 `agent/workflow/yaml_loader.py`
- [ ] 创建 `agent/workflow/runner.py`
- [ ] 集成到Agent类
- [ ] 测试Web Pentest工作流

---

## 🛠️ 最小运行演示流程

```python
# 使用流程
1. 安装依赖: pip install -r requirements.txt
2. 配置API Key: 复制 .env.example 到 .env，填入OPENAI_API_KEY
3. 运行Agent: python -m cli.main start "对 https://example.com 进行Web渗透测试"
4. 查看状态: python -m cli.main status <session-id>
5. 生成报告: python -m cli.main report <session-id> --format md
```

---

## 📊 依赖关系图

```
LLMClient
    ↓
Brain (需求解析 → 规划 → 执行 → 评估)
    ↓
工具执行引擎 ← 工作流执行引擎
    ↓
报告生成 ← 发现和证据收集
    ↓
CLI / API 接口
```
