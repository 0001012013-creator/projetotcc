import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

class GeminiService:
    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise Exception("GEMINI_API_KEY não encontrada")
        self.client = genai.Client(api_key=api_key)

    def gerar(self, prompt: str) -> str:
        try:
            response = self.client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )
            return response.text
        except Exception as e:
            raise Exception(f"Erro ao chamar Gemini: {e}")
