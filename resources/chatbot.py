import traceback
from flask_restful import Resource
from flask import request


class ChatBot(Resource):
    @classmethod
    def get(cls):
        return {"message": "Hello World"}, 200


class ChatBotRegister(Resource):
    @classmethod
    def post(cls):
        try:
            return {"message": "Save Successfully"}, 201
        except:
            return {"message": "Failed to Save"}, 500
