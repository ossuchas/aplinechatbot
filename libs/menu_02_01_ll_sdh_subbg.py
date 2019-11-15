# -*- coding: utf-8 -*-

import requests
import json
from config import LINE_API


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
                    "header": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                    {
                                        "type": "image",
                                        "url": "https://scdn.line-apps.com/n/channel_devcenter/img/flexsnapshot/clip/clip4.jpg",
                                        "size": "full",
                                        "aspectMode": "cover",
                                        "aspectRatio": "150:294",
                                        "gravity": "center",
                                        "flex": 1,
                                        "action": {
                                            "type": "message",
                                            "label": "action",
                                            "text": "กรุณาระบุเลือก Sub BG ที่สนใจข้อมูล"
                                        }
                                    },
                                    {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                            {
                                                "type": "image",
                                                "url": "https://i.ibb.co/3TWwMcJ/menu-02-01-subbg-v1-0.png",
                                                "size": "full",
                                                "aspectMode": "cover",
                                                "aspectRatio": "150:98",
                                                "gravity": "center",
                                                "action": {
                                                    "type": "message",
                                                    "label": "action",
                                                    "text": "ยอด LL SDH Sub 1.1"
                                                }
                                            },
                                            {
                                                "type": "image",
                                                "url": "https://i.ibb.co/gyrMbjD/menu-02-02-subbg-v1-0.png",
                                                "size": "full",
                                                "aspectMode": "cover",
                                                "aspectRatio": "150:98",
                                                "gravity": "center",
                                                "action": {
                                                    "type": "message",
                                                    "label": "action",
                                                    "text": "ยอด LL SDH Sub 1.2"
                                                }
                                            },
                                            {
                                                "type": "image",
                                                "url": "https://i.ibb.co/x7JyQCZ/menu-02-03-subbg-v1-0.png",
                                                "gravity": "center",
                                                "size": "full",
                                                "aspectMode": "cover",
                                                "aspectRatio": "150:98",
                                                "action": {
                                                    "type": "message",
                                                    "label": "action",
                                                    "text": "ยอด LL SDH Sub 1.3"
                                                }
                                            }
                                        ],
                                        "flex": 1
                                    },
                                    {
                                        "type": "box",
                                        "layout": "horizontal",
                                        "contents": [
                                            {
                                                "type": "image",
                                                "url": "https://i.ibb.co/fS0B4wP/AP-Logo-2018.png",
                                                "size": "lg",
                                                "aspectMode": "fit",
                                                "offsetTop": "10px"
                                            }
                                        ],
                                        "paddingAll": "2px",
                                        "paddingStart": "4px",
                                        "paddingEnd": "4px",
                                        "flex": 0,
                                        "position": "absolute",
                                        "offsetStart": "5%",
                                        "offsetBottom": "45%"
                                    }
                                ]
                            }
                        ],
                        "paddingAll": "0px"
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
                                        "type": "text",
                                        "text": "APTHAI.com",
                                        "color": "#FFFFFF",
                                        "weight": "bold",
                                        "align": "end",
                                        "action": {
                                            "type": "uri",
                                            "label": "action",
                                            "uri": "https://www.apthai.com/th/home",
                                            "altUri": {
                                                "desktop": "https://www.apthai.com/th/home"
                                            }
                                        },
                                        "size": "xxs"
                                    }
                                ],
                                "backgroundColor": "#FFFFFF",
                                "width": "2px",
                                "height": "1px"
                            }
                        ],
                        "backgroundColor": "#FFFFFF",
                        "paddingAll": "5px",
                        "height": "1px"
                    },
                    "footer": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "text",
                                "text": "Copyright 2019 AP (Thailand) PCL.",
                                "size": "xxs",
                                "color": "#FFFFFF",
                                "align": "center"
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
                                "offsetTop": "1px",
                                "offsetBottom": "3px",
                                "offsetStart": "7px"
                            }
                        ],
                        "backgroundColor": "#000000"
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
