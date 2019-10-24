from flask import Flask, jsonify
from flask_restful import Api
from dotenv import load_dotenv
from flask_cors import CORS
from marshmallow import ValidationError

from db import db
from ma import ma

from resources.chatbot import ChatBot, ChatBotRegister

app = Flask(__name__)

api = Api(app, prefix="/api/v1")

@app.route('/')
def hello_world():
    return 'AP Line Chat Bot Hello World!'

api.add_resource(ChatBot, "/webhook")
api.add_resource(ChatBotRegister, "/register")

if __name__ == '__main__':
    db.init_app(app)
    ma.init_app(app)
    # app.run(host="0.0.0.0", port=5000, debug=True)
    app.run(port=5000)
