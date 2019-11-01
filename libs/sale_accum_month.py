import os
import re
import requests
import json
from config import LINE_API
from models.sp_crm_sale_m_accum import SaleMonthAccumModel


def replyMsg(Reply_token, TextMessage, line_Acees_Token):
    authorization = 'Bearer {}'.format(line_Acees_Token)
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization': authorization
    }

    sma_models = SaleMonthAccumModel()
    return_value = sma_models.sp_crm_sale_m_accum(0)
    print(return_value.NetTransfer, return_value.TransferUnit)
    # print(value[0], value[1])


    text_header = "Accumulate Sales Oct'19"
    total_gross_sale_amnt_hedr = "฿ 3,599M"
    total_gross_sale_amnt_detl = "฿ 3,519,894,522"
    total_cancel_amnt_detl = "฿ 1,729,575,441"
    total_agreement_amnt_detl = "฿ 2,846,496,261"
    # total_transfer_amnt_detl = "฿ 1,364,440,309"
    total_transfer_amnt_detl = return_value.NetTransfer
    timestamps = "2019.10.31 12:47 (GMT+0700)"
    type_msg = \
        {
            "type": "flex",
            "altText": "Flex Message",
            "contents": {
                "type": "bubble",
                "direction": "ltr",
                "header": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "text",
                            "text": text_header,
                            "size": "lg",
                            "align": "start",
                            "weight": "bold",
                            "color": "#C92028"
                        },
                        {
                            "type": "text",
                            "text": total_gross_sale_amnt_hedr,
                            "size": "3xl",
                            "weight": "bold",
                            "color": "#000000"
                        },
                        {
                            "type": "text",
                            "text": "Total Gross Sale",
                            "size": "lg",
                            "weight": "bold",
                            "color": "#000000"
                        },
                        {
                            "type": "text",
                            "text": timestamps,
                            "size": "xs",
                            "color": "#B2B2B2"
                        },
                        {
                            "type": "text",
                            "text": "All Project @APTHAI",
                            "margin": "lg",
                            "size": "lg",
                            "color": "#000000"
                        }
                    ]
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "separator",
                            "color": "#C3C3C3"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": "Gross Sales",
                                    "color": "#C3C3C3"
                                },
                                {
                                    "type": "text",
                                    "text": total_gross_sale_amnt_detl,
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
                                    "text": "Cancel",
                                    "color": "#C3C3C3"
                                },
                                {
                                    "type": "text",
                                    "text": total_cancel_amnt_detl,
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
                                    "text": "Agreement",
                                    "color": "#C3C3C3"
                                },
                                {
                                    "type": "text",
                                    "text": total_agreement_amnt_detl,
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
                                    "text": "Transfer",
                                    "color": "#C3C3C3"
                                },
                                {
                                    "type": "text",
                                    "text": total_transfer_amnt_detl,
                                    "align": "end"
                                }
                            ]
                        },
                        {
                            "type": "separator",
                            "margin": "lg",
                            "color": "#C3C3C3"
                        }
                    ]
                },
                "footer": {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                        {
                            "type": "text",
                            "text": "View Details",
                            "size": "lg",
                            "align": "center",
                            "color": "#0084B6",
                            "action": {
                                "type": "uri",
                                "label": "View Details",
                                "uri": "https://google.co.th/"
                            }
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
    return response
