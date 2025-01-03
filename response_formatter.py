class ResponseFormatter:
    @staticmethod
    def format_success_response(message, response):
        return {
            'status': 'success',
            'message': message,
            'response': response
        }

    @staticmethod
    def format_error_response(message, error_details=None):
        return {
            'status': 'error',
            'message': message,
            'response': error_details
        }
