from ma import ma
from models.chatbot_mst_conf import MstMsgConfigModel


class MstMsgConfSchema(ma.ModelSchema):
    class Meta:
        model = MstMsgConfigModel
