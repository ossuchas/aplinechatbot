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
                            "size": "kilo",
                            "hero": {
                                "type": "box",
                                "layout": "baseline",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "Estimate Income",
                                        "align": "start",
                                        "color": "#FFFFFF",
                                        "offsetStart": "5%",
                                        "offsetTop": "2px"
                                    }
                                ],
                                "height": "25px"
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
                                                "text": "AP",
                                                "weight": "bold",
                                                "size": "sm"
                                            },
                                            {
                                                "type": "text",
                                                "text": "Year (MB)",
                                                "align": "end",
                                                "size": "sm",
                                                "weight": "bold"
                                            }
                                        ]
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "BG1 : SDH",
                                                "align": "start",
                                                "offsetStart": "5%",
                                                "size": "sm"
                                            },
                                            {
                                                "type": "text",
                                                "text": "8,631,050,577",
                                                "align": "end",
                                                "size": "sm"
                                            }
                                        ]
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "BG2 - TH",
                                                "align": "start",
                                                "offsetStart": "5%",
                                                "size": "sm"
                                            },
                                            {
                                                "type": "text",
                                                "text": "6,360,603,940",
                                                "align": "end",
                                                "size": "sm"
                                            }
                                        ]
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "BG3 - CONDO 1",
                                                "align": "start",
                                                "offsetStart": "5%",
                                                "size": "sm"
                                            },
                                            {
                                                "type": "text",
                                                "text": "2,617,314,062",
                                                "align": "end",
                                                "size": "sm"
                                            }
                                        ]
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "BG4 - CONDO 2",
                                                "offsetStart": "5%",
                                                "size": "sm"
                                            },
                                            {
                                                "type": "text",
                                                "text": "1,038,834,093",
                                                "align": "end",
                                                "size": "sm"
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
                                                "text": "AP Total :",
                                                "size": "sm",
                                                "align": "end",
                                                "weight": "bold",
                                                "style": "italic"
                                            },
                                            {
                                                "type": "text",
                                                "text": "18,647,802,672",
                                                "align": "end",
                                                "size": "sm",
                                                "weight": "bold",
                                                "style": "italic"
                                            }
                                        ],
                                        "backgroundColor": "#E8E16F"
                                    },
                                    {
                                        "type": "separator"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "JV",
                                                "size": "sm",
                                                "weight": "bold"
                                            }
                                        ]
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "BG3 - JV (100%)",
                                                "align": "start",
                                                "offsetStart": "5%",
                                                "size": "sm"
                                            },
                                            {
                                                "type": "text",
                                                "text": "4,160,316,282",
                                                "align": "end",
                                                "size": "sm"
                                            }
                                        ]
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "BG4 - JV (100%)",
                                                "align": "start",
                                                "offsetStart": "5%",
                                                "size": "sm"
                                            },
                                            {
                                                "type": "text",
                                                "text": "635,205,789",
                                                "align": "end",
                                                "size": "sm"
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
                                                "text": "JV Total :",
                                                "size": "sm",
                                                "align": "end",
                                                "weight": "bold",
                                                "style": "italic"
                                            },
                                            {
                                                "type": "text",
                                                "text": "4,795,522,071",
                                                "align": "end",
                                                "size": "sm",
                                                "weight": "bold",
                                                "style": "italic"
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
                                                "text": "Grand Total",
                                                "size": "sm",
                                                "weight": "bold"
                                            },
                                            {
                                                "type": "text",
                                                "text": "23,443,324,743",
                                                "size": "sm",
                                                "align": "end",
                                                "weight": "bold"
                                            }
                                        ],
                                        "margin": "sm",
                                        "backgroundColor": "#7AFF97"
                                    },
                                    {
                                        "type": "separator"
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
                                        "size": "xs",
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
                        },
                        {
                            "type": "bubble",
                            "size": "kilo",
                            "hero": {
                                "type": "box",
                                "layout": "baseline",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "Estimate Income",
                                        "align": "start",
                                        "color": "#FFFFFF",
                                        "offsetStart": "5%",
                                        "offsetTop": "2px"
                                    }
                                ],
                                "height": "25px"
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
                                                "text": "AP",
                                                "weight": "bold",
                                                "size": "sm"
                                            },
                                            {
                                                "type": "text",
                                                "text": "Quarter#1 (MB)",
                                                "align": "end",
                                                "size": "sm",
                                                "weight": "bold"
                                            }
                                        ]
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "BG1 : SDH",
                                                "align": "start",
                                                "offsetStart": "5%",
                                                "size": "sm"
                                            },
                                            {
                                                "type": "text",
                                                "text": "3,539,408,759",
                                                "align": "end",
                                                "size": "sm"
                                            }
                                        ]
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "BG2 - TH",
                                                "align": "start",
                                                "offsetStart": "5%",
                                                "size": "sm"
                                            },
                                            {
                                                "type": "text",
                                                "text": "2,541,474,501",
                                                "align": "end",
                                                "size": "sm"
                                            }
                                        ]
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "BG3 - CONDO 1",
                                                "align": "start",
                                                "offsetStart": "5%",
                                                "size": "sm"
                                            },
                                            {
                                                "type": "text",
                                                "text": "487,096,431",
                                                "align": "end",
                                                "size": "sm"
                                            }
                                        ]
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "BG4 - CONDO 2",
                                                "offsetStart": "5%",
                                                "size": "sm"
                                            },
                                            {
                                                "type": "text",
                                                "text": "454,672,000",
                                                "align": "end",
                                                "size": "sm"
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
                                                "text": "AP Total :",
                                                "size": "sm",
                                                "align": "end",
                                                "weight": "bold",
                                                "style": "italic"
                                            },
                                            {
                                                "type": "text",
                                                "text": "7,619,183,310",
                                                "align": "end",
                                                "size": "sm",
                                                "weight": "bold",
                                                "style": "italic"
                                            }
                                        ],
                                        "backgroundColor": "#E8E16F"
                                    },
                                    {
                                        "type": "separator"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "JV",
                                                "size": "sm",
                                                "weight": "bold"
                                            }
                                        ]
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "BG3 - JV (100%)",
                                                "align": "start",
                                                "offsetStart": "5%",
                                                "size": "sm"
                                            },
                                            {
                                                "type": "text",
                                                "text": "2,246,630,730",
                                                "align": "end",
                                                "size": "sm"
                                            }
                                        ]
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "BG4 - JV (100%)",
                                                "align": "start",
                                                "offsetStart": "5%",
                                                "size": "sm"
                                            },
                                            {
                                                "type": "text",
                                                "text": "-",
                                                "align": "end",
                                                "size": "sm"
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
                                                "text": "JV Total :",
                                                "size": "sm",
                                                "align": "end",
                                                "weight": "bold",
                                                "style": "italic"
                                            },
                                            {
                                                "type": "text",
                                                "text": "2,246,630,730",
                                                "align": "end",
                                                "size": "sm",
                                                "weight": "bold",
                                                "style": "italic"
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
                                                "text": "Grand Total",
                                                "size": "sm",
                                                "weight": "bold"
                                            },
                                            {
                                                "type": "text",
                                                "text": "9,865,814,040",
                                                "size": "sm",
                                                "align": "end",
                                                "weight": "bold"
                                            }
                                        ],
                                        "margin": "sm",
                                        "backgroundColor": "#7AFF97"
                                    },
                                    {
                                        "type": "separator"
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
                                        "size": "xs",
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
                        },
                        {
                            "type": "bubble",
                            "size": "kilo",
                            "hero": {
                                "type": "box",
                                "layout": "baseline",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "Estimate Income",
                                        "align": "start",
                                        "color": "#FFFFFF",
                                        "offsetStart": "5%",
                                        "offsetTop": "2px"
                                    }
                                ],
                                "height": "25px"
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
                                                "text": "AP",
                                                "weight": "bold",
                                                "size": "sm"
                                            },
                                            {
                                                "type": "text",
                                                "text": "Quarter#2 (MB)",
                                                "align": "end",
                                                "size": "sm",
                                                "weight": "bold"
                                            }
                                        ]
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "BG1 : SDH",
                                                "align": "start",
                                                "offsetStart": "5%",
                                                "size": "sm"
                                            },
                                            {
                                                "type": "text",
                                                "text": "1,835,104,000",
                                                "align": "end",
                                                "size": "sm"
                                            }
                                        ]
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "BG2 - TH",
                                                "align": "start",
                                                "offsetStart": "5%",
                                                "size": "sm"
                                            },
                                            {
                                                "type": "text",
                                                "text": "1,459,523,079",
                                                "align": "end",
                                                "size": "sm"
                                            }
                                        ]
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "BG3 - CONDO 1",
                                                "align": "start",
                                                "offsetStart": "5%",
                                                "size": "sm"
                                            },
                                            {
                                                "type": "text",
                                                "text": "757,820,342",
                                                "align": "end",
                                                "size": "sm"
                                            }
                                        ]
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "BG4 - CONDO 2",
                                                "offsetStart": "5%",
                                                "size": "sm"
                                            },
                                            {
                                                "type": "text",
                                                "text": "243,613,747",
                                                "align": "end",
                                                "size": "sm"
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
                                                "text": "AP Total :",
                                                "size": "sm",
                                                "align": "end",
                                                "weight": "bold",
                                                "style": "italic"
                                            },
                                            {
                                                "type": "text",
                                                "text": "4,296,061,168",
                                                "align": "end",
                                                "size": "sm",
                                                "weight": "bold",
                                                "style": "italic"
                                            }
                                        ],
                                        "backgroundColor": "#E8E16F"
                                    },
                                    {
                                        "type": "separator"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "JV",
                                                "size": "sm",
                                                "weight": "bold"
                                            }
                                        ]
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "BG3 - JV (100%)",
                                                "align": "start",
                                                "offsetStart": "5%",
                                                "size": "sm"
                                            },
                                            {
                                                "type": "text",
                                                "text": "1,379,067,987",
                                                "align": "end",
                                                "size": "sm"
                                            }
                                        ]
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "BG4 - JV (100%)",
                                                "align": "start",
                                                "offsetStart": "5%",
                                                "size": "sm"
                                            },
                                            {
                                                "type": "text",
                                                "text": "-",
                                                "align": "end",
                                                "size": "sm"
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
                                                "text": "JV Total :",
                                                "size": "sm",
                                                "align": "end",
                                                "weight": "bold",
                                                "style": "italic"
                                            },
                                            {
                                                "type": "text",
                                                "text": "1,379,067,987",
                                                "align": "end",
                                                "size": "sm",
                                                "weight": "bold",
                                                "style": "italic"
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
                                                "text": "Grand Total",
                                                "size": "sm",
                                                "weight": "bold"
                                            },
                                            {
                                                "type": "text",
                                                "text": "5,675,129,155",
                                                "size": "sm",
                                                "align": "end",
                                                "weight": "bold"
                                            }
                                        ],
                                        "margin": "sm",
                                        "backgroundColor": "#7AFF97"
                                    },
                                    {
                                        "type": "separator"
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
                                        "size": "xs",
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
                        },
                        {
                            "type": "bubble",
                            "size": "kilo",
                            "hero": {
                                "type": "box",
                                "layout": "baseline",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "Estimate Income",
                                        "align": "start",
                                        "color": "#FFFFFF",
                                        "offsetStart": "5%",
                                        "offsetTop": "2px"
                                    }
                                ],
                                "height": "25px"
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
                                                "text": "AP",
                                                "weight": "bold",
                                                "size": "sm"
                                            },
                                            {
                                                "type": "text",
                                                "text": "Quarter#3 (MB)",
                                                "align": "end",
                                                "size": "sm",
                                                "weight": "bold"
                                            }
                                        ]
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "BG1 : SDH",
                                                "align": "start",
                                                "offsetStart": "5%",
                                                "size": "sm"
                                            },
                                            {
                                                "type": "text",
                                                "text": "2,801,865,818",
                                                "align": "end",
                                                "size": "sm"
                                            }
                                        ]
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "BG2 - TH",
                                                "align": "start",
                                                "offsetStart": "5%",
                                                "size": "sm"
                                            },
                                            {
                                                "type": "text",
                                                "text": "1,990,698,360",
                                                "align": "end",
                                                "size": "sm"
                                            }
                                        ]
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "BG3 - CONDO 1",
                                                "align": "start",
                                                "offsetStart": "5%",
                                                "size": "sm"
                                            },
                                            {
                                                "type": "text",
                                                "text": "645,104,648",
                                                "align": "end",
                                                "size": "sm"
                                            }
                                        ]
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "BG4 - CONDO 2",
                                                "offsetStart": "5%",
                                                "size": "sm"
                                            },
                                            {
                                                "type": "text",
                                                "text": "242,019,389",
                                                "align": "end",
                                                "size": "sm"
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
                                                "text": "AP Total :",
                                                "size": "sm",
                                                "align": "end",
                                                "weight": "bold",
                                                "style": "italic"
                                            },
                                            {
                                                "type": "text",
                                                "text": "5,679,688,215",
                                                "align": "end",
                                                "size": "sm",
                                                "weight": "bold",
                                                "style": "italic"
                                            }
                                        ],
                                        "backgroundColor": "#E8E16F"
                                    },
                                    {
                                        "type": "separator"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "JV",
                                                "size": "sm",
                                                "weight": "bold"
                                            }
                                        ]
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "BG3 - JV (100%)",
                                                "align": "start",
                                                "offsetStart": "5%",
                                                "size": "sm"
                                            },
                                            {
                                                "type": "text",
                                                "text": "472,319,120",
                                                "align": "end",
                                                "size": "sm"
                                            }
                                        ]
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "BG4 - JV (100%)",
                                                "align": "start",
                                                "offsetStart": "5%",
                                                "size": "sm"
                                            },
                                            {
                                                "type": "text",
                                                "text": "-",
                                                "align": "end",
                                                "size": "sm"
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
                                                "text": "JV Total :",
                                                "size": "sm",
                                                "align": "end",
                                                "weight": "bold",
                                                "style": "italic"
                                            },
                                            {
                                                "type": "text",
                                                "text": "472,319,120",
                                                "align": "end",
                                                "size": "sm",
                                                "weight": "bold",
                                                "style": "italic"
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
                                                "text": "Grand Total",
                                                "size": "sm",
                                                "weight": "bold"
                                            },
                                            {
                                                "type": "text",
                                                "text": "6,152,007,335",
                                                "size": "sm",
                                                "align": "end",
                                                "weight": "bold"
                                            }
                                        ],
                                        "margin": "sm",
                                        "backgroundColor": "#7AFF97"
                                    },
                                    {
                                        "type": "separator"
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
                                        "size": "xs",
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
                        },
                        {
                            "type": "bubble",
                            "size": "kilo",
                            "hero": {
                                "type": "box",
                                "layout": "baseline",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "Estimate Income",
                                        "align": "start",
                                        "color": "#FFFFFF",
                                        "offsetStart": "5%",
                                        "offsetTop": "2px"
                                    }
                                ],
                                "height": "25px"
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
                                                "text": "AP",
                                                "weight": "bold",
                                                "size": "sm"
                                            },
                                            {
                                                "type": "text",
                                                "text": "Quarter#4 (MB)",
                                                "align": "end",
                                                "size": "sm",
                                                "weight": "bold"
                                            }
                                        ]
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "BG1 : SDH",
                                                "align": "start",
                                                "offsetStart": "5%",
                                                "size": "sm"
                                            },
                                            {
                                                "type": "text",
                                                "text": "454,672,000",
                                                "align": "end",
                                                "size": "sm"
                                            }
                                        ]
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "BG2 - TH",
                                                "align": "start",
                                                "offsetStart": "5%",
                                                "size": "sm"
                                            },
                                            {
                                                "type": "text",
                                                "text": "368,908,000",
                                                "align": "end",
                                                "size": "sm"
                                            }
                                        ]
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "BG3 - CONDO 1",
                                                "align": "start",
                                                "offsetStart": "5%",
                                                "size": "sm"
                                            },
                                            {
                                                "type": "text",
                                                "text": "163,185,453",
                                                "align": "end",
                                                "size": "sm"
                                            }
                                        ]
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "BG4 - CONDO 2",
                                                "offsetStart": "5%",
                                                "size": "sm"
                                            },
                                            {
                                                "type": "text",
                                                "text": "66,104,526",
                                                "align": "end",
                                                "size": "sm"
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
                                                "text": "AP Total :",
                                                "size": "sm",
                                                "align": "end",
                                                "weight": "bold",
                                                "style": "italic"
                                            },
                                            {
                                                "type": "text",
                                                "text": "1,052,869,979",
                                                "align": "end",
                                                "size": "sm",
                                                "weight": "bold",
                                                "style": "italic"
                                            }
                                        ],
                                        "backgroundColor": "#E8E16F"
                                    },
                                    {
                                        "type": "separator"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "JV",
                                                "size": "sm",
                                                "weight": "bold"
                                            }
                                        ]
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "BG3 - JV (100%)",
                                                "align": "start",
                                                "offsetStart": "5%",
                                                "size": "sm"
                                            },
                                            {
                                                "type": "text",
                                                "text": "62,298,445",
                                                "align": "end",
                                                "size": "sm"
                                            }
                                        ]
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "BG4 - JV (100%)",
                                                "align": "start",
                                                "offsetStart": "5%",
                                                "size": "sm"
                                            },
                                            {
                                                "type": "text",
                                                "text": "635,205,789",
                                                "align": "end",
                                                "size": "sm"
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
                                                "text": "JV Total :",
                                                "size": "sm",
                                                "align": "end",
                                                "weight": "bold",
                                                "style": "italic"
                                            },
                                            {
                                                "type": "text",
                                                "text": "697,504,234",
                                                "align": "end",
                                                "size": "sm",
                                                "weight": "bold",
                                                "style": "italic"
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
                                                "text": "Grand Total",
                                                "size": "sm",
                                                "weight": "bold"
                                            },
                                            {
                                                "type": "text",
                                                "text": "1,750,374,213",
                                                "size": "sm",
                                                "align": "end",
                                                "weight": "bold"
                                            }
                                        ],
                                        "margin": "sm",
                                        "backgroundColor": "#7AFF97"
                                    },
                                    {
                                        "type": "separator"
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
                                        "size": "xs",
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
