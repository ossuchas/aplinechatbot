import traceback
from flask_restful import Resource
from flask import request
from datetime import datetime


from models.chatbot_mst_conf import MstMsgConfigModel
from schemas.chatbot_mst_conf import MstMsgConfSchema


msg_schema = MstMsgConfSchema()
msg_list_schema = MstMsgConfSchema(many=True)


class ChatBotMstConf(Resource):
    @classmethod
    def get(cls, _user_token_id: str):
        msg = MstMsgConfigModel.find_by_id(1)
        if msg:
            return msg_schema.dump(msg), 200

        return {"message": "No Data Found"}, 404

