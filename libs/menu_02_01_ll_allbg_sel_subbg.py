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
                    "size": "giga",
                    "hero": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "text",
                                "text": "Select Sub BG",
                                "color": "#FFFFFF",
                                "align": "center"
                            }
                        ]
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "separator",
                                "margin": "sm"
                            },
                            {
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                    {
                                        "type": "image",
                                        "url": "https://i.ibb.co/xGsrVSW/SDH-v1-0.png"
                                    },
                                    {
                                        "type": "image",
                                        "url": "https://i.ibb.co/f91tLWB/subbg-v2-0-1-1.png",
                                        "action": {
                                            "type": "message",
                                            "label": "action",
                                            "text": "LL BY SubBG SDH[1.1]"
                                        }
                                    },
                                    {
                                        "type": "image",
                                        "url": "https://i.ibb.co/GWWQNBV/subbg-v2-0-1-2.png",
                                        "action": {
                                            "type": "message",
                                            "label": "action",
                                            "text": "LL BY SubBG SDH[1.2]"
                                        }
                                    },
                                    {
                                        "type": "image",
                                        "url": "https://i.ibb.co/By0Lv03/subbg-v2-0-1-3.png",
                                        "action": {
                                            "type": "message",
                                            "label": "action",
                                            "text": "LL BY SubBG SDH[1.3]"
                                        }
                                    },
                                    {
                                        "type": "image",
                                        "url": "https://i.ibb.co/LgYyk46/subbg-v2-0-4-3.png"
                                    }
                                ]
                            },
                            {
                                "type": "separator",
                                "margin": "sm"
                            },
                            {
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                    {
                                        "type": "image",
                                        "url": "https://i.ibb.co/BwwnZy2/TH-v1-0.png"
                                    },
                                    {
                                        "type": "image",
                                        "url": "https://i.ibb.co/kyD1nDz/subbg-v2-0-2-1.png",
                                        "action": {
                                            "type": "message",
                                            "label": "action",
                                            "text": "LL BY SubBG TH[2.1]"
                                        }
                                    },
                                    {
                                        "type": "image",
                                        "url": "https://i.ibb.co/jhDFdyK/subbg-v2-0-2-2.png",
                                        "action": {
                                            "type": "message",
                                            "label": "action",
                                            "text": "LL BY SubBG TH[2.2]"
                                        }
                                    },
                                    {
                                        "type": "image",
                                        "url": "https://i.ibb.co/zfXTf4D/subbg-v2-0-2-3.png",
                                        "action": {
                                            "type": "message",
                                            "label": "action",
                                            "text": "LL BY SubBG TH[2.3]"
                                        }
                                    },
                                    {
                                        "type": "image",
                                        "url": "https://i.ibb.co/GQpVP3y/subbg-v2-0-2-4.png",
                                        "action": {
                                            "type": "message",
                                            "label": "action",
                                            "text": "LL BY SubBG TH[2.4]"
                                        }
                                    }
                                ],
                                "margin": "sm"
                            },
                            {
                                "type": "separator",
                                "margin": "sm"
                            },
                            {
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                    {
                                        "type": "image",
                                        "url": "https://i.ibb.co/N37BhXJ/CD1-v1-0.png"
                                    },
                                    {
                                        "type": "image",
                                        "url": "https://i.ibb.co/hLKTSck/subbg-v2-0-3-1.png",
                                        "action": {
                                            "type": "message",
                                            "label": "action",
                                            "text": "LL BY SubBG CD1[3.1]"
                                        }
                                    },
                                    {
                                        "type": "image",
                                        "url": "https://i.ibb.co/4Y6QJsr/subbg-v2-0-3-2.png",
                                        "action": {
                                            "type": "message",
                                            "label": "action",
                                            "text": "LL BY SubBG CD1[3.2]"
                                        }
                                    },
                                    {
                                        "type": "image",
                                        "url": "https://i.ibb.co/7g7FcWd/subbg-v2-0-3-3.png",
                                        "action": {
                                            "type": "message",
                                            "label": "action",
                                            "text": "LL BY SubBG CD1[3.3]"
                                        }
                                    },
                                    {
                                        "type": "image",
                                        "url": "https://i.ibb.co/LgYyk46/subbg-v2-0-4-3.png"
                                    }
                                ],
                                "margin": "sm"
                            },
                            {
                                "type": "separator",
                                "margin": "sm"
                            },
                            {
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                    {
                                        "type": "image",
                                        "url": "https://i.ibb.co/b6h6LPL/CD2-v1-0.png"
                                    },
                                    {
                                        "type": "image",
                                        "url": "https://i.ibb.co/GnhpZzq/subbg-v2-0-4-1.png",
                                        "action": {
                                            "type": "message",
                                            "label": "action",
                                            "text": "LL BY SubBG CD2[4.1]"
                                        }
                                    },
                                    {
                                        "type": "image",
                                        "url": "https://i.ibb.co/QvvqP78/subbg-v2-0-4-2.png",
                                        "action": {
                                            "type": "message",
                                            "label": "action",
                                            "text": "LL BY SubBG CD2[4.2]"
                                        }
                                    },
                                    {
                                        "type": "image",
                                        "url": "https://i.ibb.co/LgYyk46/subbg-v2-0-4-3.png"
                                    },
                                    {
                                        "type": "image",
                                        "url": "https://i.ibb.co/LgYyk46/subbg-v2-0-4-3.png"
                                    }
                                ],
                                "margin": "sm"
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
