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

    data = {
        "replyToken": Reply_token,
        "messages": [{
            "type": "template",
            "altText": "this is a confirm template",
            "template": {
                "type": "confirm",
                "actions": [
                    {
                        "type": "uri",
                        "label": "Yes",
                        "uri": "http://www.google.com"
                    },
                    {
                        "type": "message",
                        "label": "No",
                        "text": "No"
                    }
                ],
                "text": "Continue?"
            }
        }]
    }

    session = requests.Session()
    response = session.post(LINE_API, data=json.dumps(data), headers=headers)
    return response
