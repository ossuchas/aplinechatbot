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
    type_msg = {
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
          "text": "Header",
          "align": "center"
        }
      ]
    },
    "hero": {
      "type": "image",
      "url": "https://developers.line.biz/assets/images/services/bot-designer-icon.png",
      "size": "full",
      "aspectRatio": "1.51:1",
      "aspectMode": "fit"
    },
    "body": {
      "type": "box",
      "layout": "vertical",
      "contents": [
        {
          "type": "text",
          "text": "Body",
          "align": "center"
        }
      ]
    },
    "footer": {
      "type": "box",
      "layout": "horizontal",
      "contents": [
        {
          "type": "button",
          "action": {
            "type": "uri",
            "label": "Button",
            "uri": "https://linecorp.com"
          }
        }
      ]
    },
    "styles": {
      "header": {
        "backgroundColor": "#4E0F0F"
      },
      "hero": {
        "backgroundColor": "#F4F4F4"
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
    return response
