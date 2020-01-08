import traceback
from flask_restful import Resource
from flask import request

from models.vw_crm_line_userroleproj import UserRoleProjModel
from schemas.vw_crm_line_userroleproj2 import UserRoleProj2Schema


projrole2_list_schema = UserRoleProj2Schema(many=True)


class UserRoleProject2(Resource):
    @classmethod
    def get(cls, userid: str):
        projs = UserRoleProjModel.find_by_userid(userid)
        if projs:
            return projrole2_list_schema.dump(projs), 200

        return {"message": "No Data Found"}, 404
