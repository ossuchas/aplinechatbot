import os
from requests import Response, post
import json
from config import API_TABLEAU_TICKET


class APAuthenException(Exception):
    def __init__(self, message: str):
        super().__init__(message)


class APGenTicketTableau:

    # APAUTHEN_URL = os.environ.get("APAUTHEN_URL")
    # APAUTHEN_API_KEY = os.environ.get("APAUTHEN_API_KEY")
    # APAUTHEN_API_TOKEN = os.environ.get("APAUTHEN_API_TOKEN")

    @classmethod
    def ap_genticket(cls) -> Response:
        # url = "http://dashboard.apthai.com/trusted"
        url = API_TABLEAU_TICKET
        # payload = (){"username": "admin", "taget_site": "CRM"})
        data = ({
            'username': 'admin',
            'target_site': 'CRM'
        })
        headers = {'Content-type': 'application/x-www-form-urlencoded'}
        response = post(url=url, data=data, headers=headers)
        # print(response.status_code)
        # print(response.text)

        if response.status_code != 200:
            raise APAuthenException("Gen Ticket Error Occurred.")

        return response
