# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Hello-Agents is a tutorial repository teaching AI agent development, with chapters 1-16 demonstrating different agent frameworks and protocols. The core framework is **HelloAgents** (`hello-agents` PyPI package).

## Architecture

### Chapter Organization

| Chapter | Focus | Key Frameworks |
|---------|-------|----------------|
| 1-5 | Basic agent concepts | SimpleAgent, function calling |
| 6 | Multi-agent frameworks | LangGraph, AutoGen, AgentScope, CAMEL |
| 7-9 | Advanced workflows | Knowledge graphs, RAG |
| 10 | MCP protocol | Model Context Protocol servers |
| 11 | Agent training | SFT, GRPO, RL training pipelines |
| 12 | Agent evaluation | BFCL, GAIA benchmarks |
| 13-16 | Full applications | Trip planner, AI town, deep research |

### Core Dependencies

- **hello-agents**: Main framework (`pip install hello-agents[evaluation]==0.2.3`)
- **langgraph**: Workflow orchestration
- **openai, deepseek**: LLM providers
- **fastapi**: Backend services
- **vue3 + vite**: Frontend (chapters 13, 15)

### Key Framework Concepts

- `SimpleAgent`: Basic agent with ReAct pattern
- `MCPTool`: MCP protocol tool wrapper
- `RLTrainingTool`: SFT/GRPO training
- `HelloAgentsLLM`: LLM abstraction layer

## Development Commands

Each chapter has its own virtual environment and dependencies:

```bash
# Chapter-specific setup
cd chapter6/Langgraph
pip install -r requirements.txt

cd chapter10/weather-mcp-server
pip install -r requirements.txt
pip install -e .  # Package in editable mode

# Run examples
python chapter12/02_bfcl_quick_start.py
python chapter12/05_gaia_quick_start.py
python chapter11/06_complete_pipeline.py
```

### Environment Variables

Required for various chapters:
- `OPENAI_API_KEY` or `DEEPSPEAK_API_KEY`: LLM access
- `HF_TOKEN`: HuggingFace access (GAIA dataset)
- `AMAP_MAPS_API_KEY`: Amap/Maps services
- `WANDB_API_KEY`: Weights & Biases monitoring (optional)

### MCP Server Development

Use the `/mcp-builder` command to invoke the MCP builder agent for creating MCP servers. See `.iflow/commands/mcp-builder.md` for the full workflow:
1. Research API documentation
2. Create tool selection plan
3. Implement with FastMCP (Python) or MCP SDK (TypeScript)
4. Create evaluation XML file
5. Test with provided evaluation scripts

## Code Patterns

### Simple Agent with MCP Tools
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

### Agentic RL Pipeline (Chapter 11)
```python
from hello_agents.tools import RLTrainingTool
rl_tool = RLTrainingTool()
result = rl_tool.run({"action": "train", "algorithm": "sft", ...})
```

## Important Notes

- This is example/tutorial code, not a production library
- Each chapter has independent `requirements.txt`
- Chapter 12 (evaluation) requires `hello-agents[evaluation]` extra
- MCP servers run as long-running processes via stdio/SSE transport
- Parent directory contains the main HelloAgents framework repo
