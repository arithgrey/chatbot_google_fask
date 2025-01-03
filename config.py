import os

class Config:
    GOOGLE_CHAT_SPACES = {
        "chatbot_space_test": {
            "webhook_url": os.getenv('TEST_GOOGLE_CHAT_SPACE'), #ejemplo -> https://chat.googleapis.com/v1/spaces/aquí tu space/messages
            "api_key": os.getenv('TEST_GOOGLE_API_KEY'),
            "token": os.getenv('TEST_GOOGLE_CHAT_TOKEN')
        },
        "space_2": {
            "webhook_url": "space_url_for_space",
            "api_key": os.getenv('GOOGLE_API_KEY_2'),
            "token": os.getenv('GOOGLE_CHAT_TOKEN_2')
        }
    }
