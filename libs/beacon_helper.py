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

    # type_msg = {
    #     "type": "text",
    #     "text": text_msg
    # }
    type_msg = \
        {
            "type": "flex",
            "altText": "Flex Message",
            "contents": {
                "type": "bubble",
                "hero": {
                    "type": "image",
                    "url": "https://images.pexels.com/photos/220453/pexels-photo-220453.jpeg",
                    "align": "start",
                    "size": "full",
                    "aspectRatio": "4:3",
                    "aspectMode": "cover",
                    "action": {
                        "type": "uri",
                        "label": "Action",
                        "uri": "https://linecorp.com"
                    }
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "md",
                    "action": {
                        "type": "uri",
                        "label": "Action",
                        "uri": "https://linecorp.com"
                    },
                    "contents": [
                        {
                            "type": "text",
                            "text": "Mr. Suchat S.",
                            "size": "xl",
                            "weight": "bold",
                            "wrap": True
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "spacing": "sm",
                            "contents": [
                                {
                                    "type": "box",
                                    "layout": "baseline",
                                    "contents": [
                                        {
                                            "type": "icon",
                                            "url": "https://image.flaticon.com/icons/svg/590/590474.svg"
                                        },
                                        {
                                            "type": "text",
                                            "text": "Date Of Birth",
                                            "flex": 0,
                                            "margin": "sm",
                                            "weight": "bold"
                                        },
                                        {
                                            "type": "text",
                                            "text": "14 Oct 1983",
                                            "size": "sm",
                                            "align": "end",
                                            "color": "#AAAAAA"
                                        }
                                    ]
                                },
                                {
                                    "type": "box",
                                    "layout": "baseline",
                                    "contents": [
                                        {
                                            "type": "icon",
                                            "url": "https://image.flaticon.com/icons/svg/747/747310.svg"
                                        },
                                        {
                                            "type": "text",
                                            "text": "Date Of Hired",
                                            "flex": 0,
                                            "margin": "sm",
                                            "weight": "bold"
                                        },
                                        {
                                            "type": "text",
                                            "text": "2 Jan 2019",
                                            "size": "sm",
                                            "align": "end",
                                            "color": "#AAAAAA"
                                        }
                                    ]
                                }
                            ]
                        },
                        {
                            "type": "text",
                            "text": "Assistant Team Leader: IT Business Analysis",
                            "size": "sm",
                            "color": "#AAAAAA",
                            "wrap": True
                        }
                    ]
                }
            }
        }
    # type_msg = \
    #     {
    #         "type": "flex",
    #         "altText": "Flex Message",
    #         "contents":
    #             {
    #                 "type": "bubble",
    #                 "header": {
    #                     "type": "box",
    #                     "layout": "vertical",
    #                     "contents": [
    #                         {
    #                             "type": "box",
    #                             "layout": "horizontal",
    #                             "contents": [
    #                                 {
    #                                     "type": "image",
    #                                     "url": "https://scdn.line-apps.com/n/channel_devcenter/img/flexsnapshot/clip/clip4.jpg",
    #                                     "size": "full",
    #                                     "aspectMode": "cover",
    #                                     "aspectRatio": "150:196",
    #                                     "gravity": "center",
    #                                     "flex": 1
    #                                 },
    #                                 {
    #                                     "type": "box",
    #                                     "layout": "vertical",
    #                                     "contents": [
    #                                         {
    #                                             "type": "image",
    #                                             "url": "https://scdn.line-apps.com/n/channel_devcenter/img/flexsnapshot/clip/clip5.jpg",
    #                                             "size": "full",
    #                                             "aspectMode": "cover",
    #                                             "aspectRatio": "150:98",
    #                                             "gravity": "center"
    #                                         },
    #                                         {
    #                                             "type": "image",
    #                                             "url": "https://scdn.line-apps.com/n/channel_devcenter/img/flexsnapshot/clip/clip6.jpg",
    #                                             "size": "full",
    #                                             "aspectMode": "cover",
    #                                             "aspectRatio": "150:98",
    #                                             "gravity": "center"
    #                                         }
    #                                     ],
    #                                     "flex": 1
    #                                 },
    #                                 {
    #                                     "type": "box",
    #                                     "layout": "horizontal",
    #                                     "contents": [
    #                                         {
    #                                             "type": "text",
    #                                             "text": "NEW",
    #                                             "size": "xs",
    #                                             "color": "#ffffff",
    #                                             "align": "center",
    #                                             "gravity": "center"
    #                                         }
    #                                     ],
    #                                     "backgroundColor": "#EC3D44",
    #                                     "paddingAll": "2px",
    #                                     "paddingStart": "4px",
    #                                     "paddingEnd": "4px",
    #                                     "flex": 0,
    #                                     "position": "absolute",
    #                                     "offsetStart": "18px",
    #                                     "offsetTop": "18px",
    #                                     "cornerRadius": "100px",
    #                                     "width": "48px",
    #                                     "height": "25px"
    #                                 }
    #                             ]
    #                         }
    #                     ],
    #                     "paddingAll": "0px"
    #                 },
    #                 "body": {
    #                     "type": "box",
    #                     "layout": "vertical",
    #                     "contents": [
    #                         {
    #                             "type": "box",
    #                             "layout": "vertical",
    #                             "contents": [
    #                                 {
    #                                     "type": "box",
    #                                     "layout": "vertical",
    #                                     "contents": [
    #                                         {
    #                                             "type": "text",
    #                                             "contents": [],
    #                                             "size": "xl",
    #                                             "wrap": "true",
    #                                             "text": "Mr.Suchat Sujalarnlap",
    #                                             "color": "#ffffff",
    #                                             "weight": "bold"
    #                                         },
    #                                         {
    #                                             "type": "text",
    #                                             "text": "3 Bedrooms, ¥35,000",
    #                                             "color": "#ffffffcc",
    #                                             "size": "sm"
    #                                         }
    #                                     ],
    #                                     "spacing": "sm"
    #                                 },
    #                                 {
    #                                     "type": "box",
    #                                     "layout": "vertical",
    #                                     "contents": [
    #                                         {
    #                                             "type": "box",
    #                                             "layout": "vertical",
    #                                             "contents": [
    #                                                 {
    #                                                     "type": "text",
    #                                                     "contents": [],
    #                                                     "size": "sm",
    #                                                     "wrap": "true",
    #                                                     "margin": "lg",
    #                                                     "color": "#ffffffde",
    #                                                     "text": "Private Pool, Delivery box, Floor heating, Private Cinema"
    #                                                 }
    #                                             ]
    #                                         }
    #                                     ],
    #                                     "paddingAll": "13px",
    #                                     "backgroundColor": "#ffffff1A",
    #                                     "cornerRadius": "2px",
    #                                     "margin": "xl"
    #                                 }
    #                             ]
    #                         }
    #                     ],
    #                     "paddingAll": "20px",
    #                     "backgroundColor": "#464F69"
    #                 }
    #             }
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
