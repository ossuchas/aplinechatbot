import os
import re
import requests
import json
from config import LINE_API


def replyMsg(reply_token: str = None, text_msg: str = None, line_aceess_token: str = None):
    authorization = 'Bearer {}'.format(line_aceess_token)
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
                    "hero": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "text",
                                "text": "Sale Summary Report by BG",
                                "offsetTop": "10%",
                                "offsetStart": "7%",
                                "color": "#5D6860",
                                "size": "md",
                                "weight": "bold",
                                "decoration": "none"
                            }
                        ]
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "image",
                                "url": "https://i.ibb.co/n1h9L0t/flex-m1-f1-SDH-v1.png",
                                "size": "full",
                                "aspectRatio": "24:7",
                                "action": {
                                    "type": "message",
                                    "label": "action",
                                    "text": "ยอดขายเดือนนี้"
                                }
                            },
                            {
                                "type": "image",
                                "url": "https://i.ibb.co/HqfWYHF/flex-m1-f2-TH-v1.png",
                                "size": "full",
                                "aspectRatio": "24:7",
                                "offsetTop": "3%",
                                "action": {
                                    "type": "message",
                                    "label": "action",
                                    "text": "ยอดขายเดือนที่แล้ว"
                                }
                            },
                            {
                                "type": "image",
                                "url": "https://i.ibb.co/fXgfvM6/flex-m1-f3-CD1-v1.png",
                                "aspectRatio": "24:7",
                                "size": "full",
                                "offsetTop": "7%",
                                "action": {
                                    "type": "message",
                                    "label": "action",
                                    "text": "ยอดขายเดือนนี้"
                                }
                            },
                            {
                                "type": "image",
                                "url": "https://i.ibb.co/x7zn2fp/flex-m1-f4-CD2-v1.png",
                                "size": "full",
                                "aspectRatio": "24:7",
                                "offsetTop": "10%",
                                "action": {
                                    "type": "message",
                                    "label": "action",
                                    "text": "ยอดขายเดือนที่แล้ว"
                                }
                            }
                        ],
                        "offsetTop": "-10px",
                        "cornerRadius": "40px",
                        "borderWidth": "2px"
                    }
                }

        }

    # type_msg = \
    #     {
    #         "type": "flex",
    #         "altText": "Flex Message",
    #         "contents": {
    #             "type": "bubble",
    #             "direction": "ltr",
    #             "body": {
    #                 "type": "box",
    #                 "layout": "vertical",
    #                 "contents": [
    #                     {
    #                         "type": "image",
    #                         "url": "https://i.ibb.co/1fZ7fWk/banner-d-v1.png",
    #                         "margin": "xxl",
    #                         "align": "end",
    #                         "gravity": "center",
    #                         "size": "full",
    #                         "aspectRatio": "1.91:1",
    #                         "aspectMode": "fit",
    #                         "action": {
    #                             "type": "message",
    #                             "text": "ยอดขายเดือนนี้"
    #                         }
    #                     },
    #                     {
    #                         "type": "image",
    #                         "url": "https://i.ibb.co/6n52fjT/banner-d-v2.png",
    #                         "margin": "none",
    #                         "align": "center",
    #                         "gravity": "top",
    #                         "size": "full",
    #                         "aspectRatio": "1.91:1",
    #                         "aspectMode": "fit",
    #                         "action": {
    #                             "type": "message",
    #                             "text": "ยอดขายเดือนที่แล้ว"
    #                         }
    #                     }
    #                 ]
    #             },
    #             "footer": {
    #                 "type": "box",
    #                 "layout": "horizontal",
    #                 "spacing": "none",
    #                 "margin": "none",
    #                 "contents": [
    #                     {
    #                         "type": "image",
    #                         "url": "https://i.ibb.co/k2cx9jL/AP-Logo-2018.png",
    #                         "margin": "none",
    #                         "align": "end",
    #                         "gravity": "bottom",
    #                         "size": "xxs",
    #                         "aspectRatio": "4:3",
    #                         "action": {
    #                             "type": "uri",
    #                             "uri": "https://www.apthai.com/th/home"
    #                         }
    #                     }
    #                 ]
    #             }
    #         }
    #     }

    data = {
        "replyToken": reply_token,
        "messages": [
            type_msg
        ]
    }

    session = requests.Session()
    response = session.post(LINE_API, data=json.dumps(data), headers=headers)
    return 201
