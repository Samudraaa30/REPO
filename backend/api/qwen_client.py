import os
import requests


class QwenClient:

    def __init__(self):
        self.url = "https://openrouter.ai/api/v1/chat/completions"
        self.api_key = os.getenv("OPENROUTER_API_KEY")

    def ask(self, prompt):

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }

        payload = {
            "model": "cohere/north-mini-code:free",
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "temperature": 0.2
        }

        response = requests.post(
            self.url,
            headers=headers,
            json=payload,
            timeout=300
        )

        print("========== OPENROUTER ==========")
        print(response.status_code)
        print(response.text)
        print("===============================")

        if response.status_code != 200:

          print(response.text)

          return {
            "error": response.text
          }

        data = response.json()

        return {
            "response": data["choices"][0]["message"]["content"]
        
        }
    
        data = response.json()

        return {
            "response": data["choices"][0]["message"]["content"]
        }