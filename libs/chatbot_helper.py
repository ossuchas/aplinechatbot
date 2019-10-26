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

    data = {
        "replyToken": Reply_token,
        "messages": [{
            "type": "text",
            "text": TextMessage
        }]
    }


    session = requests.Session()
    response = session.post(LINE_API, data=json.dumps(data), headers=headers)
    return response
