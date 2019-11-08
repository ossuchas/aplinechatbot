import traceback
from flask_restful import Resource
from flask import request

from models.chatbot_mst_user import MstUserModel
from schemas.chatbot_mst_user import MstUserSchema


user_schema = MstUserSchema()
user_list_schema = MstUserSchema(many=True)


class ChatBotMstUser(Resource):
    @classmethod
    def get(cls, _user_token_id: str):
        user = MstUserModel.find_by_token_id(_user_token_id)
        if user:
            return user_schema.dump(user), 200

        return {"message": "No Data Found"}, 404


