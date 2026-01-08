# Hello-Agents 智能体指南

本仓库是一个全面的教程和代码库，用于从头开始构建 AI 智能体。贡献代码时请遵循以下约定。

## 构建、检查和测试命令

### Python 项目

**代码检查和类型检查:**
```bash
ruff check .                    # 使用 ruff 进行代码检查
ruff check --fix .              # 自动修复代码检查问题
mypy src/                       # 类型检查
```

**运行测试:**
```bash
python test_react_agent.py      # 运行单个测试文件
pytest                          # 运行所有测试
pytest tests/test.py            # 单个测试文件
pytest tests/test.py::test_func # 特定测试函数
```

**依赖管理:**
```bash
pip install -r requirements.txt
pip install -e ".[dev]"         # 对于 pyproject.toml 项目
```

### 前端项目 (TypeScript/Vue)

```bash
npm run dev                     # 启动开发服务器
npm run build                   # 构建生产版本
npm run preview                 # 预览生产构建
npx vue-tsc --noEmit            # 仅类型检查
```

## 代码风格指南

### Python 代码

**导入:** 组织顺序为 标准库 → 第三方库 → 本地模块
```python
from __future__ import annotations
import json
from typing import Any, Dict, Optional
from openai import OpenAI
from my_module import local_function
```

**类型提示:** 始终为参数和返回值添加类型。模型使用 dataclass，验证使用 Pydantic
```python
@dataclass
class User:
    id: int
    username: str
    is_active: bool = True

def process(user: User) -> Optional[dict[str, Any]]:
    return {"username": user.username} if user.is_active else None
```

**格式:** 4 空格缩进，最大 100 字符，使用 f-strings，Google 风格文档字符串

**错误处理:** 使用特定异常，使用 loguru
```python
try:
    result = api_call()
except requests.RequestException as e:
    logger.error(f"API failed: {e}")
```

**命名:** 变量/函数使用 snake_case，类使用 PascalCase，常量使用 UPPER_SNAKE_CASE，私有成员使用 _prefix

**环境:** 使用 python-dotenv，创建 .env.example，永远不提交 .env

### TypeScript 代码

**导入:** ES6 语法，优先使用命名导入
```typescript
import { createApp } from "vue";
import axios from "axios";
import { myFunc } from "./utils";
```

**类型定义:** 对象使用接口，联合类型使用类型。避免使用 `any`
```typescript
interface User {
  id: number;
  username: string;
}
async function fetchUser(): Promise<User> {
  return (await axios.get<User>("/api/user")).data;
}
```

**错误处理:** 使用 instanceof 检查类型错误

**命名:** 变量/函数使用 camelCase，类/接口使用 PascalCase，常量使用 UPPER_SNAKE_CASE

### 智能体模式

**ReAct 架构:** 思考 → 行动 → 观察模式，配合工具注册
```python
PROMPT = """
Available tools: {tools}
Thought: [reasoning]
Action: tool_name[input] or Finish[answer]
Question: {question}
History: {history}
"""
```

**工具实现:** 纯函数，类型提示，描述性错误
```python
def search(query: str) -> str:
    """Search web for info."""
    try:
        return results
    except Exception as e:
        return f"Search failed: {e}"
```

## 项目结构

```
hello-agents/
├── docs/              # 文档
├── code/              # 章节代码示例
│   ├── chapter1/      # 基础智能体
│   ├── chapter7/      # 框架实现
│   └── chapter14/     # 全栈应用 (FastAPI + Vue)
└── Co-creation-projects/  # 社区贡献
```

## 重要提示

- 双语项目（中文/英文）- 检查现有内容语言
- 教育代码: 清晰度 > 优化
- 避免不必要的注释
- 遵循现有模式，不要引入新框架
- Windows: 如有需要在 Python 脚本顶部添加 UTF-8 编码声明
