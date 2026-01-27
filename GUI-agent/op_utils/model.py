import os
import base64
from openai import OpenAI
from typing import List, Dict, Any
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY")
BASE_URL = os.getenv("OPENAI_BASE_URL")

class Model:
    GOOGLE_GEMINI_3_FLASH_PREVIEW = "[次]gemini-2.5-pro"

class LVMChat:
    """支持会话记忆的多模态聊天类"""

    def __init__(self, api_key: str = API_KEY, base_url: str = BASE_URL,
                 model: str = "[次]gemini-2.5-pro"):
        self.client = OpenAI(api_key=api_key, base_url=base_url)
        self.model = model
        self.conversation_history: List[Dict[str, Any]] = []

    # 👇 修改这里：添加 res_format 参数
    def get_multimodal_response(self, text: str, image_paths: str,
                                res_format: str = None,  # 新增参数
                                use_history: bool = False) -> str:
        """
        支持记忆的图文对话
        """
        # 1. 加载图片并构建当前消息
        base64_image = self._encode_image(image_paths)
        current_message = {
            "role": "user",
            "content": [
                {"type": "image_url",
                 "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}},
                {"type": "text", "text": text}
            ]
        }

        # 2. 如果启用历史，把之前的对话也带上
        if use_history:
            messages = self.conversation_history + [current_message]
            # print(f"📚 使用历史上下文，共 {len(self.conversation_history)} 条")
        else:
            messages = [current_message]

        # 3. 处理 JSON 模式参数
        # OpenAI 客户端通常接收 response_format={"type": "json_object"}
        extra_args = {}
        if res_format == "json":
            extra_args["response_format"] = {"type": "json_object"}

        # 4. 调用API
        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            **extra_args
        )
        # 有些环境可能直接返回字符串，这里做一个兼容判断
        if isinstance(response, str):
            result = response
        else:
            # 标准 OpenAI 对象提取
            result = response.choices[0].message.content

        # 5. 更新历史记录
        if use_history:
            self.conversation_history.append(current_message)
            self.conversation_history.append({
                "role": "assistant",
                "content": result
            })

        return result

    def _encode_image(self, image_path):
        """辅助方法：转base64"""
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')

    def clear_history(self):
        """清空记忆"""
        self.conversation_history = []