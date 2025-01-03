from flask import Flask, jsonify
from controllers import GoogleChatController
from flask_restful import Api

app = Flask(__name__)
api = Api(app)

@app.route('/send-message', methods=['POST'])
def send_message():
    response = GoogleChatController.send_message()
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
