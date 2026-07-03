import requests

class QwenClient:

    def __init__(self, url):
        self.url = url.rstrip("/")

    def ask(self, prompt):

        payload = {
            "prompt": prompt
        }

        try:

            response = requests.post(
                self.url,
                json=payload,
                timeout=300
            )

            response.raise_for_status()

            return response.json()

        except Exception as e:

            return {
                "error": str(e)
            }