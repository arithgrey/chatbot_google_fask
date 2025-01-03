class Validator:
    @staticmethod
    def validate_message_data(data):
        # Verifica que los datos sean válidos
        if 'space_name' not in data or 'message_text' not in data:
            raise ValueError("Both 'space_name' and 'message_text' are required.")
