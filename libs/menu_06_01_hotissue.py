# -*- coding: utf-8 -*-

import requests
import json
from config import LINE_API


def replyMsg(Reply_token: str =None, bg: str = None, line_Acees_Token: str = None):
    authorization = 'Bearer {}'.format(line_Acees_Token)
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization': authorization
    }

    type_msg = \
        {
            "type": "flex",
            "altText": "Flex Message",
            "contents":
                {
                    "type": "bubble",
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                    {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                            {
                                                "type": "image",
                                                "url": "https://i.ibb.co/stkd5R9/Untitled-1.png",
                                                "size": "full",
                                                "aspectMode": "cover",
                                                "gravity": "center",
                                                "aspectRatio": "30:9",
                                                "action": {
                                                    "type": "message",
                                                    "label": "action",
                                                    "text": "ตรวจสอบค่า PM 2.5"
                                                }
                                            },
                                            {
                                                "type": "separator",
                                                "margin": "sm"
                                            },
                                            {
                                                "type": "image",
                                                "url": "https://i.ibb.co/k1YS4Sh/virus-10.png",
                                                "size": "full",
                                                "aspectMode": "cover",
                                                "aspectRatio": "30:9",
                                                "gravity": "center",
                                                "action": {
                                                    "type": "message",
                                                    "label": "action",
                                                    "text": "ไวรัสโคโรนา"
                                                }
                                            }
                                        ],
                                        "flex": 1
                                    }
                                ]
                            }
                        ],
                        "paddingAll": "0px"
                    }
                }
        }

    data = {
        "replyToken": Reply_token,
        "messages": [
            type_msg
        ]
    }

    session = requests.Session()
    response = session.post(LINE_API, data=json.dumps(data), headers=headers)
    return 201