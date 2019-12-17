import traceback
from flask_restful import Resource
from flask import request
import json

from libs.ap_authen import APAuthen, APAuthenException


class UserLogin(Resource):
    @classmethod
    def post(cls):
        user_json = request.get_json()
        try:
            response = APAuthen.ap_authen(user_json["username"], user_json["password"], "CRM")
            return {"message": "Successful Authentication"}, 200
            # return json.loads(response.content), 200
        except APAuthenException as e:
            return {"message": str(e)}, 401
        except:
            traceback.print_exc()
            return {"message": "Login Failed"}, 500
