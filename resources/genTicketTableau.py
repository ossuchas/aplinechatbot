import traceback
from flask_restful import Resource
from flask import request
from requests import Response, post
import json
from libs.ap_genticket import APGenTicketTableau, APAuthenException


class GenTicketTableau(Resource):
    @classmethod
    def get(cls):
        # user_json = request.get_json()
        try:
            response = APGenTicketTableau.ap_genticket()
            data = response.json()
            # return {"message": response.text}, 200
            return {"message": data["ticket_value"]}, 200
        except APAuthenException as e:
            return {"message": str(e)}, 401
        except:
            traceback.print_exc()
            return {"message": "Login Failed"}, 500
