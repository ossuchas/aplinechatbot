from ma import ma
from models.log_linechatbot import LogChatBotModel


class LogChatBotSchema(ma.ModelSchema):
    class Meta:
        model = LogChatBotModel
