# -*- coding: utf-8 -*-

import requests
import json
from config import LINE_API
from models.crm_line_exct_report import ExecutiveReportModel


def replyMsg(Reply_token: str =None, ex: ExecutiveReportModel = None, line_Acees_Token: str = None):
    authorization = 'Bearer {}'.format(line_Acees_Token)
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization': authorization
    }
    # print(ex.text_msg_detail)
    # print(ex.text_msg_header)
    # print(f"{ex.bg1_cancelunit:,.0f}")
    # print(f"{ex.bg1_cancelamount:,.2f}")

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
                        "layout": "horizontal",
                        "contents": [
                            {
                                "type": "text",
                                "text": "Executive Report",
                                "size": "lg",
                                "color": "#FFFFFF"
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": ex.text_msg_header,
                                        "color": "#FFFFFF",
                                        "align": "end",
                                        "gravity": "bottom",
                                        "size": "sm",
                                        "flex": 1
                                    },
                                    {
                                        "type": "text",
                                        "text": ex.text_msg_detail,
                                        "align": "end",
                                        "color": "#FFFFFF",
                                        "size": "xxs",
                                        "flex": 0,
                                        "style": "italic"
                                    }
                                ],
                                "flex": 0,
                                "height": "32px"
                            }
                        ]
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
                                        "align": "center",
                                        "color": "#FFFFFF"
                                    }
                                ],
                                "backgroundColor": "#c92028"
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
                                        "text": "Vol. (MB)",
                                        "size": "xs",
                                        "align": "end",
                                        "weight": "bold"
                                    }
                                ],
                                "backgroundColor": "#E8E16F"
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
                                        "align": "start",
                                        "offsetStart": "50px"
                                    },
                                    {
                                        "type": "text",
                                        "text": f"{ex.bg1_grosspresalesunit:,.0f}",
                                        "size": "xs",
                                        "align": "end"
                                    },
                                    {
                                        "type": "text",
                                        "text": f"{ex.bg1_grosspresalesamount:,.2f}",
                                        "size": "xs",
                                        "align": "end"
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
                                        "align": "start",
                                        "offsetStart": "50px"
                                    },
                                    {
                                        "type": "text",
                                        "text": f"{ex.bg2_grosspresalesunit:,.0f}",
                                        "size": "xs",
                                        "align": "end"
                                    },
                                    {
                                        "type": "text",
                                        "text": f"{ex.bg2_grosspresalesamount:,.2f}",
                                        "size": "xs",
                                        "align": "end"
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
                                        "align": "start",
                                        "offsetStart": "50px"
                                    },
                                    {
                                        "type": "text",
                                        "text": f"{ex.bg3_grosspresalesunit:,.0f}",
                                        "size": "xs",
                                        "align": "end"
                                    },
                                    {
                                        "type": "text",
                                        "text": f"{ex.bg3_grosspresalesamount:,.2f}",
                                        "size": "xs",
                                        "align": "end"
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
                                        "align": "start",
                                        "offsetStart": "50px"
                                    },
                                    {
                                        "type": "text",
                                        "text": f"{ex.bg4_grosspresalesunit:,.0f}",
                                        "size": "xs",
                                        "align": "end"
                                    },
                                    {
                                        "type": "text",
                                        "text": f"{ex.bg4_grosspresalesamount:,.2f}",
                                        "size": "xs",
                                        "align": "end"
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
                                        "size": "sm",
                                        "align": "end",
                                        "weight": "bold"
                                    },
                                    {
                                        "type": "text",
                                        "text": f"{ex.total_grosspresalesunit:,.0f}",
                                        "size": "sm",
                                        "align": "end",
                                        "weight": "bold"
                                    },
                                    {
                                        "type": "text",
                                        "text": f"{ex.total_grosspresalesamount:,.2f}",
                                        "size": "sm",
                                        "align": "end",
                                        "weight": "bold"
                                    }
                                ],
                                "backgroundColor": "#7AFF97"
                            },
                            {
                                "type": "separator",
                                "margin": "xs"
                            },
                            {
                                "type": "box",
                                "layout": "baseline",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": ":: Cancel ::",
                                        "size": "md",
                                        "weight": "bold",
                                        "align": "center",
                                        "color": "#FFFFFF"
                                    }
                                ],
                                "margin": "md",
                                "backgroundColor": "#c92028"
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
                                        "text": "Vol. (MB)",
                                        "size": "xs",
                                        "align": "end",
                                        "weight": "bold"
                                    }
                                ],
                                "backgroundColor": "#E8E16F"
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
                                        "align": "start",
                                        "offsetStart": "50px"
                                    },
                                    {
                                        "type": "text",
                                        "text": f"{ex.bg1_cancelunit:,.0f}",
                                        "size": "xs",
                                        "align": "end"
                                    },
                                    {
                                        "type": "text",
                                        "text": f"{ex.bg1_cancelamount:,.2f}",
                                        "size": "xs",
                                        "align": "end"
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
                                        "align": "start",
                                        "offsetStart": "50px"
                                    },
                                    {
                                        "type": "text",
                                        "text": f"{ex.bg2_cancelunit:,.0f}",
                                        "size": "xs",
                                        "align": "end"
                                    },
                                    {
                                        "type": "text",
                                        "text": f"{ex.bg2_cancelamount:,.2f}",
                                        "size": "xs",
                                        "align": "end"
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
                                        "align": "start",
                                        "offsetStart": "50px"
                                    },
                                    {
                                        "type": "text",
                                        "text": f"{ex.bg3_cancelunit:,.0f}",
                                        "size": "xs",
                                        "align": "end"
                                    },
                                    {
                                        "type": "text",
                                        "text": f"{ex.bg3_cancelamount:,.2f}",
                                        "size": "xs",
                                        "align": "end"
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
                                        "align": "start",
                                        "offsetStart": "50px"
                                    },
                                    {
                                        "type": "text",
                                        "text": f"{ex.bg4_cancelunit:,.0f}",
                                        "size": "xs",
                                        "align": "end"
                                    },
                                    {
                                        "type": "text",
                                        "text": f"{ex.bg4_cancelamount:,.2f}",
                                        "size": "xs",
                                        "align": "end"
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
                                        "size": "sm",
                                        "align": "end",
                                        "weight": "bold"
                                    },
                                    {
                                        "type": "text",
                                        "text": f"{ex.total_cancelunit:,.0f}",
                                        "size": "sm",
                                        "align": "end",
                                        "weight": "bold"
                                    },
                                    {
                                        "type": "text",
                                        "text": f"{ex.total_cancelamount:,.2f}",
                                        "size": "sm",
                                        "align": "end",
                                        "weight": "bold"
                                    }
                                ],
                                "backgroundColor": "#7AFF97"
                            },
                            {
                                "type": "separator",
                                "margin": "xs"
                            },
                            {
                                "type": "box",
                                "layout": "baseline",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": ":: Net Price ::",
                                        "size": "md",
                                        "weight": "bold",
                                        "align": "center",
                                        "color": "#FFFFFF"
                                    }
                                ],
                                "margin": "md",
                                "backgroundColor": "#c92028"
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
                                        "text": "Vol. (MB)",
                                        "size": "xs",
                                        "align": "end",
                                        "weight": "bold"
                                    }
                                ],
                                "backgroundColor": "#E8E16F"
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
                                        "align": "start",
                                        "offsetStart": "50px"
                                    },
                                    {
                                        "type": "text",
                                        "text": f"{ex.bg1_netpresalesunit:,.0f}",
                                        "size": "xs",
                                        "align": "end"
                                    },
                                    {
                                        "type": "text",
                                        "text": f"{ex.bg1_netpresalesamount:,.2f}",
                                        "size": "xs",
                                        "align": "end"
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
                                        "align": "start",
                                        "offsetStart": "50px"
                                    },
                                    {
                                        "type": "text",
                                        "text": f"{ex.bg2_netpresalesunit:,.0f}",
                                        "size": "xs",
                                        "align": "end"
                                    },
                                    {
                                        "type": "text",
                                        "text": f"{ex.bg2_netpresalesamount:,.2f}",
                                        "size": "xs",
                                        "align": "end"
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
                                        "align": "start",
                                        "offsetStart": "50px"
                                    },
                                    {
                                        "type": "text",
                                        "text": f"{ex.bg3_netpresalesunit:,.0f}",
                                        "size": "xs",
                                        "align": "end"
                                    },
                                    {
                                        "type": "text",
                                        "text": f"{ex.bg3_netpresalesamount:,.2f}",
                                        "size": "xs",
                                        "align": "end"
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
                                        "align": "start",
                                        "offsetStart": "50px"
                                    },
                                    {
                                        "type": "text",
                                        "text": f"{ex.bg4_netpresalesunit:,.0f}",
                                        "size": "xs",
                                        "align": "end"
                                    },
                                    {
                                        "type": "text",
                                        "text": f"{ex.bg4_netpresalesamount:,.2f}",
                                        "size": "xs",
                                        "align": "end"
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
                                        "size": "sm",
                                        "align": "end",
                                        "weight": "bold"
                                    },
                                    {
                                        "type": "text",
                                        "text": f"{ex.total_netpresalesunit:,.0f}",
                                        "size": "sm",
                                        "align": "end",
                                        "weight": "bold"
                                    },
                                    {
                                        "type": "text",
                                        "text": f"{ex.total_netpresalesamount:,.2f}",
                                        "size": "sm",
                                        "align": "end",
                                        "weight": "bold"
                                    }
                                ],
                                "backgroundColor": "#7AFF97"
                            },
                            {
                                "type": "separator",
                                "margin": "xs"
                            },
                            {
                                "type": "box",
                                "layout": "baseline",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": ":: Transfer ::",
                                        "size": "md",
                                        "weight": "bold",
                                        "align": "center",
                                        "color": "#FFFFFF"
                                    }
                                ],
                                "margin": "md",
                                "backgroundColor": "#c92028"
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
                                        "text": "Vol. (MB)",
                                        "size": "xs",
                                        "align": "end",
                                        "weight": "bold"
                                    }
                                ],
                                "backgroundColor": "#E8E16F"
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
                                        "align": "start",
                                        "offsetStart": "50px"
                                    },
                                    {
                                        "type": "text",
                                        "text": f"{ex.bg1_transferunit:,.0f}",
                                        "size": "xs",
                                        "align": "end"
                                    },
                                    {
                                        "type": "text",
                                        "text": f"{ex.bg1_transferamount:,.2f}",
                                        "size": "xs",
                                        "align": "end"
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
                                        "align": "start",
                                        "offsetStart": "50px"
                                    },
                                    {
                                        "type": "text",
                                        "text": f"{ex.bg2_transferunit:,.0f}",
                                        "size": "xs",
                                        "align": "end"
                                    },
                                    {
                                        "type": "text",
                                        "text": f"{ex.bg2_transferamount:,.2f}",
                                        "size": "xs",
                                        "align": "end"
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
                                        "align": "start",
                                        "offsetStart": "50px"
                                    },
                                    {
                                        "type": "text",
                                        "text": f"{ex.bg3_transferunit:,.0f}",
                                        "size": "xs",
                                        "align": "end"
                                    },
                                    {
                                        "type": "text",
                                        "text": f"{ex.bg3_transferamount:,.2f}",
                                        "size": "xs",
                                        "align": "end"
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
                                        "align": "start",
                                        "offsetStart": "50px"
                                    },
                                    {
                                        "type": "text",
                                        "text": f"{ex.bg4_transferunit:,.0f}",
                                        "size": "xs",
                                        "align": "end"
                                    },
                                    {
                                        "type": "text",
                                        "text": f"{ex.bg4_transferamount:,.2f}",
                                        "size": "xs",
                                        "align": "end"
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
                                        "size": "sm",
                                        "align": "end",
                                        "weight": "bold"
                                    },
                                    {
                                        "type": "text",
                                        "text": f"{ex.total_transferunit:,.0f}",
                                        "size": "sm",
                                        "align": "end",
                                        "weight": "bold"
                                    },
                                    {
                                        "type": "text",
                                        "text": f"{ex.total_transferamount:,.2f}",
                                        "size": "sm",
                                        "align": "end",
                                        "weight": "bold"
                                    }
                                ],
                                "backgroundColor": "#7AFF97"
                            },
                            {
                                "type": "separator",
                                "margin": "xs"
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
