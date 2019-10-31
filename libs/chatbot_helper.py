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
    val = r"฿ 3,588M"
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
                            "text": "Accumulate Sales Oct'19",
                            "size": "lg",
                            "align": "start",
                            "weight": "bold",
                            "color": "#C92028"
                        },
                        {
                            "type": "text",
                            "text": val,
                            "size": "3xl",
                            "weight": "bold",
                            "color": "#000000"
                        },
                        {
                            "type": "text",
                            "text": "Total Gross Sale",
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
                            "text": "All Project @APTHAI",
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
                                    "text": "Gross Sales",
                                    "color": "#C3C3C3"
                                },
                                {
                                    "type": "text",
                                    "text": "฿ 3,519,894,522",
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
                                    "text": "Cancel",
                                    "color": "#C3C3C3"
                                },
                                {
                                    "type": "text",
                                    "text": "฿ 1,729,575,441",
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
                                    "text": "Agreement",
                                    "color": "#C3C3C3"
                                },
                                {
                                    "type": "text",
                                    "text": "฿ 2,846,496,260",
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
                                    "text": "Transfer",
                                    "color": "#C3C3C3"
                                },
                                {
                                    "type": "text",
                                    "text": "฿ 1,364,440,307",
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
