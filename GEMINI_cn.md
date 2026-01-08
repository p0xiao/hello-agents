# GEMINI_cn.md

此文件为 Hello-Agents 项目提供指令上下文，旨在帮助 Gemini 理解代码库和项目结构。

## 项目概览

**Hello-Agents** 是由 Datawhale 社区发起的系统性、重实践的智能体构建教程。该项目旨在弥合理论理解与实践落地之间的鸿沟，内容涵盖从基础的 LLM 交互到高级多智能体系统以及智能体强化学习（Agentic RL）的全过程。

### 核心技术
- **语言:** Python
- **关键库:** `openai`、`langgraph`、`autogen`、`agentscope`、`tavily-python`、`requests`
- **架构:** ReAct、Plan-and-Solve、Reflection、多智能体协作
- **协议:** MCP (Model Context Protocol)、A2A (Agent-to-Agent)、ANP (Agent Network Protocol)
- **框架:** 包含一个自研的智能体框架（在第七章中开发）

## 项目结构

- `/docs` - 详尽的 Markdown 教程文档，按章节（1-16章）组织。
- `/code` - 与各章节对应的配套代码示例。
    - `chapter1-3`: 基础知识和首个智能体测试。
    - `chapter4`: 经典智能体范式的实现。
    - `chapter7`: 从零开始构建自定义智能体框架。
    - `chapter10-11`: 高级协议 (MCP) 和智能体强化学习 (从 SFT 到 GRPO)。
    - `chapter13-15`: 综合案例研究（旅行助手、赛博小镇、深度研究）。
- `/Extra-Chapter` - 社区贡献内容，包括面试题和高级技术笔记。
- `/Co-creation-projects` - 社区协作开发的子项目。

## 构建与运行

本项目是由一系列教育脚本组成的集合，而非单一的庞大应用。

### 前置条件
1. 推荐使用 Python 3.10+。
2. 安装对应章节的依赖项（通常通过章节目录或项目目录下的 `pip install -r requirements.txt` 完成）。
3. 设置环境变量。大多数章节需要一个包含以下内容的 `.env` 文件：
    - `API_KEY`: 您的 LLM 供应商 API 密钥。
    - `BASE_URL`: API 端点地址。
    - `MODEL_ID`: 模型标识符（例如 `gpt-4o`, `deepseek-chat`）。
    - `TAVILY_API_KEY`: 搜索相关工具所需的 API 密钥。

### 运行示例
导航至特定章节目录并运行 Python 脚本：
```bash
# 第一章示例
cd code/chapter1
python FirstAgentTest.py
```

## 开发规范

- **Thought-Action-Observation (思考-行动-观察):** 许多实现遵循 ReAct 模式，智能体在采取行动前会显式地输出其推理过程。
- **自定义框架:** 本项目鼓励从底层原理开始构建。核心抽象（`SimpleAgent`, `HelloAgentsLLM`, `ToolRegistry`）请参考 `code/chapter7/`。
- **教学导向:** 代码设计注重可读性和模块化，通常包含详细的日志或打印语句，以展示智能体的内部处理过程。
- **环境管理:** 使用 `.env` 文件存储敏感信息，严禁在代码中硬编码 API 密钥。

## 注意事项

- **语言:** 主要文档为中文（`docs/*.md`），代码注释和部分辅助文档为英文。
- **许可:** CC BY-NC-SA 4.0（非商业性使用）。
- **在线阅读:** [https://datawhalechina.github.io/hello-agents/](https://datawhalechina.github.io/hello-agents/)
