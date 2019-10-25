import os
import re
from requests import Response, post
import json
from config import *

# LINE_API = os.environ.get("LINE_API")

def replyMsg(Reply_token, TextMessage, Line_Acees_Token):
    # LINE_API = 'https://api.line.me/v2/bot/message/reply'
    print(LINE_API)

    Authorization = 'Bearer {}'.format(Line_Acees_Token)
    print(Authorization)
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization': Authorization
    }

    data = {
        "replyToken": Reply_token,
        "messages": [{
            "type": "text",
            "text": TextMessage + "1234"
        }]
    }
    # print(data)

    #data = json.dumps(data)
    # print(data)
    # r = requests.post(LINE_API, headers=headers, data=data)
    response = post(LINE_API, data=json.dumps(data), headers=headers)
    return 200
