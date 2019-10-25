import traceback
from flask_restful import Resource
from flask import request

from libs import chatbot_helper


CHANNEL_ACCESS_TOKEN="wXjIZWvNNerxSVIpFVomPA4baBMaXhZtSJdJT11Uw4E8IOqzoJ+DGo++h/TPthxBM2LbrPCpiWiZX0GkXXENi9FE0DccFs0d6fSgntVhbj7Kf1iWp3hwXtJUOYSm5Dib7jC121/2bDpT1b0bIP1N4wdB04t89/1O/w1cDnyilFU="

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
        reply_token = payload['events'][0]['replyToken']
        print(reply_token)
        message = payload['events'][0]['message']['text']
        print(message)
        reply_msg = message

        chatbot_helper.replyMsg(reply_token,reply_msg,CHANNEL_ACCESS_TOKEN)

        return {"message":"Save Successful"}, 201

