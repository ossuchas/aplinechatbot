import os
import re
import requests
import json
from config import LINE_API


def replyMsg(reply_token, text_msg, line_aceess_token):
    authorization = 'Bearer {}'.format(line_aceess_token)
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization': authorization
    }

    # print(type(test_dict))

    # data = {
    #     "replyToken": reply_token,
    #     "messages": [{
    #         "type": "text",
    #         "text": textMessage
    #     }]
    # }

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
                                "text": "Register Chatbot App.",
                                "color": "#FFFFFF",
                                "size": "lg"
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
                                        "type": "text",
                                        "text": "You are not authorized to access",
                                        "margin": "sm",
                                        "align": "center",
                                        "color": "#808080"
                                    },
                                    {
                                        "type": "text",
                                        "text": "Please register to access",
                                        "margin": "sm",
                                        "align": "center",
                                        "color": "#808080"
                                    },
                                    {
                                        "type": "text",
                                        "text": "CRM Line Chatbot",
                                        "align": "center",
                                        "size": "md",
                                        "margin": "sm",
                                        "color": "#808080"
                                    }
                                ]
                            },
                            {
                                "type": "separator",
                                "margin": "md"
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "Register",
                                        "align": "center",
                                        "size": "lg",
                                        "weight": "bold",
                                        "color": "#2F41EB",
                                        "action": {
                                            "type": "uri",
                                            "label": "action",
                                            "uri": "https://liff.line.me/1653377835-peowRY0O"
                                        }
                                    }
                                ],
                                "margin": "sm"
                            }
                        ]
                    },
                    "footer": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "text",
                                "text": "Copyright 2019 AP (Thailand) PCL.",
                                "align": "center",
                                "size": "xs",
                                "color": "#FFFFFF"
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
                                "height": "30px",
                                "width": "32px",
                                "offsetBottom": "3px"
                            }
                        ]
                    },
                    "styles": {
                        "header": {
                            "backgroundColor": "#000000"
                        },
                        "footer": {
                            "backgroundColor": "#000000"
                        }
                    }
                }
        }
    # type_msg = {
    #     "type": "text",
    #     "text": text_msg
    # }

    data = {
        "replyToken": reply_token,
        "messages": [
            type_msg
        ]
    }

    session = requests.Session()
    response = session.post(LINE_API, data=json.dumps(data), headers=headers)
    return 201
