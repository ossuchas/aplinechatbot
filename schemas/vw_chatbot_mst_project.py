from ma import ma
from models.vw_chatbot_mst_project import MstProjectModel


class MstProjectSchema(ma.ModelSchema):
    class Meta:
        model = MstProjectModel
