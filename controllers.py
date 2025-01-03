from flask import request
from google_chat_service import GoogleChatService
from validator import Validator
from response_formatter import ResponseFormatter

class GoogleChatController:
    @staticmethod
    def send_message():

        data = request.get_json()
        try:
            # Validamos los datos
            Validator.validate_message_data(data)
            space_name = data['space_name']
            message_text = data['message_text']
        
            google_chat_service = GoogleChatService(space_name)
            response = google_chat_service.send_message(message_text)

            return ResponseFormatter.format_success_response("Message sent successfully", response)

        except ValueError as e:
            return ResponseFormatter.format_error_response(str(e))

        except Exception as e:
            # Manejo de errores inesperados
            return ResponseFormatter.format_error_response("Failed to send message", str(e))
