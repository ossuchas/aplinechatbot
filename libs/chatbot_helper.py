import os
import re
import requests
import json
from config import LINE_API


def replyMsg(Reply_token, TextMessage, line_Acees_Token):
    authorization = 'Bearer {}'.format(line_Acees_Token)
    # print(authorization)
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization': authorization
    }

    # data = {
    #     "replyToken": Reply_token,
    #     "messages": [{
    #         "type": "text",
    #         "text": TextMessage
    #     }]
    # }
    type_msg = \
        {
            "type": "flex",
            "altText": "Flex Message",
            "contents": {
                "type": "bubble",
                "direction": "ltr",
                "header": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "text",
                            "text": "Daily Sale Report",
                            "size": "lg",
                            "align": "start",
                            "weight": "bold",
                            "color": "#009813"
                        },
                        {
                            "type": "text",
                            "text": "฿ 2,038,038",
                            "size": "3xl",
                            "weight": "bold",
                            "color": "#000000"
                        },
                        {
                            "type": "text",
                            "text": "Gross Sale",
                            "size": "lg",
                            "weight": "bold",
                            "color": "#000000"
                        },
                        {
                            "type": "text",
                            "text": "2019.10.31 12:47 (GMT+0700)",
                            "size": "xs",
                            "color": "#B2B2B2"
                        },
                        {
                            "type": "text",
                            "text": "Life ๑ Wireless (60015)",
                            "margin": "lg",
                            "size": "lg",
                            "color": "#000000"
                        }
                    ]
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "separator",
                            "color": "#C3C3C3"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": "Gross Sale",
                                    "color": "#C3C3C3"
                                },
                                {
                                    "type": "text",
                                    "text": "฿ 2,849,398",
                                    "align": "end"
                                }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": "Walk",
                                    "color": "#C3C3C3"
                                },
                                {
                                    "type": "text",
                                    "text": "99",
                                    "align": "end"
                                }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": "Register",
                                    "color": "#C3C3C3"
                                },
                                {
                                    "type": "text",
                                    "text": "1,038",
                                    "align": "end"
                                }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": "Book",
                                    "color": "#C3C3C3"
                                },
                                {
                                    "type": "text",
                                    "text": "฿ 1,308,308",
                                    "align": "end"
                                }
                            ]
                        },
                        {
                            "type": "separator",
                            "margin": "lg",
                            "color": "#C3C3C3"
                        }
                    ]
                },
                "footer": {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                        {
                            "type": "text",
                            "text": "View Details",
                            "size": "lg",
                            "align": "center",
                            "color": "#0084B6",
                            "action": {
                                "type": "uri",
                                "label": "View Details",
                                "uri": "https://google.co.th/"
                            }
                        }
                    ]
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
    return response
