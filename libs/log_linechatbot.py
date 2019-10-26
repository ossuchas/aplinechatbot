from models.log_linechatbot import LogChatBotModel
from schemas.log_linechatbot import LogChatBotSchema


def savechatlog2db(replyToken: str = None,
                   source_userId: str = None,
                   source_type: str = None,
                   timestamps: str = None,
                   message_type: str = None,
                   message_text: str = None,
                   stickerId: str = None,
                   packageId: str = None) -> int:

    models = LogChatBotModel()

    models.replyToken = replyToken
    models.source_userId = source_userId
    models.source_type = source_type
    models.timestamps = timestamps
    models.message_type = message_type
    models.message_text = message_text
    models.stickerId = stickerId
    models.packageId = packageId

    models.save_to_db()

    return 200