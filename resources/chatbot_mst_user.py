import traceback
from flask_restful import Resource
from flask import request
from datetime import datetime


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


class ChatBotMstUserList(Resource):
    @classmethod
    def get(cls):
        user = MstUserModel.find_user_listrole()
        if user:
            return user_list_schema.dump(user), 200

        return {"message": "No Data Found"}, 404


class ChatBotMstUserRole(Resource):
    @classmethod
    def put(cls, _user_empcode: str):
        item_json = request.get_json()
        user = MstUserModel.find_by_empcode(_user_empcode)

        if user:
            user.user_type = item_json["user_type"]
            user.user_sub_no = item_json["user_sub_no"]
            user.modifydate = datetime.today()
            user.modifyby = "api_updaterole"
        else:
            return {"message": "Can not find Employee Code for update"}, 404

        user.save_to_db()

        return user_schema.dump(user), 200


