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
                                        "url": "https://i.ibb.co/0V8ShdH/menu-01-q-v2-0.png",
                                        "size": "full",
                                        "aspectMode": "fit",
                                        "aspectRatio": "24:7",
                                        "offsetBottom": "3px",
                                        "action": {
                                            "type": "message",
                                            "label": "action",
                                            "text": "LL ALLBG Period Quarter"
                                        }
                                    }
                                ],
                                "backgroundColor": "#FFFFFF",
                                "borderWidth": "2px",
                                "margin": "xs"
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "image",
                                        "url": "https://i.ibb.co/NNh4k7r/menu-01-m-v2-0.png",
                                        "size": "full",
                                        "aspectMode": "fit",
                                        "aspectRatio": "24:7",
                                        "offsetBottom": "3px",
                                        "action": {
                                            "type": "message",
                                            "label": "action",
                                            "text": "LL ALLBG Period Month"
                                        }
                                    }
                                ],
                                "margin": "xs",
                                "backgroundColor": "#FFFFFF",
                                "borderWidth": "2px",
                                "borderColor": "#FFFFFF"
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "image",
                                        "size": "full",
                                        "aspectRatio": "24:7",
                                        "aspectMode": "fit",
                                        "offsetBottom": "3px",
                                        "url": "https://i.ibb.co/S6FY0Gs/menu-01-w-v2-0.png",
                                        "action": {
                                            "type": "message",
                                            "label": "action",
                                            "text": "LL ALLBG Period Week"
                                        }
                                    }
                                ],
                                "margin": "xs",
                                "backgroundColor": "#FFFFFF",
                                "borderColor": "#FFFFFF",
                                "borderWidth": "2px"
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "image",
                                        "url": "https://i.ibb.co/5hP4wLH/menu-01-d-v2-0.png",
                                        "size": "full",
                                        "aspectRatio": "24:7",
                                        "aspectMode": "fit",
                                        "offsetBottom": "3px",
                                        "action": {
                                            "type": "message",
                                            "label": "action",
                                            "text": "LL ALLBG Period Yesterday"
                                        }
                                    }
                                ],
                                "borderWidth": "2px",
                                "backgroundColor": "#FFFFFF",
                                "borderColor": "#FFFFFF",
                                "margin": "xs"
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "image",
                                        "url": "https://i.ibb.co/Jy1FgHD/menu-01-y2d-v2-0.png",
                                        "size": "full",
                                        "aspectMode": "fit",
                                        "aspectRatio": "24:7",
                                        "offsetBottom": "3px",
                                        "action": {
                                            "type": "message",
                                            "label": "action",
                                            "text": "LL ALLBG Period As of Current"
                                        }
                                    }
                                ],
                                "backgroundColor": "#FFFFFF",
                                "borderWidth": "2px",
                                "borderColor": "#FFFFFF",
                                "margin": "xs"
                            }
                        ],
                        "backgroundColor": "#c92028"
                    },
                    "footer": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "text",
                                "text": "Copyright 2019 AP (Thailand) PCL.",
                                "color": "#FFFFFF",
                                "size": "xxs",
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
                                "offsetStart": "7px",
                                "offsetBottom": "3px",
                                "offsetTop": "1px"
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
