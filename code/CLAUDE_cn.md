# CLAUDE_cn.md

本文件为 Claude Code（claude.ai/code）在本仓库中进行代码工作的提供性指南。

## 项目概述

Hello-Agents 是一个教授 AI Agent 开发的教程仓库，包含第 1–16 章，分别展示不同的 Agent 框架与协议。核心框架是 HelloAgents（PyPI 包名为 hello-agents）。

## 架构

### 章节组织

| 章节 | 主题 | 关键框架 |
|------|------|----------|
| 1-5 | 基础 Agent 概念 | SimpleAgent、函数调用 |
| 6 | 多智能体框架 | LangGraph、AutoGen、AgentScope、CAMEL |
| 7-9 | 高级工作流 | 知识图谱、RAG |
| 10 | MCP 协议 | Model Context Protocol 服务器 |
| 11 | Agent 训练 | SFT、GRPO、RL 训练流水线 |
| 12 | Agent 评估 | BFCL、GAIA 基准 |
| 13-16 | 完整应用 | 行程规划、AI Town、深度研究 |

### 核心依赖

- hello-agents：主框架（pip install hello-agents[evaluation]==0.2.3）
- langgraph：工作流编排
- openai、deepseek：LLM 提供商
- fastapi：后端服务
- vue3 + vite：前端（第 13、15 章）

### 核心框架概念

- SimpleAgent：采用 ReAct 模式的基础 Agent
- MCPTool：MCP 协议工具封装
- RLTrainingTool：SFT/GRPO 训练工具
- HelloAgentsLLM：LLM 抽象层

## 开发命令

每个章节都有独立的虚拟环境与依赖：

```bash
# 章节独立环境配置
cd chapter6/Langgraph
pip install -r requirements.txt

cd chapter10/weather-mcp-server
pip install -r requirements.txt
pip install -e .  # 以可编辑模式安装当前包

# 运行示例
python chapter12/02_bfcl_quick_start.py
python chapter12/05_gaia_quick_start.py
python chapter11/06_complete_pipeline.py
```

### 环境变量

在不同章节中需要：
- OPENAI_API_KEY 或 DEEPSPEAK_API_KEY：LLM 访问密钥
- HF_TOKEN：HuggingFace 访问（GAIA 数据集）
- AMAP_MAPS_API_KEY：高德/地图服务
+- WANDB_API_KEY：Weights & Biases 监控（可选）

### MCP 服务器开发

使用 /mcp-builder 命令调用 MCP 构建助手来创建 MCP 服务器。完整工作流见 [.iflow/commands/mcp-builder.md](./.iflow/commands/mcp-builder.md)：
1. 研究目标 API 文档
2. 制定工具选择方案
3. 使用 FastMCP（Python）或 MCP SDK（TypeScript）实现
4. 编写评估 XML 文件
5. 使用提供的评估脚本进行测试

## 代码范式

### 使用 MCP 工具的 Simple Agent
```python
from hello_agents import SimpleAgent, HelloAgentsLLM
from hello_agents.tools import MCPTool

amap_tool = MCPTool(
    name="amap",
    server_command=["uvx", "amap-mcp-server"],
    env={"AMAP_MAPS_API_KEY": "your_key"},
    auto_expand=True
)

agent = SimpleAgent(name="assistant", llm=HelloAgentsLLM())
agent.add_tool(amap_tool)
```

### Agent 式 RL 流水线（第 11 章）
```python
from hello_agents.tools import RLTrainingTool
rl_tool = RLTrainingTool()
result = rl_tool.run({"action": "train", "algorithm": "sft", ...})
```

## 重要说明

- 这是示例/教程代码，并非生产级库
- 每个章节都有独立的 requirements.txt
- 第 12 章（评估）需要安装 hello-agents[evaluation] 扩展
- MCP 服务器通过 stdio/SSE 传输作为长运行进程运行
- 父目录包含主 HelloAgents 框架仓库

