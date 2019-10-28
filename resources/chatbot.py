import traceback
from flask_restful import Resource
from flask import request

from libs import chatbot_helper, log_linechatbot as logs, crm_products as crm_pd, loadjson

from config import CHANNEL_ACCESS_TOKEN


class ChatBot(Resource):
    @classmethod
    def get(cls):
        return {"message": "Hello World"}, 200


class ChatBotRegister(Resource):
    @classmethod
    def post(cls):
        payload = request.get_json()
        # print(payload)

        reply_token = payload['events'][0]['replyToken']
        userId = payload['events'][0]['source']['userId']
        source_type = payload['events'][0]['source']['type']

        timestamps = payload['events'][0]['timestamp']

        msg_type = payload['events'][0]['message']['type']

        # if userId == 'U80a30a5bad4ea0f5f7995e5050ab8d7e':
        #     name = 'kai'
        # elif userId == 'Ua98b38ab3b83f789b1fbc9ebd0a029b9':
        #     name = 'ying'
        # else:
        #     name = ''

        stickerId = None
        packageId = None
        msg_text = None
        name = None

        if msg_type == 'text':
            msg_text = payload['events'][0]['message']['text']
            message = msg_text
        else:
            if msg_type == 'sticker':
                stickerId = payload['events'][0]['message']['stickerId']
                packageId = payload['events'][0]['message']['packageId']
            else:
                stickerId = None
                packageId = None
                msg_text = None

            message = 'รบกวนระบุคำถามที่สนใจสอบถามด้วยค่ะ'

        # Save Log to DB
        logs.savechatlog2db(reply_token, userId, source_type, timestamps, msg_type, msg_text, stickerId, packageId)

        # reply_msg = "{} {}".format(message, name)
        reply_msg = "{}".format(crm_pd.find_crm_product_by_id('60018'))

        loadjson.loadjsonfile()

        # Reply Message Post API
        chatbot_helper.replyMsg(reply_token, reply_msg, CHANNEL_ACCESS_TOKEN)

        return {"message": "Register Line Push and Reply Message Successful"}, 201

