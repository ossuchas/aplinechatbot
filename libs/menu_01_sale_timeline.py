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
            "contents":
                {
                    "type": "bubble",
                    "header": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "text",
                                "text": "ช่วงเวลาที่ท่านสนใจ",
                                "size": "lg",
                                "color": "#5DA2FF"
                            }
                        ],
                        "paddingAll": "5px",
                        "paddingStart": "20px"
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "image",
                                        "url": "https://i.ibb.co/R4mBxTs/flex-m1-m1-f1-SDH-v2.png",
                                        "size": "full",
                                        "aspectRatio": "4:1",
                                        "action": {
                                            "type": "message",
                                            "label": "action",
                                            "text": "ยอดขายเดือนที่แล้ว"
                                        }
                                    }
                                ],
                                "backgroundColor": "#FFFFFF"
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "image",
                                        "url": "https://i.ibb.co/zPQjLHV/flex-m1-m2-f1-SDH-v1.png",
                                        "size": "full",
                                        "aspectRatio": "4:1",
                                        "action": {
                                            "type": "message",
                                            "label": "action",
                                            "text": "ยอดขายเดือนนี้"
                                        }
                                    }
                                ],
                                "backgroundColor": "#FFFFFF",
                                "offsetTop": "3px"
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "image",
                                        "url": "https://i.ibb.co/yyFg20V/flex-m1-m3-f1-SDH-v1.png",
                                        "size": "full",
                                        "aspectRatio": "4:1",
                                        "action": {
                                            "type": "message",
                                            "label": "action",
                                            "text": "ยอดขายสัปดาห์ที่แล้ว"
                                        }
                                    }
                                ],
                                "backgroundColor": "#FFFFFF",
                                "offsetTop": "6px"
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "image",
                                        "url": "https://i.ibb.co/tHPs8bd/flex-m1-m4-f1-SDH-v1.png",
                                        "size": "full",
                                        "aspectRatio": "4:1",
                                        "action": {
                                            "type": "message",
                                            "label": "action",
                                            "text": "ยอดขายล่าสุด"
                                        }
                                    }
                                ],
                                "backgroundColor": "#FFFFFF",
                                "offsetTop": "9px"
                            },
                            {
                                "type": "image",
                                "url": "https://image.flaticon.com/icons/svg/148/148841.svg",
                                "position": "absolute",
                                "size": "xxs",
                                "aspectRatio": "4:3",
                                "offsetStart": "83%",
                                "offsetTop": "10px"
                            }
                        ]
                    },
                    "styles": {
                        "body": {
                            "backgroundColor": "#FF5547"
                        }
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
