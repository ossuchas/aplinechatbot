# -*- coding: utf-8 -*-

import requests
import json
from config import LINE_API
from models.crm_line_ll_data import LeadLagModel


def replyMsg(Reply_token: str =None, bg: str = None, subbg: str = None,
             ll: LeadLagModel = None, line_Acees_Token: str = None):
    authorization = 'Bearer {}'.format(line_Acees_Token)
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
                    "size": "giga",
                    "header": {
                        "type": "box",
                        "layout": "baseline",
                        "contents": [
                            {
                                "type": "text",
                                "text": "Lead Lag",
                                "color": "#FFFFFF",
                                "size": "lg",
                                "weight": "bold"
                            },
                            {
                                "type": "text",
                                "text": "BG1 - SDH",
                                "align": "end",
                                "color": "#FFFFFF",
                                "weight": "bold"
                            },
                            {
                                "type": "text",
                                "text": "Week 47 (18/11/19 - 24/11/19)",
                                "position": "absolute",
                                "color": "#FFFFFF",
                                "size": "xs",
                                "style": "italic",
                                "offsetEnd": "17px",
                                "offsetBottom": "2px"
                            }
                        ]
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "separator"
                            },
                            {
                                "type": "text",
                                "text": "10077 : The Centro วัชรพล",
                                "size": "sm",
                                "margin": "none"
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
                                        "text": "257",
                                        "size": "xs",
                                        "align": "end",
                                        "position": "absolute",
                                        "offsetBottom": "1px",
                                        "offsetEnd": "31%"
                                    },
                                    {
                                        "type": "text",
                                        "text": "157",
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
                                        "text": "40",
                                        "size": "xs",
                                        "align": "end",
                                        "position": "absolute",
                                        "offsetBottom": "1px",
                                        "offsetEnd": "31%"
                                    },
                                    {
                                        "type": "text",
                                        "text": "24",
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
                                        "text": "29",
                                        "size": "xs",
                                        "position": "absolute",
                                        "offsetBottom": "1px",
                                        "align": "end",
                                        "offsetEnd": "31%"
                                    },
                                    {
                                        "type": "text",
                                        "text": "19",
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
                                        "text": "6",
                                        "size": "xs",
                                        "position": "absolute",
                                        "align": "end",
                                        "offsetBottom": "1px",
                                        "offsetEnd": "31%"
                                    },
                                    {
                                        "type": "text",
                                        "text": "28",
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
                                        "text": "30",
                                        "size": "xs",
                                        "align": "end",
                                        "position": "absolute",
                                        "offsetBottom": "1px",
                                        "offsetEnd": "31%"
                                    },
                                    {
                                        "type": "text",
                                        "text": "36",
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
                                        "text": "-",
                                        "size": "xs",
                                        "align": "end",
                                        "flex": 2,
                                        "position": "absolute",
                                        "offsetBottom": "1px",
                                        "offsetEnd": "31%"
                                    },
                                    {
                                        "type": "text",
                                        "text": "17",
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
                                        "text": "-",
                                        "size": "xs",
                                        "align": "end",
                                        "position": "absolute",
                                        "offsetBottom": "1px",
                                        "offsetEnd": "31%"
                                    },
                                    {
                                        "type": "text",
                                        "text": "279",
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
                                        "text": "195",
                                        "size": "xs",
                                        "align": "end",
                                        "position": "absolute",
                                        "offsetBottom": "1px",
                                        "offsetEnd": "31%"
                                    },
                                    {
                                        "type": "text",
                                        "text": "73",
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
                                        "text": "-",
                                        "size": "xs",
                                        "align": "end",
                                        "flex": 1,
                                        "margin": "xxl",
                                        "position": "absolute",
                                        "offsetBottom": "1px",
                                        "offsetEnd": "31%"
                                    },
                                    {
                                        "type": "text",
                                        "text": "206",
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
                                        "text": "-",
                                        "size": "xs",
                                        "align": "end",
                                        "position": "absolute",
                                        "offsetBottom": "1px",
                                        "offsetEnd": "31%"
                                    },
                                    {
                                        "type": "text",
                                        "text": "133",
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
                                        "text": "-",
                                        "size": "xs",
                                        "align": "end",
                                        "flex": 2,
                                        "position": "absolute",
                                        "offsetBottom": "1px",
                                        "offsetEnd": "31%"
                                    },
                                    {
                                        "type": "text",
                                        "text": "31",
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
                                        "text": "26",
                                        "size": "xs",
                                        "align": "end",
                                        "position": "absolute",
                                        "offsetBottom": "1px",
                                        "offsetEnd": "31%"
                                    },
                                    {
                                        "type": "text",
                                        "text": "13",
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
                                        "text": "-",
                                        "size": "xs",
                                        "align": "end",
                                        "position": "absolute",
                                        "offsetBottom": "1px",
                                        "offsetEnd": "31%"
                                    },
                                    {
                                        "type": "text",
                                        "text": "32",
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
                                        "text": "-",
                                        "size": "xs",
                                        "align": "end",
                                        "position": "absolute",
                                        "offsetBottom": "1px",
                                        "offsetEnd": "31%"
                                    },
                                    {
                                        "type": "text",
                                        "text": "19",
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
                                        "text": "215",
                                        "size": "xs",
                                        "align": "end",
                                        "position": "absolute",
                                        "offsetBottom": "1px",
                                        "offsetEnd": "31%"
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
                                        "text": "59",
                                        "size": "xs",
                                        "align": "end",
                                        "position": "absolute",
                                        "offsetBottom": "1px",
                                        "offsetEnd": "31%"
                                    },
                                    {
                                        "type": "text",
                                        "text": "52",
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
                                        "text": "11",
                                        "size": "xs",
                                        "align": "end",
                                        "position": "absolute",
                                        "offsetBottom": "1px",
                                        "offsetEnd": "31%"
                                    },
                                    {
                                        "type": "text",
                                        "text": "18",
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
                                "type": "separator"
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
                        "header": {
                            "backgroundColor": "#000000"
                        },
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
        "replyToken": Reply_token,
        "messages": [
            type_msg
        ]
    }

    session = requests.Session()
    response = session.post(LINE_API, data=json.dumps(data), headers=headers)
    return 201
