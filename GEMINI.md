# GEMINI.md

This file provides instructional context for the Hello-Agents project to assist Gemini in understanding the codebase and project structure.

## Project Overview

**Hello-Agents** is a systematic, hands-on tutorial project by the Datawhale community designed to teach AI agent construction from scratch. It bridges the gap between theoretical understanding and practical implementation, covering everything from basic LLM interactions to advanced multi-agent systems and Agentic Reinforcement Learning (RL).

### Core Technologies
- **Language:** Python
- **Key Libraries:** `openai`, `langgraph`, `autogen`, `agentscope`, `tavily-python`, `requests`
- **Architectures:** ReAct, Plan-and-Solve, Reflection, Multi-Agent Collaboration
- **Protocols:** MCP (Model Context Protocol), A2A (Agent-to-Agent), ANP (Agent Network Protocol)
- **Frameworks:** Includes a custom-built agent framework (developed in Chapter 7)

## Project Structure

- `/docs` - Comprehensive tutorial documentation in Markdown, organized by chapters (1-16).
- `/code` - Practical code examples corresponding to each chapter.
    - `chapter1-3`: Fundamentals and first agent tests.
    - `chapter4`: Implementation of classic agent paradigms.
    - `chapter7`: Building a custom agent framework from first principles.
    - `chapter10-11`: Advanced protocols (MCP) and Agentic RL (SFT to GRPO).
    - `chapter13-15`: Complex case studies (Trip Planner, AI Town, Deep Research).
- `/Extra-Chapter` - Community-contributed content, including interview questions and advanced technical notes.
- `/Co-creation-projects` - Collaborative projects developed by the community.

## Building and Running

The project is structured as a collection of educational scripts rather than a single monolith application.

### Prerequisites
1.  Python 3.10+ recommended.
2.  Install dependencies for the specific chapter you are working on (usually via `pip install -r requirements.txt` within the chapter or project directory).
3.  Set up environment variables. Most chapters require a `.env` file containing:
    - `API_KEY`: Your LLM provider's API key.
    - `BASE_URL`: The API endpoint.
    - `MODEL_ID`: The model identifier (e.g., `gpt-4o`, `deepseek-chat`).
    - `TAVILY_API_KEY`: Required for search-related tools.

### Running Examples
Navigate to the specific chapter directory and run the Python scripts:
```bash
# Example for Chapter 1
cd code/chapter1
python FirstAgentTest.py
```

## Development Conventions

- **Thought-Action-Observation:** Many implementations follow the ReAct pattern, where the agent explicitly outputs its reasoning before taking an action.
- **Custom Framework:** The project encourages building from first principles. See `code/chapter7/` for the core abstractions (`SimpleAgent`, `HelloAgentsLLM`, `ToolRegistry`).
- **Educational Focus:** Code is designed to be readable and modular, often including verbose logging or print statements to show the agent's internal process.
- **Environment Management:** Use `.env` files for secrets. Never hardcode API keys.

## Important Notes

- **Language:** Primary documentation is in Chinese (`docs/*.md`), while code comments and some secondary docs are in English.
- **License:** CC BY-NC-SA 4.0 (Non-commercial use).
- **Online Reading:** Accessible at [https://datawhalechina.github.io/hello-agents/](https://datawhalechina.github.io/hello-agents/)
