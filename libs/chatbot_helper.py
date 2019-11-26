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

    # data = {
    #     "replyToken": reply_token,
    #     "messages": [{
    #         "type": "text",
    #         "text": textMessage
    #     }]
    # }

    # type_msg = {
    #     "type": "text",
    #     "text": text_msg
    # }
    type_msg = \
        {
            "type": "flex",
            "altText": "Flex Message",
            "contents":
                {
                    "type": "bubble",
                    "size": "giga",
                    "hero": {
                        "type": "box",
                        "layout": "baseline",
                        "contents": [
                            {
                                "type": "text",
                                "text": "Lead Lag",
                                "color": "#FFFFFF",
                                "size": "md",
                                "align": "start",
                                "weight": "bold",
                                "offsetStart": "5%"
                            },
                            {
                                "type": "text",
                                "text": "BG1 - SDH",
                                "align": "end",
                                "color": "#FFFFFF",
                                "size": "sm",
                                "weight": "bold",
                                "offsetEnd": "5%"
                            }
                        ]
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "text",
                                "text": "Week 45 (04/11/19 - 10/11/19)",
                                "size": "xs",
                                "align": "end",
                                "style": "italic"
                            },
                            {
                                "type": "separator"
                            },
                            {
                                "type": "box",
                                "layout": "baseline",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "รายการ",
                                        "size": "xs",
                                        "color": "#4FFFBD"
                                    },
                                    {
                                        "type": "text",
                                        "text": "Target",
                                        "size": "sm",
                                        "align": "end",
                                        "weight": "bold",
                                        "position": "absolute",
                                        "offsetBottom": "1px",
                                        "offsetStart": "59%"
                                    },
                                    {
                                        "type": "text",
                                        "text": "Actual",
                                        "size": "sm",
                                        "align": "end",
                                        "weight": "bold"
                                    },
                                    {
                                        "type": "icon",
                                        "url": "https://i.ibb.co/Ws37N5t/icon-tmp.png",
                                        "margin": "lg"
                                    }
                                ],
                                "backgroundColor": "#4FFFBD"
                            },
                            {
                                "type": "separator"
                            },
                            {
                                "type": "box",
                                "layout": "baseline",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "โอน (MB)",
                                        "size": "xs",
                                        "flex": 0
                                    },
                                    {
                                        "type": "text",
                                        "text": "813",
                                        "size": "xs",
                                        "align": "end",
                                        "position": "absolute",
                                        "offsetStart": "65%",
                                        "offsetBottom": "1px"
                                    },
                                    {
                                        "type": "text",
                                        "text": "183",
                                        "size": "xs",
                                        "align": "end"
                                    },
                                    {
                                        "type": "icon",
                                        "url": "https://i.ibb.co/y0hQkxb/yellow-32x32.png",
                                        "margin": "lg",
                                        "offsetTop": "2px"
                                    }
                                ],
                                "backgroundColor": "#FAF5FF"
                            },
                            {
                                "type": "box",
                                "layout": "baseline",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "โอน (Unit)",
                                        "size": "xs",
                                        "flex": 0
                                    },
                                    {
                                        "type": "text",
                                        "text": "813",
                                        "size": "xs",
                                        "align": "end",
                                        "position": "absolute",
                                        "offsetBottom": "1px",
                                        "offsetStart": "65%"
                                    },
                                    {
                                        "type": "text",
                                        "text": "183",
                                        "size": "xs",
                                        "align": "end"
                                    },
                                    {
                                        "type": "icon",
                                        "url": "https://i.ibb.co/b2zz5hJ/green-32x32.png",
                                        "margin": "lg",
                                        "offsetTop": "2px"
                                    }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "baseline",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "ห้องผ่าน QC",
                                        "size": "xs",
                                        "flex": 0
                                    },
                                    {
                                        "type": "text",
                                        "text": "813",
                                        "size": "xs",
                                        "align": "end",
                                        "position": "absolute",
                                        "offsetBottom": "1px",
                                        "offsetStart": "65%"
                                    },
                                    {
                                        "type": "text",
                                        "text": "183",
                                        "size": "xs",
                                        "align": "end"
                                    },
                                    {
                                        "type": "icon",
                                        "url": "https://i.ibb.co/ykFsNjm/red-32x32.png",
                                        "margin": "lg",
                                        "offsetTop": "2px"
                                    }
                                ],
                                "backgroundColor": "#FAF5FF"
                            },
                            {
                                "type": "box",
                                "layout": "baseline",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "ลูกค้าเข้าตรวจ",
                                        "size": "xs",
                                        "flex": 0
                                    },
                                    {
                                        "type": "text",
                                        "text": "813",
                                        "size": "xs",
                                        "align": "end",
                                        "position": "absolute",
                                        "offsetBottom": "1px",
                                        "offsetStart": "65%"
                                    },
                                    {
                                        "type": "text",
                                        "text": "183",
                                        "size": "xs",
                                        "align": "end"
                                    },
                                    {
                                        "type": "icon",
                                        "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png",
                                        "margin": "lg"
                                    }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "baseline",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "ลูกค้ารับห้อง",
                                        "size": "xs",
                                        "flex": 0
                                    },
                                    {
                                        "type": "text",
                                        "text": "813",
                                        "size": "xs",
                                        "align": "end",
                                        "position": "absolute",
                                        "offsetBottom": "1px",
                                        "offsetStart": "65%"
                                    },
                                    {
                                        "type": "text",
                                        "text": "183",
                                        "size": "xs",
                                        "align": "end"
                                    },
                                    {
                                        "type": "icon",
                                        "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png",
                                        "margin": "lg"
                                    }
                                ],
                                "backgroundColor": "#FAF5FF"
                            },
                            {
                                "type": "box",
                                "layout": "baseline",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "โอนสด + Bankอนุมัติ",
                                        "size": "xs",
                                        "wrap": True,
                                        "flex": 0
                                    },
                                    {
                                        "type": "text",
                                        "text": "813",
                                        "size": "xs",
                                        "align": "end",
                                        "flex": 2,
                                        "position": "absolute",
                                        "offsetBottom": "1px",
                                        "offsetStart": "65%"
                                    },
                                    {
                                        "type": "text",
                                        "text": "183",
                                        "size": "xs",
                                        "align": "end"
                                    },
                                    {
                                        "type": "icon",
                                        "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png",
                                        "margin": "lg"
                                    }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "baseline",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "Grs. Presale(MB)",
                                        "size": "xs",
                                        "wrap": True,
                                        "flex": 0
                                    },
                                    {
                                        "type": "text",
                                        "text": "813",
                                        "size": "xs",
                                        "align": "end",
                                        "position": "absolute",
                                        "offsetBottom": "1px",
                                        "offsetStart": "65%"
                                    },
                                    {
                                        "type": "text",
                                        "text": "183",
                                        "size": "xs",
                                        "align": "end"
                                    },
                                    {
                                        "type": "icon",
                                        "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png",
                                        "margin": "lg"
                                    }
                                ],
                                "backgroundColor": "#FAF5FF"
                            },
                            {
                                "type": "box",
                                "layout": "baseline",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "Net Presale (MB)",
                                        "size": "xs",
                                        "flex": 0
                                    },
                                    {
                                        "type": "text",
                                        "text": "813",
                                        "size": "xs",
                                        "align": "end",
                                        "position": "absolute",
                                        "offsetBottom": "1px",
                                        "offsetStart": "65%"
                                    },
                                    {
                                        "type": "text",
                                        "text": "183",
                                        "size": "xs",
                                        "align": "end"
                                    },
                                    {
                                        "type": "icon",
                                        "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png",
                                        "margin": "lg"
                                    }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "baseline",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "Net Presale (MB) - รอยกเลิก",
                                        "size": "xs",
                                        "wrap": True,
                                        "flex": 0
                                    },
                                    {
                                        "type": "text",
                                        "text": "813",
                                        "size": "xs",
                                        "align": "end",
                                        "flex": 1,
                                        "margin": "xxl",
                                        "position": "absolute",
                                        "offsetBottom": "1px",
                                        "offsetStart": "65%"
                                    },
                                    {
                                        "type": "text",
                                        "text": "183",
                                        "size": "xs",
                                        "align": "end"
                                    },
                                    {
                                        "type": "icon",
                                        "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png",
                                        "margin": "lg"
                                    }
                                ],
                                "backgroundColor": "#FAF5FF"
                            },
                            {
                                "type": "box",
                                "layout": "baseline",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "รอยกเลิก (MB)",
                                        "size": "xs",
                                        "flex": 0
                                    },
                                    {
                                        "type": "text",
                                        "text": "813",
                                        "size": "xs",
                                        "align": "end",
                                        "position": "absolute",
                                        "offsetBottom": "1px",
                                        "offsetStart": "65%"
                                    },
                                    {
                                        "type": "text",
                                        "text": "183",
                                        "size": "xs",
                                        "align": "end"
                                    },
                                    {
                                        "type": "icon",
                                        "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png",
                                        "margin": "lg"
                                    }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "baseline",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "Grs. Presale (Units)",
                                        "size": "xs",
                                        "flex": 0
                                    },
                                    {
                                        "type": "text",
                                        "text": "813",
                                        "size": "xs",
                                        "align": "end",
                                        "flex": 2,
                                        "position": "absolute",
                                        "offsetBottom": "1px",
                                        "offsetStart": "65%"
                                    },
                                    {
                                        "type": "text",
                                        "text": "183",
                                        "size": "xs",
                                        "align": "end"
                                    },
                                    {
                                        "type": "icon",
                                        "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png",
                                        "margin": "lg"
                                    }
                                ],
                                "backgroundColor": "#FAF5FF"
                            },
                            {
                                "type": "box",
                                "layout": "baseline",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "Net Presale (Units)",
                                        "size": "xs",
                                        "wrap": True,
                                        "flex": 0
                                    },
                                    {
                                        "type": "text",
                                        "text": "813",
                                        "size": "xs",
                                        "align": "end",
                                        "position": "absolute",
                                        "offsetBottom": "1px",
                                        "offsetStart": "65%"
                                    },
                                    {
                                        "type": "text",
                                        "text": "183",
                                        "size": "xs",
                                        "align": "end"
                                    },
                                    {
                                        "type": "icon",
                                        "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png",
                                        "margin": "lg"
                                    }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "baseline",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "Net Presales (Unit) - รอยกเลิก",
                                        "size": "xs",
                                        "wrap": True,
                                        "flex": 0
                                    },
                                    {
                                        "type": "text",
                                        "text": "813",
                                        "size": "xs",
                                        "align": "end",
                                        "position": "absolute",
                                        "offsetBottom": "1px",
                                        "offsetStart": "65%"
                                    },
                                    {
                                        "type": "text",
                                        "text": "183",
                                        "size": "xs",
                                        "align": "end"
                                    },
                                    {
                                        "type": "icon",
                                        "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png",
                                        "margin": "lg"
                                    }
                                ],
                                "backgroundColor": "#FAF5FF"
                            },
                            {
                                "type": "box",
                                "layout": "baseline",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "รอยกเลิก (Units)",
                                        "size": "xs",
                                        "flex": 0
                                    },
                                    {
                                        "type": "text",
                                        "text": "813",
                                        "size": "xs",
                                        "align": "end",
                                        "position": "absolute",
                                        "offsetBottom": "1px",
                                        "offsetStart": "65%"
                                    },
                                    {
                                        "type": "text",
                                        "text": "183",
                                        "size": "xs",
                                        "align": "end"
                                    },
                                    {
                                        "type": "icon",
                                        "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png",
                                        "margin": "lg"
                                    }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "baseline",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "Walk",
                                        "size": "xs",
                                        "flex": 0
                                    },
                                    {
                                        "type": "text",
                                        "text": "813",
                                        "size": "xs",
                                        "align": "end",
                                        "position": "absolute",
                                        "offsetBottom": "1px",
                                        "offsetStart": "65%"
                                    },
                                    {
                                        "type": "text",
                                        "text": "183",
                                        "size": "xs",
                                        "align": "end"
                                    },
                                    {
                                        "type": "icon",
                                        "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png",
                                        "margin": "lg"
                                    }
                                ],
                                "backgroundColor": "#FAF5FF"
                            },
                            {
                                "type": "box",
                                "layout": "baseline",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "2nd Walk++",
                                        "size": "xs",
                                        "flex": 0
                                    },
                                    {
                                        "type": "text",
                                        "text": "813",
                                        "size": "xs",
                                        "align": "end",
                                        "position": "absolute",
                                        "offsetBottom": "1px",
                                        "offsetStart": "65%"
                                    },
                                    {
                                        "type": "text",
                                        "text": "183",
                                        "size": "xs",
                                        "align": "end"
                                    },
                                    {
                                        "type": "icon",
                                        "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png",
                                        "margin": "lg"
                                    }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "baseline",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "Conversion",
                                        "size": "xs",
                                        "flex": 0
                                    },
                                    {
                                        "type": "text",
                                        "text": "813",
                                        "size": "xs",
                                        "align": "end",
                                        "position": "absolute",
                                        "offsetBottom": "1px",
                                        "offsetStart": "65%"
                                    },
                                    {
                                        "type": "text",
                                        "text": "183",
                                        "size": "xs",
                                        "align": "end"
                                    },
                                    {
                                        "type": "icon",
                                        "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png",
                                        "margin": "lg"
                                    }
                                ],
                                "backgroundColor": "#FAF5FF"
                            }
                        ]
                    },
                    "footer": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "text",
                                "text": "Copyright 2019 AP (Thailand) PCL.",
                                "align": "center",
                                "size": "xs",
                                "color": "#FFFFFF"
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "image",
                                        "url": "https://i.ibb.co/fS0B4wP/AP-Logo-2018.png"
                                    }
                                ],
                                "position": "absolute",
                                "height": "30px",
                                "width": "32px",
                                "offsetBottom": "3px"
                            }
                        ]
                    },
                    "styles": {
                        "hero": {
                            "backgroundColor": "#000000"
                        },
                        "footer": {
                            "backgroundColor": "#000000"
                        }
                    }
                }
        }

    data = {
        "replyToken": reply_token,
        "messages": [
          type_msg
        ]
    }


    session = requests.Session()
    response = session.post(LINE_API, data=json.dumps(data), headers=headers)
    return 201
