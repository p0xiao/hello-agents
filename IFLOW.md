# IFLOW.md - Hello-Agents 项目上下文

## 项目概述

Hello-Agents 是 Datawhale 社区发起的**系统性智能体学习教程项目**，旨在从零开始教授智能体系统的设计与实现。项目涵盖从基础理论到实际应用的完整知识体系，包括智能体经典范式（ReAct、Plan-and-Solve、Reflection）、主流框架（LangGraph、AutoGen、AgentScope）、通信协议（MCP、A2A、ANP）以及综合案例实战。

**项目定位**：面向 AI 开发者、软件工程师和自学者，通过理论与实践相结合的方式，帮助学习者从大语言模型的"使用者"成长为智能体系统的"构建者"。

---

## 技术栈

### 核心依赖

| 类别 | 技术/库 | 用途 |
|------|---------|------|
| **LLM 框架** | `langgraph`, `langchain_openai` | 智能体工作流编排 |
| **LLM SDK** | `openai` | OpenAI 及兼容 API 调用 |
| **环境管理** | `python-dotenv` | 环境变量加载 |
| **搜索工具** | `tavily-python` | Tavily Search API 集成 |
| **框架** | `autogen`, `agentscope` | 多智能体框架 |
| **训练** | `transformers`, `trl`, `peft` | LLM 训练（SFT/GRPO） |
| **评估** | `bfcl`, `gaia-benchmark` | 智能体性能评估 |

### 主要技术方向

- **智能体范式**：ReAct、Plan-and-Solve、Reflection、Self-Reflection
- **通信协议**：MCP（Model Context Protocol）、A2A（Agent-to-Agent）、ANP（Agent Network Protocol）
- **记忆系统**：Working Memory、Episodic Memory、Semantic Memory、RAG
- **训练方法**：SFT（监督微调）、GRPO（Group Relative Policy Optimization）

---

## 项目结构

```
hello-agents/
├── code/                          # 配套代码实现
│   ├── chapter1/                  # 初识智能体
│   ├── chapter2/                  # 智能体发展史
│   ├── chapter3/                  # 大语言模型基础
│   ├── chapter4/                  # 智能体经典范式实现
│   ├── chapter5/                  # 低代码平台实践
│   ├── chapter6/                  # 框架开发（LangGraph/AutoGen/AgentScope）
│   ├── chapter7/                  # 自研 Agent 框架
│   ├── chapter8/                  # 记忆与检索系统
│   ├── chapter9/                  # 上下文工程
│   ├── chapter10/                 # 智能体通信协议（MCP/A2A/ANP）
│   ├── chapter11/                 # Agentic-RL 训练实战
│   ├── chapter12/                 # 智能体性能评估
│   ├── chapter13/                 # 智能旅行助手（综合案例）
│   ├── chapter14/                 # 深度研究智能体
│   ├── chapter15/                 # 赛博小镇
│   ├── chapter16/                 # 毕业设计项目
│   └── demo/                      # 示例代码
├── docs/                          # 文档目录（中英文）
├── Co-creation-projects/          # 社区贡献项目
├── Extra-Chapter/                 # 额外章节内容
└── Additional-Chapter/            # 安装配置指南
```

---

## 开发约定

### 代码风格

1. **环境变量管理**：使用 `python-dotenv` 加载 `.env` 文件
   ```python
   from dotenv import load_dotenv
   load_dotenv()
   API_KEY = os.environ.get("API_KEY")
   ```

2. **LLM 客户端封装**：参考 `OpenAICompatibleClient` 类的实现模式
   ```python
   class OpenAICompatibleClient:
       def __init__(self, model: str, api_key: str, base_url: str):
           self.model = model
           self.client = OpenAI(api_key=api_key, base_url=base_url)
       
       def generate(self, prompt: str, system_prompt: str) -> str:
           # 实现逻辑
   ```

3. **工具函数定义**：使用类型提示和详细 docstring
   ```python
   def get_weather(city: str) -> str:
       """通过调用 API 查询天气信息。"""
       # 实现逻辑
   ```

4. **ReAct 模式**：遵循 Thought-Action-Observation 循环
   ```
   Thought: 思考过程
   Action: function_name(arg_name="arg_value")
   Observation: 工具执行结果
   ```

5. **输出解析**：使用正则表达式提取 LLM 输出中的 Action
   ```python
   action_match = re.search(r"Action: (.*)", llm_output, re.DOTALL)
   tool_name = re.search(r"(\w+)\(", action_str).group(1)
   ```

### 文件命名

- **章节代码**：`code/chapter{N}/` 目录下使用序号前缀（`01_`, `02_`）
- **测试文件**：`test_*.py` 前缀表示单元测试
- **配置文件**：`.env.example` 为环境变量模板

### 依赖管理

- 每个独立项目/章节包含 `requirements.txt`
- 使用 `pip install -r requirements.txt` 安装依赖

---

## 构建与运行

### 环境准备

```bash
# 克隆项目
git clone https://github.com/datawhalechina/hello-agents.git
cd hello-agents

# 创建虚拟环境（推荐）
python -m venv venv
source venv/bin/activate  # Linux/Mac
# 或
.\venv\Scripts\activate   # Windows

# 安装依赖（以 chapter6/Langgraph 为例）
cd code/chapter6/Langgraph
pip install -r requirements.txt
```

### 运行示例

```bash
# 运行 chapter1 智能旅行助手示例
cd code/chapter1
python FirstAgentTest.py

# 运行 chapter4 ReAct 示例
cd code/chapter4
python ReAct.py

# 运行 chapter10 MCP 服务器
cd code/chapter10
python 14_weather_mcp_server.py
```

### 环境变量配置

创建 `.env` 文件（参考 `.env.example`）：

```env
# API 配置
API_KEY=your_api_key
BASE_URL=https://api.openai.com/v1
MODEL_ID=gpt-4

# Tavily 搜索
TAVILY_API_KEY=your_tavily_key

# 其他配置
...
```

---

## 关键代码模式

### 工具注册与调用

```python
# 1. 定义工具函数
def tool_function(param: str) -> str:
    """工具说明"""
    # 实现
    return result

# 2. 注册到工具字典
available_tools = {
    "tool_name": tool_function,
}

# 3. 解析并执行
if tool_name in available_tools:
    observation = available_tools[tool_name](**kwargs)
```

### 主循环模式（ReAct）

```python
prompt_history = [f"用户请求: {user_input}"]

for i in range(max_iterations):
    # 构建 prompt
    full_prompt = "\n".join(prompt_history)
    
    # 调用 LLM
    llm_output = llm.generate(full_prompt, system_prompt)
    
    # 解析 Action
    action_match = re.search(r"Action: (.*)", llm_output)
    
    if action_str.startswith("finish"):
        # 完成任务
        break
    
    # 执行工具
    observation = execute_tool(action_str)
    prompt_history.append(f"Observation: {observation}")
```

### 多智能体通信

```python
# A2A 协议示例
from a2a import A2AClient, A2AServer

# 创建 A2A 服务器
server = A2AServer(agent=my_agent)
await server.start()

# 创建客户端调用其他智能体
client = A2AClient(server_url="http://other-agent:8000")
response = await client.send_message(message)
```

---

## 常见任务

| 任务 | 位置 | 说明 |
|------|------|------|
| 学习 ReAct 范式 | `code/chapter4/ReAct.py` | 手动实现 ReAct 模式 |
| 了解 MCP 协议 | `code/chapter10/` | MCP 服务器/客户端示例 |
| 构建旅行助手 | `code/chapter13/` | MCP 与多智能体协作案例 |
| 实现 RAG 记忆 | `code/chapter8/10_RAG_Pipeline_Complete.py` | 完整 RAG 流水线 |
| 训练 Agent | `code/chapter11/06_complete_pipeline.py` | SFT + GRPO 训练流程 |

---

## 注意事项

1. **API 密钥**：大多数示例需要外部 API 密钥（OpenAI、Tavily、高德地图等）
2. **版本兼容性**：`langgraph` 等库更新频繁，示例使用特定版本
3. **协议演进**：MCP、A2A 协议仍在发展中，示例代码可能需适配新版本
4. **社区资源**：有问题可在 GitHub Issue 讨论，或参考 Extra-Chapter 内容
