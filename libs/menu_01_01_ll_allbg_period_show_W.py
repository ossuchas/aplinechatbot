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
                    "type": "carousel",
                    "contents": [
                        {
                            "type": "bubble",
                            "hero": {
                                "type": "box",
                                "layout": "baseline",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "Lead Lag (LL)",
                                        "size": "xl",
                                        "color": "#FFFFFF",
                                        "weight": "bold",
                                        "offsetStart": "20px"
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
                                        "layout": "vertical",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "Week45",
                                                "weight": "bold",
                                                "color": "#808080"
                                            }
                                        ],
                                        "offsetEnd": "-73%"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "filler",
                                                "flex": 1
                                            },
                                            {
                                                "type": "text",
                                                "text": "Target",
                                                "align": "end",
                                                "offsetEnd": "-3px",
                                                "weight": "bold",
                                                "color": "#808080"
                                            },
                                            {
                                                "type": "text",
                                                "text": "Actual",
                                                "align": "end",
                                                "offsetEnd": "20px",
                                                "weight": "bold",
                                                "color": "#808080"
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
                                                "text": "Transfer",
                                                "wrap": True,
                                                "color": "#808080",
                                                "size": "sm"
                                            },
                                            {
                                                "type": "text",
                                                "text": "489M",
                                                "size": "sm",
                                                "align": "end",
                                                "offsetEnd": "-15px"
                                            },
                                            {
                                                "type": "text",
                                                "text": "474M",
                                                "size": "sm",
                                                "align": "end",
                                                "offsetEnd": "10px"
                                            },
                                            {
                                                "type": "icon",
                                                "url": "https://i.ibb.co/y0hQkxb/yellow-32x32.png",
                                                "offsetEnd": "1px",
                                                "offsetBottom": "2px",
                                                "offsetTop": "3px"
                                            }
                                        ]
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "Transfer",
                                                "size": "sm",
                                                "color": "#808080"
                                            },
                                            {
                                                "type": "text",
                                                "text": "72u",
                                                "size": "sm",
                                                "align": "end",
                                                "offsetEnd": "-15px"
                                            },
                                            {
                                                "type": "text",
                                                "text": "66u",
                                                "size": "sm",
                                                "align": "end",
                                                "offsetEnd": "10px"
                                            },
                                            {
                                                "type": "icon",
                                                "url": "https://i.ibb.co/ykFsNjm/red-32x32.png",
                                                "offsetEnd": "1px",
                                                "offsetBottom": "2px",
                                                "offsetTop": "3px"
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
                                                "text": "Grs. Presale",
                                                "wrap": True,
                                                "size": "sm",
                                                "color": "#808080"
                                            },
                                            {
                                                "type": "text",
                                                "text": "-",
                                                "size": "sm",
                                                "align": "end",
                                                "offsetEnd": "-15px"
                                            },
                                            {
                                                "type": "text",
                                                "text": "1,555M",
                                                "size": "sm",
                                                "align": "end",
                                                "offsetEnd": "10px"
                                            },
                                            {
                                                "type": "icon",
                                                "url": "https://i.ibb.co/b2zz5hJ/green-32x32.png",
                                                "offsetEnd": "1px",
                                                "offsetBottom": "2px",
                                                "offsetTop": "3px"
                                            }
                                        ]
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "Grs. Presale",
                                                "wrap": True,
                                                "size": "sm",
                                                "color": "#808080"
                                            },
                                            {
                                                "type": "text",
                                                "text": "-",
                                                "size": "sm",
                                                "align": "end",
                                                "offsetEnd": "-15px"
                                            },
                                            {
                                                "type": "text",
                                                "text": "185u",
                                                "size": "sm",
                                                "align": "end",
                                                "offsetEnd": "10px"
                                            },
                                            {
                                                "type": "icon",
                                                "url": "https://i.ibb.co/b2zz5hJ/green-32x32.png",
                                                "offsetEnd": "1px",
                                                "offsetBottom": "2px",
                                                "offsetTop": "3px"
                                            }
                                        ]
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "Net Presale",
                                                "wrap": True,
                                                "size": "sm",
                                                "color": "#808080"
                                            },
                                            {
                                                "type": "text",
                                                "text": "1,078M",
                                                "size": "sm",
                                                "align": "end",
                                                "offsetEnd": "-15px"
                                            },
                                            {
                                                "type": "text",
                                                "text": "982M",
                                                "size": "sm",
                                                "align": "end",
                                                "offsetEnd": "10px"
                                            },
                                            {
                                                "type": "icon",
                                                "url": "https://i.ibb.co/ykFsNjm/red-32x32.png",
                                                "offsetEnd": "1px",
                                                "offsetBottom": "2px",
                                                "offsetTop": "3px"
                                            }
                                        ]
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "Net Presale",
                                                "size": "sm",
                                                "color": "#808080",
                                                "wrap": True
                                            },
                                            {
                                                "type": "text",
                                                "text": "148u",
                                                "size": "sm",
                                                "align": "end",
                                                "offsetEnd": "-15px"
                                            },
                                            {
                                                "type": "text",
                                                "text": "114u",
                                                "size": "sm",
                                                "align": "end",
                                                "offsetEnd": "10px"
                                            },
                                            {
                                                "type": "icon",
                                                "url": "https://i.ibb.co/ykFsNjm/red-32x32.png",
                                                "offsetEnd": "1px",
                                                "offsetBottom": "2px",
                                                "offsetTop": "3px"
                                            }
                                        ]
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "N.Presale + P.Cancel",
                                                "wrap": True,
                                                "size": "sm",
                                                "color": "#808080"
                                            },
                                            {
                                                "type": "text",
                                                "text": "-",
                                                "size": "sm",
                                                "align": "end",
                                                "offsetEnd": "-15px"
                                            },
                                            {
                                                "type": "text",
                                                "text": "660M",
                                                "size": "sm",
                                                "align": "end",
                                                "offsetEnd": "10px"
                                            },
                                            {
                                                "type": "icon",
                                                "url": "https://i.ibb.co/b2zz5hJ/green-32x32.png",
                                                "offsetEnd": "1px",
                                                "offsetBottom": "2px",
                                                "offsetTop": "3px"
                                            }
                                        ]
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "N.Presale + P.Cancel",
                                                "wrap": True,
                                                "size": "sm",
                                                "color": "#808080"
                                            },
                                            {
                                                "type": "text",
                                                "text": "-",
                                                "size": "sm",
                                                "align": "end",
                                                "offsetEnd": "-15px"
                                            },
                                            {
                                                "type": "text",
                                                "text": "75u",
                                                "size": "sm",
                                                "align": "end",
                                                "offsetEnd": "10px"
                                            },
                                            {
                                                "type": "icon",
                                                "url": "https://i.ibb.co/b2zz5hJ/green-32x32.png",
                                                "offsetEnd": "1px",
                                                "offsetBottom": "2px",
                                                "offsetTop": "3px"
                                            }
                                        ]
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "Pre Cancel",
                                                "size": "sm",
                                                "color": "#808080"
                                            },
                                            {
                                                "type": "text",
                                                "text": "-",
                                                "size": "sm",
                                                "align": "end",
                                                "offsetEnd": "-15px"
                                            },
                                            {
                                                "type": "text",
                                                "text": "(322)M",
                                                "size": "sm",
                                                "align": "end",
                                                "offsetEnd": "10px"
                                            },
                                            {
                                                "type": "icon",
                                                "url": "https://i.ibb.co/ykFsNjm/red-32x32.png",
                                                "offsetEnd": "1px",
                                                "offsetBottom": "2px",
                                                "offsetTop": "3px"
                                            }
                                        ]
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "Pre Cancel",
                                                "wrap": True,
                                                "color": "#808080",
                                                "size": "sm"
                                            },
                                            {
                                                "type": "text",
                                                "text": "-",
                                                "size": "sm",
                                                "align": "end",
                                                "offsetEnd": "-15px"
                                            },
                                            {
                                                "type": "text",
                                                "text": "(39)u",
                                                "size": "sm",
                                                "align": "end",
                                                "offsetEnd": "10px"
                                            },
                                            {
                                                "type": "icon",
                                                "url": "https://i.ibb.co/ykFsNjm/red-32x32.png",
                                                "offsetEnd": "1px",
                                                "offsetBottom": "2px",
                                                "offsetTop": "3px"
                                            }
                                        ]
                                    },
                                    {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "All BG",
                                                "weight": "bold",
                                                "color": "#808080",
                                                "size": "lg"
                                            },
                                            {
                                                "type": "text",
                                                "text": "By Quarter",
                                                "wrap": True,
                                                "color": "#808080",
                                                "size": "xs"
                                            }
                                        ],
                                        "position": "absolute",
                                        "offsetTop": "1%",
                                        "offsetStart": "5%",
                                        "paddingAll": "2px"
                                    },
                                    {
                                        "type": "separator",
                                        "margin": "md"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "Walk",
                                                "wrap": True,
                                                "color": "#808080",
                                                "size": "sm"
                                            },
                                            {
                                                "type": "text",
                                                "text": "1,378",
                                                "size": "sm",
                                                "align": "end",
                                                "offsetEnd": "-30px"
                                            },
                                            {
                                                "type": "text",
                                                "text": "1,110",
                                                "size": "sm",
                                                "align": "end",
                                                "offsetEnd": "10px"
                                            },
                                            {
                                                "type": "icon",
                                                "url": "https://i.ibb.co/y0hQkxb/yellow-32x32.png",
                                                "offsetEnd": "1px",
                                                "offsetBottom": "2px",
                                                "offsetTop": "3px"
                                            }
                                        ]
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "2nd Walk++",
                                                "wrap": True,
                                                "color": "#808080",
                                                "size": "sm"
                                            },
                                            {
                                                "type": "text",
                                                "text": "354",
                                                "size": "sm",
                                                "align": "end",
                                                "offsetEnd": "-30px"
                                            },
                                            {
                                                "type": "text",
                                                "text": "278",
                                                "size": "sm",
                                                "align": "end",
                                                "offsetEnd": "10px"
                                            },
                                            {
                                                "type": "icon",
                                                "url": "https://i.ibb.co/ykFsNjm/red-32x32.png",
                                                "offsetEnd": "1px",
                                                "offsetBottom": "2px",
                                                "offsetTop": "3px"
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
                                                "wrap": True,
                                                "color": "#808080",
                                                "size": "sm"
                                            },
                                            {
                                                "type": "text",
                                                "text": "12",
                                                "size": "sm",
                                                "align": "end",
                                                "offsetEnd": "-30px"
                                            },
                                            {
                                                "type": "text",
                                                "text": "12",
                                                "size": "sm",
                                                "align": "end",
                                                "offsetEnd": "10px"
                                            },
                                            {
                                                "type": "icon",
                                                "url": "https://i.ibb.co/y0hQkxb/yellow-32x32.png",
                                                "offsetEnd": "1px",
                                                "offsetBottom": "2px",
                                                "offsetTop": "3px"
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
                                                "wrap": True,
                                                "color": "#808080",
                                                "size": "sm"
                                            },
                                            {
                                                "type": "text",
                                                "text": "112",
                                                "size": "sm",
                                                "align": "end",
                                                "offsetEnd": "-30px"
                                            },
                                            {
                                                "type": "text",
                                                "text": "164",
                                                "size": "sm",
                                                "align": "end",
                                                "offsetEnd": "10px"
                                            },
                                            {
                                                "type": "icon",
                                                "url": "https://i.ibb.co/b2zz5hJ/green-32x32.png",
                                                "offsetEnd": "1px",
                                                "offsetBottom": "2px",
                                                "offsetTop": "3px"
                                            }
                                        ]
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "ลูกค้าเข้าตรวจ",
                                                "wrap": True,
                                                "color": "#808080",
                                                "size": "sm"
                                            },
                                            {
                                                "type": "text",
                                                "text": "126",
                                                "size": "sm",
                                                "align": "end",
                                                "offsetEnd": "-30px"
                                            },
                                            {
                                                "type": "text",
                                                "text": "84",
                                                "size": "sm",
                                                "align": "end",
                                                "offsetEnd": "10px"
                                            },
                                            {
                                                "type": "icon",
                                                "url": "https://i.ibb.co/ykFsNjm/red-32x32.png",
                                                "offsetEnd": "1px",
                                                "offsetBottom": "2px",
                                                "offsetTop": "3px"
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
                                                "wrap": True,
                                                "color": "#808080",
                                                "size": "sm"
                                            },
                                            {
                                                "type": "text",
                                                "text": "92",
                                                "size": "sm",
                                                "align": "end",
                                                "offsetEnd": "-30px"
                                            },
                                            {
                                                "type": "text",
                                                "text": "83",
                                                "size": "sm",
                                                "align": "end",
                                                "offsetEnd": "10px"
                                            },
                                            {
                                                "type": "icon",
                                                "url": "https://i.ibb.co/y0hQkxb/yellow-32x32.png",
                                                "offsetEnd": "1px",
                                                "offsetBottom": "2px",
                                                "offsetTop": "3px"
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
                                        "align": "center",
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
                                        "width": "32px",
                                        "height": "32px",
                                        "offsetTop": "1px",
                                        "offsetBottom": "3px",
                                        "offsetStart": "7px"
                                    }
                                ]
                            },
                            "styles": {
                                "hero": {
                                    "backgroundColor": "#000000",
                                    "separator": True
                                },
                                "footer": {
                                    "separator": True,
                                    "backgroundColor": "#000000"
                                }
                            }
                        },
                        {
                            "type": "bubble",
                            "hero": {
                                "type": "box",
                                "layout": "baseline",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "Lead Lag (LL)",
                                        "size": "xl",
                                        "color": "#FFFFFF",
                                        "weight": "bold",
                                        "offsetStart": "20px"
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
                                        "layout": "vertical",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "Week46",
                                                "weight": "bold",
                                                "color": "#808080"
                                            }
                                        ],
                                        "offsetEnd": "-73%"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "filler",
                                                "flex": 1
                                            },
                                            {
                                                "type": "text",
                                                "text": "Target",
                                                "align": "end",
                                                "offsetEnd": "-3px",
                                                "weight": "bold",
                                                "color": "#808080"
                                            },
                                            {
                                                "type": "text",
                                                "text": "Actual",
                                                "align": "end",
                                                "offsetEnd": "20px",
                                                "weight": "bold",
                                                "color": "#808080"
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
                                                "text": "Transfer",
                                                "wrap": True,
                                                "color": "#808080",
                                                "size": "sm"
                                            },
                                            {
                                                "type": "text",
                                                "text": "489M",
                                                "size": "sm",
                                                "align": "end",
                                                "offsetEnd": "-15px"
                                            },
                                            {
                                                "type": "text",
                                                "text": "474M",
                                                "size": "sm",
                                                "align": "end",
                                                "offsetEnd": "10px"
                                            },
                                            {
                                                "type": "icon",
                                                "url": "https://i.ibb.co/y0hQkxb/yellow-32x32.png",
                                                "offsetEnd": "1px",
                                                "offsetBottom": "2px",
                                                "offsetTop": "3px"
                                            }
                                        ]
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "Transfer",
                                                "size": "sm",
                                                "color": "#808080"
                                            },
                                            {
                                                "type": "text",
                                                "text": "72u",
                                                "size": "sm",
                                                "align": "end",
                                                "offsetEnd": "-15px"
                                            },
                                            {
                                                "type": "text",
                                                "text": "66u",
                                                "size": "sm",
                                                "align": "end",
                                                "offsetEnd": "10px"
                                            },
                                            {
                                                "type": "icon",
                                                "url": "https://i.ibb.co/ykFsNjm/red-32x32.png",
                                                "offsetEnd": "1px",
                                                "offsetBottom": "2px",
                                                "offsetTop": "3px"
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
                                                "text": "Grs. Presale",
                                                "wrap": True,
                                                "size": "sm",
                                                "color": "#808080"
                                            },
                                            {
                                                "type": "text",
                                                "text": "-",
                                                "size": "sm",
                                                "align": "end",
                                                "offsetEnd": "-15px"
                                            },
                                            {
                                                "type": "text",
                                                "text": "1,555M",
                                                "size": "sm",
                                                "align": "end",
                                                "offsetEnd": "10px"
                                            },
                                            {
                                                "type": "icon",
                                                "url": "https://i.ibb.co/b2zz5hJ/green-32x32.png",
                                                "offsetEnd": "1px",
                                                "offsetBottom": "2px",
                                                "offsetTop": "3px"
                                            }
                                        ]
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "Grs. Presale",
                                                "wrap": True,
                                                "size": "sm",
                                                "color": "#808080"
                                            },
                                            {
                                                "type": "text",
                                                "text": "-",
                                                "size": "sm",
                                                "align": "end",
                                                "offsetEnd": "-15px"
                                            },
                                            {
                                                "type": "text",
                                                "text": "185u",
                                                "size": "sm",
                                                "align": "end",
                                                "offsetEnd": "10px"
                                            },
                                            {
                                                "type": "icon",
                                                "url": "https://i.ibb.co/b2zz5hJ/green-32x32.png",
                                                "offsetEnd": "1px",
                                                "offsetBottom": "2px",
                                                "offsetTop": "3px"
                                            }
                                        ]
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "Net Presale",
                                                "wrap": True,
                                                "size": "sm",
                                                "color": "#808080"
                                            },
                                            {
                                                "type": "text",
                                                "text": "1,078M",
                                                "size": "sm",
                                                "align": "end",
                                                "offsetEnd": "-15px"
                                            },
                                            {
                                                "type": "text",
                                                "text": "982M",
                                                "size": "sm",
                                                "align": "end",
                                                "offsetEnd": "10px"
                                            },
                                            {
                                                "type": "icon",
                                                "url": "https://i.ibb.co/ykFsNjm/red-32x32.png",
                                                "offsetEnd": "1px",
                                                "offsetBottom": "2px",
                                                "offsetTop": "3px"
                                            }
                                        ]
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "Net Presale",
                                                "size": "sm",
                                                "color": "#808080",
                                                "wrap": True
                                            },
                                            {
                                                "type": "text",
                                                "text": "148u",
                                                "size": "sm",
                                                "align": "end",
                                                "offsetEnd": "-15px"
                                            },
                                            {
                                                "type": "text",
                                                "text": "114u",
                                                "size": "sm",
                                                "align": "end",
                                                "offsetEnd": "10px"
                                            },
                                            {
                                                "type": "icon",
                                                "url": "https://i.ibb.co/ykFsNjm/red-32x32.png",
                                                "offsetEnd": "1px",
                                                "offsetBottom": "2px",
                                                "offsetTop": "3px"
                                            }
                                        ]
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "N.Presale + P.Cancel",
                                                "wrap": True,
                                                "size": "sm",
                                                "color": "#808080"
                                            },
                                            {
                                                "type": "text",
                                                "text": "-",
                                                "size": "sm",
                                                "align": "end",
                                                "offsetEnd": "-15px"
                                            },
                                            {
                                                "type": "text",
                                                "text": "660M",
                                                "size": "sm",
                                                "align": "end",
                                                "offsetEnd": "10px"
                                            },
                                            {
                                                "type": "icon",
                                                "url": "https://i.ibb.co/b2zz5hJ/green-32x32.png",
                                                "offsetEnd": "1px",
                                                "offsetBottom": "2px",
                                                "offsetTop": "3px"
                                            }
                                        ]
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "N.Presale + P.Cancel",
                                                "wrap": True,
                                                "size": "sm",
                                                "color": "#808080"
                                            },
                                            {
                                                "type": "text",
                                                "text": "-",
                                                "size": "sm",
                                                "align": "end",
                                                "offsetEnd": "-15px"
                                            },
                                            {
                                                "type": "text",
                                                "text": "75u",
                                                "size": "sm",
                                                "align": "end",
                                                "offsetEnd": "10px"
                                            },
                                            {
                                                "type": "icon",
                                                "url": "https://i.ibb.co/b2zz5hJ/green-32x32.png",
                                                "offsetEnd": "1px",
                                                "offsetBottom": "2px",
                                                "offsetTop": "3px"
                                            }
                                        ]
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "Pre Cancel",
                                                "size": "sm",
                                                "color": "#808080"
                                            },
                                            {
                                                "type": "text",
                                                "text": "-",
                                                "size": "sm",
                                                "align": "end",
                                                "offsetEnd": "-15px"
                                            },
                                            {
                                                "type": "text",
                                                "text": "(322)M",
                                                "size": "sm",
                                                "align": "end",
                                                "offsetEnd": "10px"
                                            },
                                            {
                                                "type": "icon",
                                                "url": "https://i.ibb.co/ykFsNjm/red-32x32.png",
                                                "offsetEnd": "1px",
                                                "offsetBottom": "2px",
                                                "offsetTop": "3px"
                                            }
                                        ]
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "Pre Cancel",
                                                "wrap": True,
                                                "color": "#808080",
                                                "size": "sm"
                                            },
                                            {
                                                "type": "text",
                                                "text": "-",
                                                "size": "sm",
                                                "align": "end",
                                                "offsetEnd": "-15px"
                                            },
                                            {
                                                "type": "text",
                                                "text": "(39)u",
                                                "size": "sm",
                                                "align": "end",
                                                "offsetEnd": "10px"
                                            },
                                            {
                                                "type": "icon",
                                                "url": "https://i.ibb.co/ykFsNjm/red-32x32.png",
                                                "offsetEnd": "1px",
                                                "offsetBottom": "2px",
                                                "offsetTop": "3px"
                                            }
                                        ]
                                    },
                                    {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "All BG",
                                                "weight": "bold",
                                                "color": "#808080",
                                                "size": "lg"
                                            },
                                            {
                                                "type": "text",
                                                "text": "By Quarter",
                                                "wrap": True,
                                                "color": "#808080",
                                                "size": "xs"
                                            }
                                        ],
                                        "position": "absolute",
                                        "offsetTop": "1%",
                                        "offsetStart": "5%",
                                        "paddingAll": "2px"
                                    },
                                    {
                                        "type": "separator",
                                        "margin": "md"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "Walk",
                                                "wrap": True,
                                                "color": "#808080",
                                                "size": "sm"
                                            },
                                            {
                                                "type": "text",
                                                "text": "1,378",
                                                "size": "sm",
                                                "align": "end",
                                                "offsetEnd": "-30px"
                                            },
                                            {
                                                "type": "text",
                                                "text": "1,110",
                                                "size": "sm",
                                                "align": "end",
                                                "offsetEnd": "10px"
                                            },
                                            {
                                                "type": "icon",
                                                "url": "https://i.ibb.co/y0hQkxb/yellow-32x32.png",
                                                "offsetEnd": "1px",
                                                "offsetBottom": "2px",
                                                "offsetTop": "3px"
                                            }
                                        ]
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "2nd Walk++",
                                                "wrap": True,
                                                "color": "#808080",
                                                "size": "sm"
                                            },
                                            {
                                                "type": "text",
                                                "text": "354",
                                                "size": "sm",
                                                "align": "end",
                                                "offsetEnd": "-30px"
                                            },
                                            {
                                                "type": "text",
                                                "text": "278",
                                                "size": "sm",
                                                "align": "end",
                                                "offsetEnd": "10px"
                                            },
                                            {
                                                "type": "icon",
                                                "url": "https://i.ibb.co/ykFsNjm/red-32x32.png",
                                                "offsetEnd": "1px",
                                                "offsetBottom": "2px",
                                                "offsetTop": "3px"
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
                                                "wrap": True,
                                                "color": "#808080",
                                                "size": "sm"
                                            },
                                            {
                                                "type": "text",
                                                "text": "12",
                                                "size": "sm",
                                                "align": "end",
                                                "offsetEnd": "-30px"
                                            },
                                            {
                                                "type": "text",
                                                "text": "12",
                                                "size": "sm",
                                                "align": "end",
                                                "offsetEnd": "10px"
                                            },
                                            {
                                                "type": "icon",
                                                "url": "https://i.ibb.co/y0hQkxb/yellow-32x32.png",
                                                "offsetEnd": "1px",
                                                "offsetBottom": "2px",
                                                "offsetTop": "3px"
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
                                                "wrap": True,
                                                "color": "#808080",
                                                "size": "sm"
                                            },
                                            {
                                                "type": "text",
                                                "text": "112",
                                                "size": "sm",
                                                "align": "end",
                                                "offsetEnd": "-30px"
                                            },
                                            {
                                                "type": "text",
                                                "text": "164",
                                                "size": "sm",
                                                "align": "end",
                                                "offsetEnd": "10px"
                                            },
                                            {
                                                "type": "icon",
                                                "url": "https://i.ibb.co/b2zz5hJ/green-32x32.png",
                                                "offsetEnd": "1px",
                                                "offsetBottom": "2px",
                                                "offsetTop": "3px"
                                            }
                                        ]
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "ลูกค้าเข้าตรวจ",
                                                "wrap": True,
                                                "color": "#808080",
                                                "size": "sm"
                                            },
                                            {
                                                "type": "text",
                                                "text": "126",
                                                "size": "sm",
                                                "align": "end",
                                                "offsetEnd": "-30px"
                                            },
                                            {
                                                "type": "text",
                                                "text": "84",
                                                "size": "sm",
                                                "align": "end",
                                                "offsetEnd": "10px"
                                            },
                                            {
                                                "type": "icon",
                                                "url": "https://i.ibb.co/ykFsNjm/red-32x32.png",
                                                "offsetEnd": "1px",
                                                "offsetBottom": "2px",
                                                "offsetTop": "3px"
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
                                                "wrap": True,
                                                "color": "#808080",
                                                "size": "sm"
                                            },
                                            {
                                                "type": "text",
                                                "text": "92",
                                                "size": "sm",
                                                "align": "end",
                                                "offsetEnd": "-30px"
                                            },
                                            {
                                                "type": "text",
                                                "text": "83",
                                                "size": "sm",
                                                "align": "end",
                                                "offsetEnd": "10px"
                                            },
                                            {
                                                "type": "icon",
                                                "url": "https://i.ibb.co/y0hQkxb/yellow-32x32.png",
                                                "offsetEnd": "1px",
                                                "offsetBottom": "2px",
                                                "offsetTop": "3px"
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
                                        "align": "center",
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
                                        "width": "32px",
                                        "height": "32px",
                                        "offsetTop": "1px",
                                        "offsetBottom": "3px",
                                        "offsetStart": "7px"
                                    }
                                ]
                            },
                            "styles": {
                                "hero": {
                                    "backgroundColor": "#000000",
                                    "separator": True
                                },
                                "footer": {
                                    "separator": True,
                                    "backgroundColor": "#000000"
                                }
                            }
                        }
                    ]
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
