# Qwen Code Context File

## Project Overview

Hello-Agents is a comprehensive, open-source tutorial project by Datawhale community focused on building AI agents from scratch. It provides both theoretical knowledge and practical implementation of agent systems, covering everything from basic agent concepts to advanced multi-agent applications.

The project is structured into five main parts:
1. Agent and LLM fundamentals (Chapters 1-3)
2. Building LLM-based agents (Chapters 4-7) 
3. Advanced knowledge expansion (Chapters 8-12)
4. Comprehensive case studies (Chapters 13-15)
5. Capstone project and future outlook (Chapter 16)

The project emphasizes hands-on practice, with all code examples provided in the `code` directory. It covers various agent frameworks like LangGraph, AutoGen, AgentScope, and teaches how to build custom agent frameworks from scratch.

## Project Structure

- `/docs` - Complete tutorial content organized by chapters
- `/code` - All practical code examples organized by chapter
- `/Extra-Chapter` - Community contributed content and additional topics
- `/Additional-Chapter` - Additional guides (e.g., installation guides)
- `/Co-creation-projects` - Community collaboration projects

## Key Technologies & Concepts

- Large Language Model (LLM) based agents
- Agent architectures (reactive, deliberative, hybrid)
- Agent communication protocols (MCP, A2A, ANP)
- Memory systems and RAG
- Context engineering
- Multi-agent systems and collaboration
- Agent evaluation frameworks
- Agentic Reinforcement Learning (SFT to GRPO)

## Building and Running

The project is primarily educational with practical code examples. To run the code examples:

1. Install required dependencies (typically Python packages like `openai`, `tavily-python`, `requests`, etc.)
2. Set up API keys for services like OpenAI and Tavily in environment variables
3. Run the Python scripts in the `code` directory

For example, the first agent example in `code/chapter1/TravelAssistantAgent.py` demonstrates a complete agent loop with tools for weather checking and attraction recommendation.

## Development Conventions

- The project uses Python for most code examples
- Follows a "Theory + Practice" approach with each concept accompanied by working code
- Uses the Thought-Action-Observation pattern for agent implementations
- Emphasizes building from first principles rather than just using existing frameworks
- Code examples are designed to be educational and easily modifiable for experimentation

## Special Notes

- The project is licensed under CC BY-NC-SA 4.0 (non-commercial use)
- Online reading is available at https://datawhalechina.github.io/hello-agents/
- The project includes both traditional AI agent concepts and modern LLM-based agents
- It covers the difference between workflows and agents, emphasizing goal-oriented autonomous behavior