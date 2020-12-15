# -*- coding: utf-8 -*-

import requests
import json
from config import LINE_API

from models.chatbot_mst_conf import MstMsgConfigModel
from schemas.chatbot_mst_conf import MstMsgConfSchema


def replyMsg(Reply_token: str =None, TextMessage: str = None, line_Acees_Token: str = None):
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
                    "hero": {
                        "type": "box",
                        "layout": "baseline",
                        "contents": [
                            {
                                "type": "text",
                                "text": "."
                            }
                        ]
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "text",
                                "text": "กรุณาเลือกข้อมูล BG ที่ท่านสนใจ",
                                "size": "sm",
                                "color": "#FFFFFF",
                                "align": "start",
                                "offsetStart": "10px"
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "image",
                                        "url": "https://i.ibb.co/D4QTPdL/bg-banner-bg1-v2.png",
                                        "aspectRatio": "24:7",
                                        "size": "full",
                                        "action": {
                                            "type": "message",
                                            "label": "action",
                                            "text": "LL BY BG SDH"
                                        }
                                    }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "image",
                                        "url": "https://i.ibb.co/BBC9G0d/bg-banner-bg2-v2.png",
                                        "size": "full",
                                        "aspectRatio": "24:7",
                                        "action": {
                                            "type": "message",
                                            "label": "action",
                                            "text": "LL BY BG TH"
                                        }
                                    }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "image",
                                        "url": "https://i.ibb.co/zmLDxB6/bg-banner-bg3-cd1-v2.png",
                                        "size": "full",
                                        "aspectRatio": "24:7",
                                        "action": {
                                            "type": "message",
                                            "label": "action",
                                            "text": "LL BY BG CD1"
                                        }
                                    }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "image",
                                        "url": "https://i.ibb.co/263zbCJ/bg-banner-bg4-cd2-v2.png",
                                        "size": "full",
                                        "aspectRatio": "24:7",
                                        "action": {
                                            "type": "message",
                                            "label": "action",
                                            "text": "LL BY BG CD2"
                                        }
                                    }
                                ]
                            }
                        ]
                    },
                    "footer": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "text",
                                "text": "Copyright 2019 AP PCL.",
                                "size": "xxs",
                                "align": "center",
                                "color": "#ffffff"
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "image",
                                        "url": "https://i.ibb.co/fS0B4wP/AP-Logo-2018.png"
                                    }
                                ],
                                "position": "absolute",
                                "width": "32px",
                                "height": "32px",
                                "offsetBottom": "2px"
                            }
                        ]
                    },
                    "styles": {
                        "hero": {
                            "backgroundColor": "#000000"
                        },
                        "body": {
                            "backgroundColor": "#c92028"
                        },
                        "footer": {
                            "backgroundColor": "#000000"
                        }
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


def replyMsgDB(Reply_token: str = None, TextMessage: str = None, line_Acees_Token: str = None, msg_value: str = None):
    authorization = f"Bearer {line_Acees_Token}"
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization': authorization
    }

    msg = MstMsgConfigModel.find_by_msg_value(msg_value)
    msg_schema = MstMsgConfSchema().dumps(msg)

    msg_obj = json.loads(msg_schema)
    type_msg = json.loads(msg_obj['msg_json'])

    data = {
        "replyToken": Reply_token,
        "messages": [
            type_msg
        ]
    }

    session = requests.Session()
    response = session.post(LINE_API, data=json.dumps(data), headers=headers)
    return response, 201
