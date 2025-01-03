# google_chat_service.py
import requests
from config import Config

class GoogleChatService:
    def __init__(self, space_name):
        self.space_name = space_name
        space_config = Config.GOOGLE_CHAT_SPACES.get(space_name)
        if not space_config:
            raise ValueError(f"Space '{space_name}' is not configured.")
        
        self.webhook_url = space_config['webhook_url']
        self.api_key = space_config['api_key']
        self.token = space_config['token']

    def send_message(self, message_text):
        url = f'{self.webhook_url}?key={self.api_key}&token={self.token}'
        message = {"text": message_text}
        
        try:
            response = requests.post(url, json=message)
            if response.status_code == 200:
                return response.json()
            else:
                raise Exception(f"Failed to send message: {response.status_code}")
        except Exception as e:
            raise Exception(f"Error sending message: {e}")
