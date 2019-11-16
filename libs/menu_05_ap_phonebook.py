# -*- coding: utf-8 -*-

import requests
import json
from config import LINE_API


def replyMsg(Reply_token: str =None, TextMessage: str = None, line_Acees_Token: str = None):
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
                    "hero": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "text",
                                "text": "xxx",
                                "color": "#000000"
                            }
                        ]
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "image",
                                        "url": "https://i.ibb.co/kcRpWJG/AP003910.jpg",
                                        "align": "start",
                                        "aspectMode": "fit",
                                        "size": "md",
                                        "offsetStart": "-15%",
                                        "offsetTop": "-7px"
                                    }
                                ],
                                "position": "absolute",
                                "borderWidth": "2px",
                                "paddingTop": "2%",
                                "width": "128px",
                                "height": "128px"
                            },
                            {
                                "type": "box",
                                "layout": "baseline",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "ชื่อ :",
                                        "align": "end",
                                        "size": "xs",
                                        "color": "#989898",
                                        "weight": "bold"
                                    },
                                    {
                                        "type": "text",
                                        "text": "สุชาติ สุเจริญลาภ (ไก่)",
                                        "size": "xs",
                                        "align": "start",
                                        "offsetStart": "4%",
                                        "wrap": True,
                                        "color": "#989898"
                                    }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "baseline",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "Name :",
                                        "align": "end",
                                        "size": "xs",
                                        "color": "#989898",
                                        "weight": "bold"
                                    },
                                    {
                                        "type": "text",
                                        "text": "Suchat Sujalarnlap",
                                        "size": "xs",
                                        "align": "start",
                                        "offsetStart": "4%",
                                        "wrap": True,
                                        "color": "#989898"
                                    }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "baseline",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "รหัสพนักงาน :",
                                        "align": "end",
                                        "size": "xs",
                                        "color": "#989898",
                                        "weight": "bold"
                                    },
                                    {
                                        "type": "text",
                                        "text": "AP003910",
                                        "size": "xs",
                                        "align": "start",
                                        "offsetStart": "4%",
                                        "color": "#989898"
                                    }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "baseline",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "ตำแหน่ง :",
                                        "size": "xs",
                                        "align": "end",
                                        "color": "#989898",
                                        "weight": "bold"
                                    },
                                    {
                                        "type": "text",
                                        "text": "Assistant Team Leader: IT Business Analysis",
                                        "wrap": True,
                                        "size": "xs",
                                        "offsetStart": "4%",
                                        "color": "#989898"
                                    }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "baseline",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "อีเมล :",
                                        "size": "xs",
                                        "align": "end",
                                        "color": "#989898",
                                        "weight": "bold"
                                    },
                                    {
                                        "type": "text",
                                        "text": "suchat_s@apthai.com",
                                        "size": "xs",
                                        "wrap": True,
                                        "offsetStart": "4%",
                                        "color": "#989898"
                                    }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "baseline",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "เบอร์มือถือบริษัท :",
                                        "size": "xs",
                                        "align": "end",
                                        "color": "#989898",
                                        "weight": "bold"
                                    },
                                    {
                                        "type": "text",
                                        "text": "0655186997",
                                        "size": "xs",
                                        "align": "start",
                                        "offsetStart": "4%",
                                        "color": "#989898"
                                    }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "baseline",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "เบอร์โทรภายใน :",
                                        "size": "xs",
                                        "align": "end",
                                        "color": "#989898",
                                        "weight": "bold"
                                    },
                                    {
                                        "type": "text",
                                        "text": "647",
                                        "align": "start",
                                        "size": "xs",
                                        "offsetStart": "4%",
                                        "color": "#989898"
                                    }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "baseline",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "สายงาน :",
                                        "size": "xs",
                                        "align": "end",
                                        "color": "#989898",
                                        "weight": "bold"
                                    },
                                    {
                                        "type": "text",
                                        "text": "Business Technology Integration (12041)",
                                        "size": "xs",
                                        "align": "start",
                                        "offsetStart": "4%",
                                        "wrap": True,
                                        "color": "#989898"
                                    }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "baseline",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "ฝ่ายงาน :",
                                        "size": "xs",
                                        "align": "end",
                                        "color": "#989898",
                                        "weight": "bold"
                                    },
                                    {
                                        "type": "text",
                                        "text": "IT Business Analysis",
                                        "size": "xs",
                                        "align": "start",
                                        "offsetStart": "4%",
                                        "wrap": True,
                                        "color": "#989898"
                                    }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "baseline",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "หัวหน้างาน :",
                                        "size": "xs",
                                        "align": "end",
                                        "color": "#989898",
                                        "weight": "bold"
                                    },
                                    {
                                        "type": "text",
                                        "text": "สมชาย วัฒนเสาวภาคย์",
                                        "size": "xs",
                                        "align": "start",
                                        "offsetStart": "4%",
                                        "wrap": True,
                                        "color": "#989898"
                                    }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "baseline",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "บริษัท :",
                                        "size": "xs",
                                        "align": "end",
                                        "color": "#989898",
                                        "weight": "bold"
                                    },
                                    {
                                        "type": "text",
                                        "text": "บริษัท เอพี (ไทยแลนด์) จำกัด (มหาชน )",
                                        "size": "xs",
                                        "wrap": True,
                                        "align": "start",
                                        "offsetStart": "4%",
                                        "color": "#989898"
                                    }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "baseline",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "สถานที่ปฏิบัติงาน :",
                                        "size": "xs",
                                        "align": "end",
                                        "color": "#989898",
                                        "weight": "bold"
                                    },
                                    {
                                        "type": "text",
                                        "text": "สำนักงานใหญ่",
                                        "size": "xs",
                                        "align": "start",
                                        "offsetStart": "4%",
                                        "color": "#989898"
                                    }
                                ]
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
                                "color": "#FFFFFF",
                                "align": "center"
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
