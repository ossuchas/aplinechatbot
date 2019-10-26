import traceback
from flask_restful import Resource
from flask import request

from libs import chatbot_helper
from config import CHANNEL_ACCESS_TOKEN


class ChatBot(Resource):
    @classmethod
    def get(cls):
        return {"message": "Hello World"}, 200


class ChatBotRegister(Resource):
    @classmethod
    def post(cls):
        payload = request.get_json()
        print(payload)
        reply_token = payload['events'][0]['replyToken']
        userId = payload['events'][0]['source']['userId']

        if userId == 'U80a30a5bad4ea0f5f7995e5050ab8d7e':
            name = 'kai'
        elif userId == 'Ua98b38ab3b83f789b1fbc9ebd0a029b9':
            name = 'ying'
        else:
            name = ''

        # print(userId)
        msg_type = payload['events'][0]['message']['type']
        if msg_type == 'text':
            message = payload['events'][0]['message']['text']
        else:
            message = 'รบกวนระบุคำถามที่สนใจสอบถามด้วยค่ะ'

        reply_msg = "{} {}".format(message, name)

        chatbot_helper.replyMsg(reply_token, reply_msg, CHANNEL_ACCESS_TOKEN)

        return {"message": "Register Line Push and Reply Message Successful"}, 201

