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
                    "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/01_1_cafe.png",
                    "size": "full",
                    "aspectRatio": "20:13",
                    "aspectMode": "cover",
                    "action": {
                        "type": "uri",
                        "label": "Line",
                        "uri": "https://linecorp.com/"
                    }
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "text",
                            "text": "Brown Cafe",
                            "size": "xl",
                            "weight": "bold"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "margin": "md",
                            "contents": [
                                {
                                    "type": "icon",
                                    "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png",
                                    "size": "sm"
                                },
                                {
                                    "type": "icon",
                                    "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png",
                                    "size": "sm"
                                },
                                {
                                    "type": "icon",
                                    "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png",
                                    "size": "sm"
                                },
                                {
                                    "type": "icon",
                                    "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png",
                                    "size": "sm"
                                },
                                {
                                    "type": "icon",
                                    "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gray_star_28.png",
                                    "size": "sm"
                                },
                                {
                                    "type": "text",
                                    "text": "4.0",
                                    "flex": 0,
                                    "margin": "md",
                                    "size": "sm",
                                    "color": "#999999"
                                }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "spacing": "sm",
                            "margin": "lg",
                            "contents": [
                                {
                                    "type": "box",
                                    "layout": "baseline",
                                    "spacing": "sm",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": "Place",
                                            "flex": 1,
                                            "size": "sm",
                                            "color": "#AAAAAA"
                                        },
                                        {
                                            "type": "text",
                                            "text": "Miraina Tower, 4-1-6 Shinjuku, Tokyo",
                                            "flex": 5,
                                            "size": "sm",
                                            "color": "#666666",
                                            "wrap": True
                                        }
                                    ]
                                },
                                {
                                    "type": "box",
                                    "layout": "baseline",
                                    "spacing": "sm",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": "Time",
                                            "flex": 1,
                                            "size": "sm",
                                            "color": "#AAAAAA"
                                        },
                                        {
                                            "type": "text",
                                            "text": "10:00 - 23:00",
                                            "flex": 5,
                                            "size": "sm",
                                            "color": "#666666",
                                            "wrap": True
                                        }
                                    ]
                                }
                            ]
                        }
                    ]
                },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "flex": 0,
                    "spacing": "sm",
                    "contents": [
                        {
                            "type": "button",
                            "action": {
                                "type": "uri",
                                "label": "CALL",
                                "uri": "https://linecorp.com"
                            },
                            "height": "sm",
                            "style": "link"
                        },
                        {
                            "type": "button",
                            "action": {
                                "type": "uri",
                                "label": "WEBSITE",
                                "uri": "https://linecorp.com"
                            },
                            "height": "sm",
                            "style": "link"
                        },
                        {
                            "type": "spacer",
                            "size": "sm"
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
