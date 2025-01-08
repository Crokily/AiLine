import os
import google.generativeai as genai

class Agent:
    def __init__(
        self,
        name,
        api_key=None,
        model_name="gemini-1.5-flash-8b",
        generation_config=None,
        system_instruction=None,
        history=None,
    ):
        self.name = name
        # 配置API密钥
        self.api_key = api_key or os.environ.get("GEMINI_API_KEY")
        if not self.api_key:
            raise ValueError("API密钥未设置，请提供有效的GEMINI_API_KEY。")
        genai.configure(api_key=self.api_key)

        # 生成配置
        self.generation_config = generation_config or {
            "temperature": 1,
            "top_p": 0.95,
            "top_k": 40,
            "max_output_tokens": 8192,
            "response_mime_type": "text/plain",
        }

        # 系统指令
        self.system_instruction = system_instruction or ""

        # 初始化模型
        self.model = genai.GenerativeModel(
            model_name=model_name,
            generation_config=self.generation_config,
            system_instruction=self.system_instruction,
        )

        self.history = history

        # 创建聊天会话
        self.chat_session = self.model.start_chat(
            history=self.history,
        )

    def process(self, text):
        if not text:
            raise ValueError("输入文本不能为空。")
        response = self.chat_session.send_message(text)
        return response.text.strip()