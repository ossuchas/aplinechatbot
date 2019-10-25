import traceback
from flask_restful import Resource
from flask import request

from libs import chatbot_helper
from config import CHANNEL_ACCESS_TOKEN


# CHANNEL_ACCESS_TOKEN="wXjIZWvNNerxSVIpFVomPA4baBMaXhZtSJdJT11Uw4E8IOqzoJ+DGo++h/TPthxBM2LbrPCpiWiZX0GkXXENi9FE0DccFs0d6fSgntVhbj7Kf1iWp3hwXtJUOYSm5Dib7jC121/2bDpT1b0bIP1N4wdB04t89/1O/w1cDnyilFU="

class ChatBot(Resource):
    @classmethod
    def get(cls):
        return {"message": "Hello World"}, 200


class ChatBotRegister(Resource):
    @classmethod
    def post(cls):
        payload = request.get_json()
        reply_token = payload['events'][0]['replyToken']
        msg_type = payload['events'][0]['message']['type']
        if msg_type == 'text':
            message = payload['events'][0]['message']['text']
        else:
            message = 'รบกวนระบุคำถามที่สนใจสอบถามด้วยค่ะ'

        reply_msg = message

        chatbot_helper.replyMsg(reply_token, reply_msg, CHANNEL_ACCESS_TOKEN)

        return {"message": "Register Line Push and Reply Message Successful"}, 201

