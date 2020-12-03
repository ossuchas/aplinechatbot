import os
from requests import Response, post
import json
from config import API_TABLEAU_TICKET

from config import CRM_GETTOKEN_URL, CRM_CLIENT_ID, CRM_CLIENT_SECRET, CRM_API_PROC


class APAuthenException(Exception):
    def __init__(self, message: str):
        super().__init__(message)


class APGenTicketTableau:

    @classmethod
    def ap_genticket(cls) -> Response:
        # url = API_TABLEAU_TICKET
        # # url = "https://dashboard.apthai.com/trusted/"
        # data = ({
        #     'username': 'admin',
        #     'target_site': 'CRM'
        # })
        # headers = {'Content-type': 'application/x-www-form-urlencoded'}
        # # headers = None
        # response = post(url=url, data=data, headers=headers)
        # # print(response.status_code)
        # # print(response.text)
        #
        # if response.status_code != 200:
        #     raise APAuthenException("Gen Ticket Error Occurred.")
        #
        # return response
        url = CRM_GETTOKEN_URL
        payload = {
            "client_id": CRM_CLIENT_ID,
            "client_secret": CRM_CLIENT_SECRET
        }
        headers = {"Content-Type": "application/json"}
        response = post(url, data=json.dumps(payload), headers=headers)
        response_data = response.json()
        access_token = response_data["token"]

        token = f"Bearer {access_token}"
        url = f"{CRM_API_PROC}"

        headers = {
            "Content-Type": "application/json",
            "Authorization": token
        }

        data = {
            "server_trusted": API_TABLEAU_TICKET,
            "username": "admin",
            "target_site": "CRM"
        }

        response = post(url=url, data=json.dumps(data), headers=headers)

        if response.status_code != 200:
            raise APAuthenException(f"Gen Ticket Error Occurred.{response}")

        return response
