import traceback
from flask_restful import Resource
from flask import request


class ChatBot(Resource):
    @classmethod
    def get(cls):
        print("xx")
        return {"message": "Hello World"}, 200


class ChatBotRegister(Resource):
    @classmethod
    def post(cls):
        # payload = request.json
        payload = request.get_json()
        print(payload)
        Reply_token = payload['events'][0]['replyToken']
        print(Reply_token)
        message = payload['events'][0]['message']['text']
        print(message)

        try:
            return {"message": "Save Successfully"}, 201
        except:
            return {"message": "Failed to Save"}, 500
