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
                                "layout": "horizontal",
                                "contents": [
                                    {
                                        "type": "image",
                                        "url": "https://i.ibb.co/4Tw4wgJ/calendar-q-v1-0.png",
                                        "aspectRatio": "1:1",
                                        "aspectMode": "fit",
                                        "action": {
                                            "type": "message",
                                            "label": "action",
                                            "text": "LL Period BY BG Quarter [{}]".format(bg)
                                        }
                                    },
                                    {
                                        "type": "image",
                                        "url": "https://i.ibb.co/R71C8Q6/calendar-m-v1-0.png",
                                        "action": {
                                            "type": "message",
                                            "label": "action",
                                            "text": "LL Period BY BG Month [{}]".format(bg)
                                        }
                                    }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                    {
                                        "type": "image",
                                        "url": "https://i.ibb.co/Pg8X4RG/calendar-w-v1-0.png",
                                        "action": {
                                            "type": "message",
                                            "label": "action",
                                            "text": "LL Period BY BG Week [{}]".format(bg)
                                        }
                                    },
                                    {
                                        "type": "image",
                                        "url": "https://i.ibb.co/8m6TFfb/calendar-y-v1-0.png",
                                        "action": {
                                            "type": "message",
                                            "label": "action",
                                            "text": "LL Period BY BG Yesterday [{}]".format(bg)
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
                                        "url": "https://i.ibb.co/6B7wwDn/calendar-y2d-v3-0.png",
                                        "size": "full",
                                        "aspectMode": "fit",
                                        "aspectRatio": "24:7",
                                        "action": {
                                            "type": "message",
                                            "label": "action",
                                            "text": "LL Period BY BG As of Current [{}]".format(bg)
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
