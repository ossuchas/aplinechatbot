# -*- coding: utf-8 -*-

import requests
import json
from config import LINE_API
from models.crm_line_actual_income import ActualIncomeModel


def replyMsg(Reply_token: str =None, actual_income: ActualIncomeModel = None, line_Acees_Token: str = None):
    authorization = 'Bearer {}'.format(line_Acees_Token)
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization': authorization
    }
    # print(actual_income.ap_bg1_q1)
    print(f"{actual_income.ap_bg1_q2:,.0f}")

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
                                "text": "Executive Summary",
                                "size": "xs",
                                "offsetTop": "5px",
                                "offsetStart": "5%",
                                "color": "#FFFFFF"
                            },
                            {
                                "type": "text",
                                "text": "Week45 : 04/11/19 - 10/11/19",
                                "align": "end",
                                "size": "xxs",
                                "offsetEnd": "5%",
                                "offsetTop": "5px",
                                "color": "#FFFFFF"
                            }
                        ],
                        "height": "30px"
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "box",
                                "layout": "baseline",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": ":: Booking ::",
                                        "size": "md",
                                        "weight": "bold",
                                        "align": "start"
                                    }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "baseline",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "BG",
                                        "align": "start",
                                        "weight": "bold",
                                        "size": "sm"
                                    },
                                    {
                                        "type": "text",
                                        "text": "Unit",
                                        "size": "xs",
                                        "align": "end",
                                        "weight": "bold"
                                    },
                                    {
                                        "type": "text",
                                        "text": "Vol.",
                                        "size": "xs",
                                        "align": "end",
                                        "weight": "bold"
                                    },
                                    {
                                        "type": "text",
                                        "text": "% W44",
                                        "align": "end",
                                        "size": "xs",
                                        "weight": "bold"
                                    },
                                    {
                                        "type": "icon",
                                        "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                                    }
                                ],
                                "backgroundColor": "#EBE4AB"
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
                                        "text": "SDH",
                                        "size": "xs",
                                        "align": "start"
                                    },
                                    {
                                        "type": "text",
                                        "text": "27",
                                        "size": "xs",
                                        "align": "end"
                                    },
                                    {
                                        "type": "text",
                                        "text": "198.42M",
                                        "size": "xs",
                                        "align": "end"
                                    },
                                    {
                                        "type": "text",
                                        "text": "1.83",
                                        "size": "xs",
                                        "align": "end"
                                    },
                                    {
                                        "type": "icon",
                                        "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                                    }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "baseline",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "TH",
                                        "size": "xs",
                                        "align": "start"
                                    },
                                    {
                                        "type": "text",
                                        "text": "128",
                                        "size": "xs",
                                        "align": "end"
                                    },
                                    {
                                        "type": "text",
                                        "text": "454.69M",
                                        "size": "xs",
                                        "align": "end"
                                    },
                                    {
                                        "type": "text",
                                        "text": "2.83",
                                        "size": "xxs",
                                        "align": "end"
                                    },
                                    {
                                        "type": "icon",
                                        "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                                    }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "baseline",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "CD1",
                                        "size": "xs",
                                        "align": "start"
                                    },
                                    {
                                        "type": "text",
                                        "text": "31",
                                        "size": "xs",
                                        "align": "end"
                                    },
                                    {
                                        "type": "text",
                                        "text": "95.59M",
                                        "size": "xs",
                                        "align": "end"
                                    },
                                    {
                                        "type": "text",
                                        "text": "1.83",
                                        "size": "xs",
                                        "align": "end"
                                    },
                                    {
                                        "type": "icon",
                                        "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                                    }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "baseline",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "CD2",
                                        "size": "xs",
                                        "align": "start"
                                    },
                                    {
                                        "type": "text",
                                        "text": "41",
                                        "size": "xs",
                                        "align": "end"
                                    },
                                    {
                                        "type": "text",
                                        "text": "90.71M",
                                        "size": "xs",
                                        "align": "end"
                                    },
                                    {
                                        "type": "text",
                                        "text": "1.38",
                                        "size": "xs",
                                        "align": "end"
                                    },
                                    {
                                        "type": "icon",
                                        "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                                    }
                                ]
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
                                        "text": "Total",
                                        "size": "xs",
                                        "align": "end",
                                        "weight": "bold"
                                    },
                                    {
                                        "type": "text",
                                        "text": "226",
                                        "size": "xs",
                                        "align": "end",
                                        "weight": "bold"
                                    },
                                    {
                                        "type": "text",
                                        "text": "839.41M",
                                        "size": "xs",
                                        "align": "end",
                                        "weight": "bold"
                                    },
                                    {
                                        "type": "text",
                                        "text": "2.80",
                                        "size": "xs",
                                        "align": "end",
                                        "weight": "bold"
                                    },
                                    {
                                        "type": "icon",
                                        "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                                    }
                                ],
                                "backgroundColor": "#F6FFFF"
                            },
                            {
                                "type": "separator",
                                "margin": "none"
                            },
                            {
                                "type": "box",
                                "layout": "baseline",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": ":: Net Booking ::",
                                        "size": "md",
                                        "weight": "bold"
                                    }
                                ],
                                "margin": "xs"
                            },
                            {
                                "type": "box",
                                "layout": "baseline",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "BG",
                                        "align": "start",
                                        "weight": "bold",
                                        "size": "sm"
                                    },
                                    {
                                        "type": "text",
                                        "text": "Unit",
                                        "size": "xs",
                                        "align": "end",
                                        "weight": "bold"
                                    },
                                    {
                                        "type": "text",
                                        "text": "Vol.",
                                        "size": "xs",
                                        "align": "end",
                                        "weight": "bold"
                                    },
                                    {
                                        "type": "text",
                                        "text": "% W44",
                                        "align": "end",
                                        "size": "xs",
                                        "weight": "bold"
                                    },
                                    {
                                        "type": "icon",
                                        "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                                    }
                                ],
                                "backgroundColor": "#EBE4AB"
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
                                        "text": "SDH",
                                        "size": "xs",
                                        "align": "start"
                                    },
                                    {
                                        "type": "text",
                                        "text": "27",
                                        "size": "xs",
                                        "align": "end"
                                    },
                                    {
                                        "type": "text",
                                        "text": "198.42M",
                                        "size": "xs",
                                        "align": "end"
                                    },
                                    {
                                        "type": "text",
                                        "text": "1.83",
                                        "size": "xs",
                                        "align": "end"
                                    },
                                    {
                                        "type": "icon",
                                        "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                                    }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "baseline",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "TH",
                                        "size": "xs",
                                        "align": "start"
                                    },
                                    {
                                        "type": "text",
                                        "text": "128",
                                        "size": "xs",
                                        "align": "end"
                                    },
                                    {
                                        "type": "text",
                                        "text": "454.69M",
                                        "size": "xs",
                                        "align": "end"
                                    },
                                    {
                                        "type": "text",
                                        "text": "2.83",
                                        "size": "xxs",
                                        "align": "end"
                                    },
                                    {
                                        "type": "icon",
                                        "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                                    }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "baseline",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "CD1",
                                        "size": "xs",
                                        "align": "start"
                                    },
                                    {
                                        "type": "text",
                                        "text": "31",
                                        "size": "xs",
                                        "align": "end"
                                    },
                                    {
                                        "type": "text",
                                        "text": "95.59M",
                                        "size": "xs",
                                        "align": "end"
                                    },
                                    {
                                        "type": "text",
                                        "text": "1.83",
                                        "size": "xs",
                                        "align": "end"
                                    },
                                    {
                                        "type": "icon",
                                        "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                                    }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "baseline",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "CD2",
                                        "size": "xs",
                                        "align": "start"
                                    },
                                    {
                                        "type": "text",
                                        "text": "41",
                                        "size": "xs",
                                        "align": "end"
                                    },
                                    {
                                        "type": "text",
                                        "text": "90.71M",
                                        "size": "xs",
                                        "align": "end"
                                    },
                                    {
                                        "type": "text",
                                        "text": "1.38",
                                        "size": "xs",
                                        "align": "end"
                                    },
                                    {
                                        "type": "icon",
                                        "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                                    }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "baseline",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "Total",
                                        "size": "xs",
                                        "align": "end",
                                        "weight": "bold"
                                    },
                                    {
                                        "type": "text",
                                        "text": "226",
                                        "size": "xs",
                                        "align": "end",
                                        "weight": "bold"
                                    },
                                    {
                                        "type": "text",
                                        "text": "839.41M",
                                        "size": "xs",
                                        "align": "end",
                                        "weight": "bold"
                                    },
                                    {
                                        "type": "text",
                                        "text": "2.80",
                                        "size": "xs",
                                        "align": "end",
                                        "weight": "bold"
                                    },
                                    {
                                        "type": "icon",
                                        "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                                    }
                                ],
                                "backgroundColor": "#F6FFFF"
                            },
                            {
                                "type": "box",
                                "layout": "baseline",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": ":: Transfer ::",
                                        "size": "md",
                                        "weight": "bold"
                                    }
                                ],
                                "margin": "xs"
                            },
                            {
                                "type": "box",
                                "layout": "baseline",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "BG",
                                        "align": "start",
                                        "weight": "bold",
                                        "size": "sm"
                                    },
                                    {
                                        "type": "text",
                                        "text": "Unit",
                                        "size": "xs",
                                        "align": "end",
                                        "weight": "bold"
                                    },
                                    {
                                        "type": "text",
                                        "text": "Vol.",
                                        "size": "xs",
                                        "align": "end",
                                        "weight": "bold"
                                    },
                                    {
                                        "type": "text",
                                        "text": "% W44",
                                        "align": "end",
                                        "size": "xs",
                                        "weight": "bold"
                                    },
                                    {
                                        "type": "icon",
                                        "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                                    }
                                ],
                                "backgroundColor": "#EBE4AB"
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
                                        "text": "SDH",
                                        "size": "xs",
                                        "align": "start"
                                    },
                                    {
                                        "type": "text",
                                        "text": "27",
                                        "size": "xs",
                                        "align": "end"
                                    },
                                    {
                                        "type": "text",
                                        "text": "198.42M",
                                        "size": "xs",
                                        "align": "end"
                                    },
                                    {
                                        "type": "text",
                                        "text": "1.83",
                                        "size": "xs",
                                        "align": "end"
                                    },
                                    {
                                        "type": "icon",
                                        "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                                    }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "baseline",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "TH",
                                        "size": "xs",
                                        "align": "start"
                                    },
                                    {
                                        "type": "text",
                                        "text": "128",
                                        "size": "xs",
                                        "align": "end"
                                    },
                                    {
                                        "type": "text",
                                        "text": "454.69M",
                                        "size": "xs",
                                        "align": "end"
                                    },
                                    {
                                        "type": "text",
                                        "text": "2.83",
                                        "size": "xxs",
                                        "align": "end"
                                    },
                                    {
                                        "type": "icon",
                                        "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                                    }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "baseline",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "CD1",
                                        "size": "xs",
                                        "align": "start"
                                    },
                                    {
                                        "type": "text",
                                        "text": "31",
                                        "size": "xs",
                                        "align": "end"
                                    },
                                    {
                                        "type": "text",
                                        "text": "95.59M",
                                        "size": "xs",
                                        "align": "end"
                                    },
                                    {
                                        "type": "text",
                                        "text": "1.83",
                                        "size": "xs",
                                        "align": "end"
                                    },
                                    {
                                        "type": "icon",
                                        "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                                    }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "baseline",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "CD2",
                                        "size": "xs",
                                        "align": "start"
                                    },
                                    {
                                        "type": "text",
                                        "text": "41",
                                        "size": "xs",
                                        "align": "end"
                                    },
                                    {
                                        "type": "text",
                                        "text": "90.71M",
                                        "size": "xs",
                                        "align": "end"
                                    },
                                    {
                                        "type": "text",
                                        "text": "1.38",
                                        "size": "xs",
                                        "align": "end"
                                    },
                                    {
                                        "type": "icon",
                                        "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                                    }
                                ]
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
                                        "text": "Total",
                                        "size": "xs",
                                        "align": "end",
                                        "weight": "bold"
                                    },
                                    {
                                        "type": "text",
                                        "text": "226",
                                        "size": "xs",
                                        "align": "end",
                                        "weight": "bold"
                                    },
                                    {
                                        "type": "text",
                                        "text": "839.41M",
                                        "size": "xs",
                                        "align": "end",
                                        "weight": "bold"
                                    },
                                    {
                                        "type": "text",
                                        "text": "2.80",
                                        "size": "xs",
                                        "align": "end",
                                        "weight": "bold"
                                    },
                                    {
                                        "type": "icon",
                                        "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                                    }
                                ],
                                "backgroundColor": "#F6FFFF"
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
                                "size": "xxs",
                                "align": "center",
                                "color": "#ffffff"
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
                                "width": "32px",
                                "height": "32px",
                                "offsetBottom": "2px"
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
        "replyToken": Reply_token,
        "messages": [
            type_msg
        ]
    }

    session = requests.Session()
    response = session.post(LINE_API, data=json.dumps(data), headers=headers)
    return 201
