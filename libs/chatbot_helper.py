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

    test_dict = [
        {
            "type": "box",
            "layout": "baseline",
            "contents": [
                {
                    "type": "text",
                    "text": "10077: centro",
                    "size": "sm",
                    "flex": 0
                },
                {
                    "type": "text",
                    "text": "1,038,308",
                    "align": "end",
                    "size": "xs",
                    "flex": 1
                },
                {
                    "type": "text",
                    "text": "39",
                    "size": "xs",
                    "align": "end",
                    "flex": 1
                }
            ]
        },
        {
            "type": "box",
            "layout": "baseline",
            "contents": [
                {
                    "type": "text",
                    "text": "10077: centro",
                    "size": "sm",
                    "flex": 0
                },
                {
                    "type": "text",
                    "text": "1,038,308",
                    "align": "end",
                    "size": "xs",
                    "flex": 1
                },
                {
                    "type": "text",
                    "text": "39",
                    "size": "xs",
                    "align": "end",
                    "flex": 1
                }
            ]
        },
        {
            "type": "box",
            "layout": "baseline",
            "contents": [
                {
                    "type": "text",
                    "text": "10077: centro",
                    "size": "sm",
                    "flex": 0
                },
                {
                    "type": "text",
                    "text": "1,038,308",
                    "align": "end",
                    "size": "xs",
                    "flex": 1
                },
                {
                    "type": "text",
                    "text": "39",
                    "size": "xs",
                    "align": "end",
                    "flex": 1
                }
            ]
        }
    ]
    print(type(test_dict))

    # data = {
    #     "replyToken": reply_token,
    #     "messages": [{
    #         "type": "text",
    #         "text": textMessage
    #     }]
    # }

    tmp_str = \
        {
            "type": "flex",
            "altText": "Flex Message",
            "contents": {
                "type": "bubble",
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": test_dict
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
            tmp_str
        ]
    }

    session = requests.Session()
    response = session.post(LINE_API, data=json.dumps(data), headers=headers)
    return 201
