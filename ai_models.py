import requests

class DeepseekAI:
    BASE_URL = 'https://api.deepseek.ai/v1/'

    def __init__(self, api_key):
        self.api_key = api_key

    def _handle_response(self, response):
        if response.status_code != 200:
            raise Exception(f'Error: {response.status_code} - {response.text}')
        return response.json()

    def call_model(self, data):
        headers = {'Authorization': f'Bearer {self.api_key}', 'Content-Type': 'application/json'}
        response = requests.post(self.BASE_URL + 'model', json=data, headers=headers)
        return self._handle_response(response)


class QwenAI:
    BASE_URL = 'https://api.qwen.ai/v1/'

    def __init__(self, api_key):
        self.api_key = api_key

    def _handle_response(self, response):
        if response.status_code != 200:
            raise Exception(f'Error: {response.status_code} - {response.text}')
        return response.json()

    def call_model(self, data):
        headers = {'Authorization': f'Bearer {self.api_key}', 'Content-Type': 'application/json'}
        response = requests.post(self.BASE_URL + 'model', json=data, headers=headers)
        return self._handle_response(response)
