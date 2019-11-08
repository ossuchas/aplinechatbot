import traceback
from flask_restful import Resource
from flask import request

from libs import chatbot_helper, log_linechatbot as logs, \
    sale_accum_month, beacon_helper

from config import CHANNEL_ACCESS_TOKEN, REPLY_WORDING, \
    REPLY_SALCE_ACCM_B_M_WORDING, REPLY_SALCE_ACCM_C_M_WORDING, \
    DEFAULT_REPLY_WORDING


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
        # get event type beacon or message
        events_type = payload['events'][0]['type']
        # print(events_type)

        groupId = None
        userId = None
        stickerId = None
        packageId = None
        msg_text = None
        name = None

        try:
            groupId = payload['events'][0]['source']['groupId']
            userId = payload['events'][0]['source']['userId']
            # print(userId, groupId)
        except:
            userId = payload['events'][0]['source']['userId']

        # print(userId, groupId)

        source_type = payload['events'][0]['source']['type']
        timestamps = payload['events'][0]['timestamp']
        if events_type == 'message':
            msg_type = payload['events'][0]['message']['type']
        else:
            # msg_type = payload['events'][0]['beacon']['hwid']
            msg_type = 'beacon'

        reply_msg = None

        if msg_type == 'text':
            msg_text = payload['events'][0]['message']['text']
            message = msg_text

            if message in REPLY_SALCE_ACCM_B_M_WORDING:
                sale_accum_month.replyMsg(reply_token, reply_msg, "-1", CHANNEL_ACCESS_TOKEN)
            elif message in REPLY_SALCE_ACCM_C_M_WORDING:
                sale_accum_month.replyMsg(reply_token, reply_msg, "0", CHANNEL_ACCESS_TOKEN)
            elif message in REPLY_WORDING:
                reply_msg = DEFAULT_REPLY_WORDING

                # Reply Message Default Post API
                chatbot_helper.replyMsg(reply_token, reply_msg, CHANNEL_ACCESS_TOKEN)
        elif msg_type == 'beacon':
            msg_text = payload['events'][0]['beacon']['dm']
            stickerId = None
            packageId = None

            if userId == 'U80a30a5bad4ea0f5f7995e5050ab8d7e':
                str_reply = "Hello World Beacon K.{}".format("Suchat S.")
            else:
                str_reply = "Hello World Beacon"

            beacon_helper.replyMsg(reply_token, str_reply, CHANNEL_ACCESS_TOKEN)
        else:
            if msg_type == 'sticker':
                stickerId = payload['events'][0]['message']['stickerId']
                packageId = payload['events'][0]['message']['packageId']
            else:
                stickerId = None
                packageId = None
                msg_text = None

            # message = 'รบกวนระบุคำถามที่สนใจสอบถามด้วยค่ะ'

        # Save Log to DB
        logs.savechatlog2db(reply_token, groupId, userId, source_type, timestamps, msg_type, msg_text, stickerId, packageId)

        # # reply_msg = "{} {}".format(message, name)
        # reply_msg = "{}".format(crm_pd.find_crm_product_by_id('60018'))
        # str_json_obj = loadjson.loadjsonfile()
        #
        # print(str_json_obj[0]['value'])
        # print(str_json_obj[0]['key'])

        # loadjson.loadjsonfile()
        #
        # # Reply Message Post API
        # chatbot_helper.replyMsg(reply_token, reply_msg, CHANNEL_ACCESS_TOKEN)

        return {"message": "Register Line Push and Reply Message Successful"}, 201

