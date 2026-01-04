import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

class Qwen:
    def __init__(self, model_id="Qwen/Qwen1.5-0.5B-Chat"):
        self.model_id = model_id
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.tokenizer = AutoTokenizer.from_pretrained(model_id)
        self.model = AutoModelForCausalLM.from_pretrained(model_id).to(self.device)
        print("模型和分词器加载完成！")

    def generate(self, prompt: str, system_prompt: str) -> str:
        # 准备对话输入
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ]

        # 使用分词器的模板格式化输入
        text = self.tokenizer.apply_chat_template(
            messages,
            tokenize=False,
            add_generation_prompt=True
        )

        # 编码输入文本
        model_inputs = self.tokenizer([text], return_tensors="pt").to(self.device)

        # 使用模型生成回答
        # max_new_tokens 控制了模型最多能生成多少个新的Token
        generated_ids = self.model.generate(
            model_inputs.input_ids,
            max_new_tokens=512
        )

        # 将生成的 Token ID 截取掉输入部分
        # 这样我们只解码模型新生成的部分
        generated_ids = [
            output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
        ]

        # 解码生成的 Token ID
        response = self.tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
        return response
