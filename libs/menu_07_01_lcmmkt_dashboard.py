# -*- coding: utf-8 -*-

import requests
import json
from config import LINE_API, TABLEAU_URL

from models.chatbot_mst_user import MstUserModel

from string import Template

from models.chatbot_mst_conf import MstMsgConfigModel
from schemas.chatbot_mst_conf import MstMsgConfSchema


def replyMsg(Reply_token: str = None, user: MstUserModel = None, userId: str = None, line_Acees_Token: str = None):
    authorization = f'Bearer {line_Acees_Token}'
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization': authorization
    }

    subbg = user.user_sub_no

    bg = user.user_sub_no[0].strip()
    # print(bg)
    ptypeBG = None
    if bg:
        # print(bg)
        if bg == '1':
            ptypeBG = '1.SDH'
        elif bg == '2':
            ptypeBG = '2.TH'
        elif bg == '3':
            ptypeBG = '3.CD1'
        elif bg == '4':
            ptypeBG = '4.CD2'
    else:
        print('Empty')

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
                                "text": "Please select Dashboard",
                                "color": "#FFFFFF",
                                "offsetStart": "5%"
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
                                        "url": "https://drive.google.com/uc?id=1ZbalrMFQuLk7Ldb8c-uzOld5j7evgjeL",
                                        "size": "full",
                                        "aspectMode": "fit",
                                        "aspectRatio": "24:7",
                                        "action": {
                                            "type": "uri",
                                            "label": "action",
                                            "uri": f"{TABLEAU_URL}/walksummary?userId={userId}"
                                        }
                                    }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "image",
                                        "url": "https://drive.google.com/uc?id=11Ky9LzWp2CYpv9FFUNXYsQql4EBxCyUa",
                                        "size": "full",
                                        "aspectMode": "fit",
                                        "aspectRatio": "24:7",
                                        "action": {
                                            "type": "uri",
                                            "label": "action",
                                            "uri": f"{TABLEAU_URL}/walkbyproj?pTypeDesc={ptypeBG}&ProjectGroup={subbg}&userId={userId}"
                                        }
                                    }
                                ]
                            },
                            {
                                "type": "separator",
                                "margin": "sm"
                            }
                        ]
                    },
                    "footer": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "text",
                                "text": "Copyright 2019 AP PCL.",
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


def replyMsgDB(Reply_token: str = None, user: MstUserModel = None, userId: str = None, line_Acees_Token: str = None,
               msg_value: str = None, user_type: str = None):
    authorization = f'Bearer {line_Acees_Token}'
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization': authorization
    }

    subbg = user.user_sub_no

    bg = user.user_sub_no[0].strip()
    ptypeBG = None
    if bg:
        if bg == '1':
            ptypeBG = '1.SDH'
        elif bg == '2':
            ptypeBG = '2.TH'
        elif bg == '3':
            ptypeBG = '3.CD1'
        elif bg == '4':
            ptypeBG = '4.CD2'
    else:
        print('Empty')

    msg = MstMsgConfigModel.find_by_msg_value_ds(msg_value, user_type)
    msg_schema = MstMsgConfSchema().dumps(msg)

    msg_obj = json.loads(msg_schema)

    template = Template(msg_obj['msg_json'])
    msg_json = template.substitute(TABLEAU_URL=TABLEAU_URL, userId=userId, ptypeBG=ptypeBG, subbg=subbg)

    type_msg = json.loads(msg_json)

    data = {
        "replyToken": Reply_token,
        "messages": [
            type_msg
        ]
    }

    session = requests.Session()
    response = session.post(LINE_API, data=json.dumps(data), headers=headers)
    return response, 201
