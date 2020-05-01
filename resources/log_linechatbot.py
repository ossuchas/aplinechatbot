import traceback
from flask_restful import Resource
from flask import request
from datetime import datetime


from models.log_linechatbot import LogChatBotModel


class LogLineChatBot(Resource):
    @classmethod
    def post(cls):
        json_data = request.get_json()
        # print(json_data)
        msg_text_view = json_data["name"]
        userId = json_data["userid"]
        log_models = LogChatBotModel()

        log_models.replyToken = '8ab9ecda51bf4eb89e3617ed0358ad3d'
        log_models.source_groupId = None
        log_models.source_userId = userId
        log_models.source_type = 'user'
        log_models.timestamps = str(datetime.timestamp(datetime.now()))
        log_models.message_type = 'web'
        log_models.message_text = msg_text_view
        log_models.stickerId = None
        log_models.packageId = None
        log_models.beacon_hwid = None
        log_models.beacon_dm = None
        log_models.beacon_type = None
        log_models.beacon_entrydate = None
        log_models.register_flag = 'N'
        log_models.register_empid = None
        log_models.register_email = None

        log_models.save_to_db()

        return {"message": "Save Successful"}, 201


