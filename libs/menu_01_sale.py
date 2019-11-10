import os
import re
import requests
import json
from config import LINE_API


def replyMsg(reply_token: str = None, text_msg: str = None, line_aceess_token: str = None):
    authorization = 'Bearer {}'.format(line_aceess_token)
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization': authorization
    }

    type_msg = \
        {
            "type": "flex",
            "altText": "Flex Message",
            "contents": {
                "type": "bubble",
                "direction": "ltr",
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "image",
                            "url": "https://i.ibb.co/1fZ7fWk/banner-d-v1.png",
                            "margin": "xxl",
                            "align": "end",
                            "gravity": "center",
                            "size": "full",
                            "aspectRatio": "1.91:1",
                            "aspectMode": "fit",
                            "action": {
                                "type": "message",
                                "text": "ยอดขายเดือนนี้"
                            }
                        },
                        {
                            "type": "image",
                            "url": "https://i.ibb.co/6n52fjT/banner-d-v2.png",
                            "margin": "none",
                            "align": "center",
                            "gravity": "top",
                            "size": "full",
                            "aspectRatio": "1.91:1",
                            "aspectMode": "fit",
                            "action": {
                                "type": "message",
                                "text": "ยอดขายเดือนที่แล้ว"
                            }
                        }
                    ]
                },
                "footer": {
                    "type": "box",
                    "layout": "horizontal",
                    "spacing": "none",
                    "margin": "none",
                    "contents": [
                        {
                            "type": "image",
                            "url": "https://i.ibb.co/k2cx9jL/AP-Logo-2018.png",
                            "margin": "none",
                            "align": "end",
                            "gravity": "bottom",
                            "size": "xxs",
                            "aspectRatio": "4:3",
                            "action": {
                                "type": "uri",
                                "uri": "https://www.apthai.com/th/home"
                            }
                        }
                    ]
                }
            }
        }

    data = {
        "replyToken": reply_token,
        "messages": [
            type_msg
        ]
    }

    session = requests.Session()
    response = session.post(LINE_API, data=json.dumps(data), headers=headers)
    return 201
