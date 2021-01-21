# -*- coding: utf-8 -*-

import requests
import json
from config import LINE_API

from models.chatbot_mst_conf import MstMsgConfigModel
from schemas.chatbot_mst_conf import MstMsgConfSchema


def replyMsg(Reply_token: str = None, line_Acees_Token: str = None):
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
                    # "size": "giga",
                    "hero": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "text",
                                "text": "Please select period",
                                "color": "#FFFFFF",
                                "offsetStart": "5%"
                            }
                        ]
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
                                        "type": "box",
                                        "layout": "horizontal",
                                        "contents": [
                                            {
                                                "type": "box",
                                                "layout": "vertical",
                                                "contents": [
                                                    {
                                                        "type": "text",
                                                        "text": "Actual Income",
                                                        "weight": "bold",
                                                        "style": "normal",
                                                        "size": "xl",
                                                        "align": "center",
                                                        "gravity": "center",
                                                        "color": "#FFFFFF"
                                                    },
                                                    {
                                                        "type": "image",
                                                        "url": "https://i.ibb.co/1M4dwWq/calendar-y2d-v1-0.png",
                                                        "size": "full",
                                                        "aspectRatio": "24:7",
                                                        "aspectMode": "fit",
                                                        "action": {
                                                            "type": "message",
                                                            "label": "action",
                                                            "text": "Actual Income Period Y2D"
                                                        }
                                                    },
                                                    {
                                                        "type": "image",
                                                        "url": "https://i.ibb.co/71TKZLp/calendar-daily-v1-0.png",
                                                        "size": "full",
                                                        "aspectRatio": "24:7",
                                                        "aspectMode": "fit",
                                                        "action": {
                                                            "type": "message",
                                                            "label": "action",
                                                            "text": "Actual Income Daily"
                                                        }
                                                    }
                                                ]
                                            }
                                        ],
                                        "backgroundColor": "#6F807C"
                                    }
                                ]
                            },
                            {
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
                                                        "type": "text",
                                                        "text": "Booking",
                                                        "size": "xl",
                                                        "color": "#FFFFFF",
                                                        "weight": "bold",
                                                        "align": "center",
                                                        "gravity": "center"
                                                    },
                                                    {
                                                        "type": "image",
                                                        "url": "https://i.ibb.co/1M4dwWq/calendar-y2d-v1-0.png",
                                                        "size": "full",
                                                        "aspectMode": "fit",
                                                        "aspectRatio": "24:7",
                                                        "action": {
                                                            "type": "message",
                                                            "label": "action",
                                                            "text": "Booking Period Y2D"
                                                        }
                                                    }
                                                ]
                                            }
                                        ],
                                        "backgroundColor": "#498073"
                                    }
                                ],
                                "margin": "md"
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


def replyMsgDB(Reply_token: str = None, line_Acees_Token: str = None, msg_value: str = None,
               user_type: str = None, user_position: str = None):

    authorization = f"Bearer {line_Acees_Token}"
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization': authorization
    }

    if user_position == 'IT':
        user_type = 'IT'

    msg = MstMsgConfigModel.find_by_msg_value_ds(msg_value, user_type)
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
