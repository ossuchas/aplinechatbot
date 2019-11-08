from ma import ma
from models.chatbot_mst_user import MstUserModel


class MstUserSchema(ma.ModelSchema):
    class Meta:
        model = MstUserModel
