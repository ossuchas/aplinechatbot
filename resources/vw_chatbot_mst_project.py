import traceback
from flask_restful import Resource
from flask import request

from models.vw_chatbot_mst_project import MstProjectModel
from schemas.vw_chatbot_mst_project import MstProjectSchema


proj_schema = MstProjectSchema()
proj_list_schema = MstProjectSchema(many=True)


class MstProject(Resource):
    @classmethod
    def get(cls):
        proj = MstProjectModel.find_all()
        if proj:
            return proj_list_schema.dump(proj), 200

        return {"message": "No Data Found"}, 404


