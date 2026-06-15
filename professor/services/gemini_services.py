import os
import requests

class GeminiService:


    def gerar(self, prompt):

        api_key = os.getenv("GEMINI_API_KEY")

        url = (
            "https://generativelanguage.googleapis.com/v1beta/"
            "models/gemini-2.5-flash:generateContent"
            f"?key={api_key}"
        )

        payload = {
            "contents": [
                {
                    "parts": [
                        {"text": prompt}
                    ]
                }
            ]
        }

        response = requests.post(url, json=payload)

        print("\nSTATUS GEMINI:")
        print(response.status_code)

        data = response.json()

        print("\nRESPOSTA COMPLETA GEMINI:")
        print(data)

        return data["candidates"][0]["content"]["parts"][0]["text"]