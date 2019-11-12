import traceback
from flask_restful import Resource
from flask import request

from libs import chatbot_helper, log_linechatbot as logs, \
    sale_accum_month, beacon_helper, menu_01_sale as m1, \
    menu_01_sale_timeline as m1_SDH, \
    leadlag_bg_all, leadlag_bg_project, leadlag_bg_sub

from config import CHANNEL_ACCESS_TOKEN, REPLY_WORDING, \
    REPLY_SALCE_ACCM_B_M_WORDING, REPLY_SALCE_ACCM_C_M_WORDING, \
    DEFAULT_REPLY_WORDING, \
    MENU_01, MENU_02, MENU_03, MENU_04, MENU_05, MENU_06, \
    MENU_01_01_SDH, MENU_02_01_TH, MENU_03_01_CD1, MENU_04_01_CD2, \
    LL_MSG_All, LL_MSG_PROJ, LL_MSG_SUB

from models.chatbot_mst_user import MstUserModel
from models.log_linechatbot import LogChatBotModel
from schemas.chatbot_mst_user import MstUserSchema


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
        source_type = payload['events'][0]['source']['type']
        timestamps = payload['events'][0]['timestamp']

        # get event type beacon or message
        events_type = payload['events'][0]['type']
        # print(events_type)

        groupId = None
        userId = None
        stickerId = None
        packageId = None
        msg_text = None
        name = None
        beacon_hwid = None
        beacon_dm = None
        beacon_type = None

        try:
            groupId = payload['events'][0]['source']['groupId']
            userId = payload['events'][0]['source']['userId']
            # print(userId, groupId)
        except:
            userId = payload['events'][0]['source']['userId']

        if events_type == 'message':
            msg_type = payload['events'][0]['message']['type']
        else:
            msg_type = 'beacon'

        reply_msg = None

        if msg_type == 'text':
            msg_text = payload['events'][0]['message']['text']
            message = msg_text

            if message in MENU_01:
                m1.replyMsg(reply_token, None, CHANNEL_ACCESS_TOKEN)
            elif message in MENU_01_01_SDH:
                m1_SDH.replyMsg(reply_token, None, CHANNEL_ACCESS_TOKEN)
            elif message in MENU_02:
                sale_accum_month.replyMsg(reply_token, reply_msg, "-1", CHANNEL_ACCESS_TOKEN)
            elif message in MENU_03:
                sale_accum_month.replyMsg(reply_token, reply_msg, "-1", CHANNEL_ACCESS_TOKEN)
            elif message in MENU_04:
                sale_accum_month.replyMsg(reply_token, reply_msg, "-1", CHANNEL_ACCESS_TOKEN)
            # Lead Lag
            elif message in LL_MSG_All:
                leadlag_bg_all.replyMsg(reply_token, None, CHANNEL_ACCESS_TOKEN)
            elif message in LL_MSG_SUB:
                leadlag_bg_sub.replyMsg(reply_token, None, CHANNEL_ACCESS_TOKEN)
            elif message in LL_MSG_PROJ:
                leadlag_bg_project.replyMsg(reply_token, None, CHANNEL_ACCESS_TOKEN)
            elif message in REPLY_SALCE_ACCM_B_M_WORDING:
                sale_accum_month.replyMsg(reply_token, reply_msg, "-1", CHANNEL_ACCESS_TOKEN)
            elif message in REPLY_SALCE_ACCM_C_M_WORDING:
                sale_accum_month.replyMsg(reply_token, reply_msg, "0", CHANNEL_ACCESS_TOKEN)
            elif message in REPLY_WORDING:
                reply_msg = DEFAULT_REPLY_WORDING

                # Reply Message Default Post API
                chatbot_helper.replyMsg(reply_token, reply_msg, CHANNEL_ACCESS_TOKEN)
        elif msg_type == 'beacon':
            beacon_hwid = payload['events'][0]['beacon']['hwid']
            beacon_dm = payload['events'][0]['beacon']['dm']
            beacon_type = payload['events'][0]['beacon']['type']
            stickerId = None
            packageId = None
            msg_text = None

            user = MstUserModel().find_by_token_id(userId)

            if user:
                log = LogChatBotModel().find_by_token_beacon_today(userId)

                # Check Revisit..!!
                # if log:
                #     msg_text = "Hello World Beacon K.{} Revisit..!!".format(user.user_full_name)
                # else:
                #     msg_text = "Hello World Beacon K.{} New Walk..".format(user.user_full_name)
                if not log:
                    msg_text = "Hello World Beacon K.{} New Walk..".format(user.user_full_name)

                beacon_helper.replyMsg(reply_token, msg_text, CHANNEL_ACCESS_TOKEN)
        else:
            if msg_type == 'sticker':
                stickerId = payload['events'][0]['message']['stickerId']
                packageId = payload['events'][0]['message']['packageId']
            else:
                stickerId = None
                packageId = None
                msg_text = None

        # Save Log to DB
        logs.savechatlog2db(reply_token, groupId,
                            userId, source_type,
                            timestamps, msg_type,
                            msg_text, stickerId, packageId,
                            beacon_hwid, beacon_dm, beacon_type)

        return {"message": "Register Line Push and Reply Message Successful"}, 201

