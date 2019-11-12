# -*- coding: utf-8 -*-

import os
import re
import requests
import json
from config import LINE_API
from models.sp_crm_sale_m_accum import SaleMonthAccumModel
from libs import chatbot_helper
import datetime


def replyMsg(Reply_token: str =None, TextMessage: str = None, param_month: str = None, line_Acees_Token: str = None):
    authorization = 'Bearer {}'.format(line_Acees_Token)
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization': authorization
    }


    sma_models = SaleMonthAccumModel()
    return_value = sma_models.sp_crm_sale_m_accum(param_month)
    # print(return_value.NetTransfer, return_value.TransferUnit, return_value.NetAgreement, return_value.AgreementUnit,
    #       return_value.NetBooking, return_value.BookingUnit,
    #       return_value.NetCancelBooking, return_value.CancelUnit, return_value.NetBookingM, return_value.MonthSelect)


    text_header = "Accumulate Sales {}".format(return_value.MonthSelect)
    total_gross_sale_amnt_hedr = return_value.NetBookingM
    total_gross_sale_amnt_detl = return_value.NetBooking
    total_cancel_amnt_detl = return_value.NetCancelBooking
    total_agreement_amnt_detl = return_value.NetAgreement
    # total_transfer_amnt_detl = "฿ 1,364,440,309"
    total_transfer_amnt_detl = return_value.NetTransfer
    # timestamps = "2019.10.31 12:47 (GMT+0700)"
    timestamps = datetime.datetime.now().strftime("%Y.%m.%d %H:%M (GMT+0700)")
    # type_msg = \
    #     {
    #         "type": "flex",
    #         "altText": "Flex Message",
    #         "contents": {
    #             "type": "bubble",
    #             "direction": "ltr",
    #             "header": {
    #                 "type": "box",
    #                 "layout": "vertical",
    #                 "contents": [
    #                     {
    #                         "type": "text",
    #                         "text": text_header,
    #                         "size": "lg",
    #                         "align": "start",
    #                         "weight": "bold",
    #                         "color": "#C92028"
    #                     },
    #                     {
    #                         "type": "text",
    #                         "text": total_gross_sale_amnt_hedr,
    #                         "size": "3xl",
    #                         "weight": "bold",
    #                         "color": "#000000"
    #                     },
    #                     {
    #                         "type": "text",
    #                         "text": "Total Gross Sale",
    #                         "size": "lg",
    #                         "weight": "bold",
    #                         "color": "#000000"
    #                     },
    #                     {
    #                         "type": "text",
    #                         "text": timestamps,
    #                         "size": "xs",
    #                         "color": "#B2B2B2"
    #                     },
    #                     {
    #                         "type": "text",
    #                         "text": "All Project @APTHAI",
    #                         "margin": "lg",
    #                         "size": "lg",
    #                         "color": "#000000"
    #                     }
    #                 ]
    #             },
    #             "body": {
    #                 "type": "box",
    #                 "layout": "vertical",
    #                 "contents": [
    #                     {
    #                         "type": "separator",
    #                         "color": "#C3C3C3"
    #                     },
    #                     {
    #                         "type": "box",
    #                         "layout": "baseline",
    #                         "contents": [
    #                             {
    #                                 "type": "text",
    #                                 "text": "Gross Sales",
    #                                 "color": "#C3C3C3"
    #                             },
    #                             {
    #                                 "type": "text",
    #                                 "text": total_gross_sale_amnt_detl,
    #                                 "align": "end"
    #                             }
    #                         ]
    #                     },
    #                     {
    #                         "type": "box",
    #                         "layout": "baseline",
    #                         "contents": [
    #                             {
    #                                 "type": "text",
    #                                 "text": "Cancel",
    #                                 "color": "#C3C3C3"
    #                             },
    #                             {
    #                                 "type": "text",
    #                                 "text": total_cancel_amnt_detl,
    #                                 "align": "end"
    #                             }
    #                         ]
    #                     },
    #                     {
    #                         "type": "box",
    #                         "layout": "baseline",
    #                         "contents": [
    #                             {
    #                                 "type": "text",
    #                                 "text": "Agreement",
    #                                 "color": "#C3C3C3"
    #                             },
    #                             {
    #                                 "type": "text",
    #                                 "text": total_agreement_amnt_detl,
    #                                 "align": "end"
    #                             }
    #                         ]
    #                     },
    #                     {
    #                         "type": "box",
    #                         "layout": "baseline",
    #                         "contents": [
    #                             {
    #                                 "type": "text",
    #                                 "text": "Transfer",
    #                                 "color": "#C3C3C3"
    #                             },
    #                             {
    #                                 "type": "text",
    #                                 "text": total_transfer_amnt_detl,
    #                                 "align": "end"
    #                             }
    #                         ]
    #                     },
    #                     {
    #                         "type": "separator",
    #                         "margin": "lg",
    #                         "color": "#C3C3C3"
    #                     }
    #                 ]
    #             },
    #             "footer": {
    #                 "type": "box",
    #                 "layout": "horizontal",
    #                 "contents": [
    #                     {
    #                         "type": "image",
    #                         "url": "https://www.intellyticshub.com/assets/img/tableau.jpg",
    #                         "align": "center",
    #                         "size": "full",
    #                         "aspectRatio": "1.51:1",
    #                         "aspectMode": "cover"
    #                     }
    #                 ]
    #             }
    #         }
    #     }

    type_msg = \
        {
            "type": "flex",
            "altText": "Flex Message",
            "contents":
                {
                    "type": "bubble",
                    "size": "giga",
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
                                        "text": "QTD",
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
                                        "type": "filler"
                                    },
                                    {
                                        "type": "text",
                                        "text": "Target",
                                        "align": "end",
                                        "offsetEnd": "-20px",
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
                                        "text": "Transfer (M)",
                                        "wrap": True,
                                        "color": "#C3C3C3",
                                        "size": "sm"
                                    },
                                    {
                                        "type": "text",
                                        "text": "488.66",
                                        "size": "sm",
                                        "align": "end",
                                        "offsetEnd": "-30px"
                                    },
                                    {
                                        "type": "text",
                                        "text": "473.56",
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
                                        "text": "Grs. Presale(M)",
                                        "wrap": True,
                                        "size": "sm",
                                        "color": "#C3C3C3"
                                    },
                                    {
                                        "type": "text",
                                        "text": "-",
                                        "size": "sm",
                                        "align": "end",
                                        "offsetEnd": "-30px"
                                    },
                                    {
                                        "type": "text",
                                        "text": "1,554.87",
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
                                        "text": "Net Presales (M)",
                                        "wrap": True,
                                        "size": "sm",
                                        "color": "#C3C3C3"
                                    },
                                    {
                                        "type": "text",
                                        "text": "1,078.45",
                                        "size": "sm",
                                        "align": "end",
                                        "offsetEnd": "-30px"
                                    },
                                    {
                                        "type": "text",
                                        "text": "981.53",
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
                                        "text": "Net Presales + Pre-Cancel (M)",
                                        "wrap": True,
                                        "size": "sm",
                                        "color": "#C3C3C3"
                                    },
                                    {
                                        "type": "text",
                                        "text": "-",
                                        "size": "sm",
                                        "align": "end",
                                        "offsetEnd": "-30px"
                                    },
                                    {
                                        "type": "text",
                                        "text": "659.93",
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
                                        "text": "Pre-Cancel (M)",
                                        "size": "sm",
                                        "color": "#C3C3C3"
                                    },
                                    {
                                        "type": "text",
                                        "text": "-",
                                        "size": "sm",
                                        "align": "end",
                                        "offsetEnd": "-30px"
                                    },
                                    {
                                        "type": "text",
                                        "text": "(321.6)",
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
                                "type": "separator",
                                "margin": "md"
                            },
                            {
                                "type": "box",
                                "layout": "baseline",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "Transfer (U.)",
                                        "size": "sm",
                                        "color": "#C3C3C3"
                                    },
                                    {
                                        "type": "text",
                                        "text": "72",
                                        "size": "sm",
                                        "align": "end",
                                        "offsetEnd": "-30px"
                                    },
                                    {
                                        "type": "text",
                                        "text": "66",
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
                                        "text": "Grs. Presale (U.)",
                                        "wrap": True,
                                        "size": "sm",
                                        "color": "#C3C3C3"
                                    },
                                    {
                                        "type": "text",
                                        "text": "-",
                                        "size": "sm",
                                        "align": "end",
                                        "offsetEnd": "-30px"
                                    },
                                    {
                                        "type": "text",
                                        "text": "185",
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
                                        "text": "Net Presales (U.)",
                                        "size": "sm",
                                        "color": "#C3C3C3",
                                        "wrap": True
                                    },
                                    {
                                        "type": "text",
                                        "text": "148",
                                        "size": "sm",
                                        "align": "end",
                                        "offsetEnd": "-30px"
                                    },
                                    {
                                        "type": "text",
                                        "text": "114",
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
                                        "text": "Net Presales + Pre-Cancel (U)",
                                        "wrap": True,
                                        "size": "sm",
                                        "color": "#C3C3C3"
                                    },
                                    {
                                        "type": "text",
                                        "text": "-",
                                        "size": "sm",
                                        "align": "end",
                                        "offsetEnd": "-30px"
                                    },
                                    {
                                        "type": "text",
                                        "text": "75",
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
                                        "text": "Pre-Cancel (U.)",
                                        "wrap": True,
                                        "color": "#C3C3C3",
                                        "size": "sm"
                                    },
                                    {
                                        "type": "text",
                                        "text": "-",
                                        "size": "sm",
                                        "align": "end",
                                        "offsetEnd": "-30px"
                                    },
                                    {
                                        "type": "text",
                                        "text": "(39)",
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
                                        "text": "Lead Indicator",
                                        "weight": "bold",
                                        "size": "xl",
                                        "color": "#c92028",
                                        "decoration": "underline"
                                    }
                                ],
                                "position": "absolute",
                                "offsetTop": "3%",
                                "offsetStart": "5%"
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": ":: Total  BG1 : SDH ::",
                                        "weight": "bold",
                                        "color": "#808080"
                                    }
                                ],
                                "position": "absolute",
                                "offsetTop": "11%",
                                "offsetStart": "5%",
                                "paddingAll": "2px"
                            }
                        ]
                    },
                    "footer": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "separator"
                            },
                            {
                                "type": "text",
                                "text": "2019.10.31 12:47 (GMT+0700)",
                                "size": "xxs",
                                "color": "#B2B2B2",
                                "align": "end",
                                "offsetEnd": "4%"
                            }
                        ]
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
