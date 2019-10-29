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
                "altText": "this is a buttons template",
                "template": {
                    "type": "buttons",
                    "actions": [
                        {
                            "type": "uri",
                            "label": "go to google",
                            "uri": "http://www.google.com"
                        },
                        {
                            "type": "message",
                            "label": "Action 2",
                            "text": "Action 2"
                        },
                        {
                            "type": "message",
                            "label": "Action 3",
                            "text": "Action 3"
                        }
                    ],
                    "thumbnailImageUrl": "https://sirichaiwatt.com/wp-content/uploads/2018/03/SirichaiwattAtt-01-326x236.jpg",
                    "title": "บทความดีดี สร้างแรงบันดาลใจ",
                    "text": "by suchat_s"
                }
        }]
    }




    session = requests.Session()
    response = session.post(LINE_API, data=json.dumps(data), headers=headers)
    return response
