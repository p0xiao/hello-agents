# 设置控制台输出编码为 UTF-8，解决 Windows 下 GBK 编码无法显示 Unicode emoji 字符的问题
import sys
import io
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

from browser_use import Agent, Browser, ChatBrowserUse, ChatOpenAI
from browser_use.llm import ChatDeepSeek
import asyncio
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv('API_KEY')
base_url = os.getenv('BASE_URL')
model_id = os.getenv('MODEL_ID')

extend_system_message = """
Remember the most important rules: 
1. When performing a search task, open https://www.google.com/ first for search. 
2. Final output.
"""

ACTION_FORMAT_PROMPT = """
Important: Use ONLY the exact parameters allowed for each action. Do NOT add extra parameters.

Correct action formats:
- Click: {"click": {"index": 122}}
- Navigate: {"navigate": {"url": "https://google.com"}}
- Input text: {"input_text": {"index": 5, "text": "hello"}}
- Go back: {"go_back": {}}  # NO parameters allowed!
- Wait: {"wait": {"seconds": 2}}  # Use separate wait action
- Done: {"done": {"text": "Task completed"}}
- Scroll: {"scroll": {"direction": "down"}}
- Extract: {"extract": {"query": "extract info"}}
- Write file: {"write_file": {"file_path": "file.txt", "content": "..."}}
- Read file: {"read_file": {"file_path": "file.txt"}}


WRONG (DO NOT USE):
- {"go_back": {"wait": 2}}  # go_back has NO parameters
- {"click": 122}  # Missing nested object
- {"navigate": "google.com"}
- "action": [{"write_file": {...}, "done": {...}}]
- replace_file
- update_file
- modify_file

CRITICAL RULES:
1. Return actions as an ARRAY of separate objects
2. ONE action type per object - NEVER combine!
3. Return ONLY ONE action per response!
"""

async def example():
    browser = Browser(
        minimum_wait_page_load_time=0.5,        # 最小等待时间（秒）
        wait_for_network_idle_page_load_time=6.0,  # 网络空闲等待时间（增加到6秒）
        wait_between_actions=0.5,               # 动作间等待时间
        # use_cloud=True,  # Uncomment to use a stealth browser on Browser Use Cloud
    )

    # llm = ChatBrowserUse()
    llm = ChatOpenAI(model=model_id, api_key=api_key, base_url=base_url)
    # llm = ChatDeepSeek(model=model_id, api_key=api_key, base_url=base_url)

    agent = Agent(
        # task="Find the number of stars of the browser-use repo",
        task="在sufy.com中的AI大模型广场上，找出标记热门的3个模型",
        llm=llm,
        browser=browser,
        use_vision=True,
        # extend_system_message=ACTION_FORMAT_PROMPT,
        max_actions_per_step=1,  # 限制每步只执行一个动作，减少格式错误
        generate_gif="./output.gif",  # 保存执行过程
    )

    history = await agent.run()
    return history

if __name__ == "__main__":
    history = asyncio.run(example())
