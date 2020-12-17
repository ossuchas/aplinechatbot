import os
import urllib

DEBUG = True
DATABASE_HOST = os.environ.get("DATABASE_HOST")
DATABASE_NAME = os.environ.get("DATABASE_NAME")
DATABASE_USER = os.environ.get("DATABASE_USER")
DATABASE_PASS = os.environ.get("DATABASE_PASS")

params = 'Driver={ODBC Driver 17 for SQL Server};' \
             f"Server=" + f"{DATABASE_HOST};" \
             f"Database=" + f"{DATABASE_NAME};" \
             f"uid=" + f"{DATABASE_USER};" \
             f"pwd=" + f"{DATABASE_PASS};"

params = urllib.parse.quote_plus(params)

SQLALCHEMY_DATABASE_URI = "mssql+pyodbc:///?odbc_connect=%s" % params
SQLALCHEMY_TRACK_MODIFICATIONS = False
PROPAGATE_EXCEPTIONS = True
JWT_BLACKLIST_ENABLED = True
JWT_BLACKLIST_TOKEN_CHECKS = ["access", "refresh"]

# Bot Test
#CHANNEL_ACCESS_TOKEN="wXjIZWvNNerxSVIpFVomPA4baBMaXhZtSJdJT11Uw4E8IOqzoJ+DGo++h/TPthxBM2LbrPCpiWiZX0GkXXENi9FE0DccFs0d6fSgntVhbj7Kf1iWp3hwXtJUOYSm5Dib7jC121/2bDpT1b0bIP1N4wdB04t89/1O/w1cDnyilFU="

# IT@APTHAI BOT
# CHANNEL_ACCESS_TOKEN="yzEGLNrzFPgkRW113hBPayMP+4Z6nmGa3gDQNAxNxYQR7jqj9Vo6w3YwfOLnpzPr48+GB9j4rgTlcWKyRPMgY0f+e0FuX5tizSVzLrd/o3gkaniObBMudbWZXrHL3CD9IZ2SQXUE7GeDp76UVNpG+gdB04t89/1O/w1cDnyilFU="
CHANNEL_ACCESS_TOKEN = os.environ.get("CHANNEL_ACCESS_TOKEN")
LINE_API_RICHMENU=os.environ.get("LINE_API_RICHMENU")
# LINE_API="https://api.line.me/v2/bot/message/reply"
LINE_API = os.environ.get("LINE_API")
LINE_API_PUSH = os.environ.get("LINE_API_PUSH")
TABLEAU_URL = os.environ.get("TABLEAU_URL")

DEFAULT_REPLY_WORDING = "เจ้านายกำลังฝึกผมให้เข้าใจในเรื่องอื่นๆอยู่นะครับ ขอโทษทีตอนนี้ยังไม่พร้อมตอบเรื่องที่ถามมานะครับ"
REPLY_WORDING = ["99999", "00000", "เสี่ยจัสติน", "เสี่ย"]

REPLY_SALCE_ACCM_B_M_WORDING = ["ยอดเดือนที่แล้ว", "ยอดขายเดือนที่แล้ว", "สอบถามยอดขายเดือนที่แล้วหน่อยครับ", "ส่งยอดเดือนที่แล้วมาดูหน่อย",
                 "ขอยอดขายเดือนที่แล้ว", "ส่งยอดขายเดือนที่แล้วหน่อย"]

REPLY_SALCE_ACCM_C_M_WORDING = ["ยอดเดือนนี้", "ยอดขายเดือนนี้", "สอบถามยอดขายเดือนนี้หน่อยครับ", "ส่งยอดเดือนนี้มาดูหน่อย",
                              "ขอยอดขายเดือนนี้", "ส่งยอดขายเดือนนี้หน่อย"]

MENU_01_VIP = "LL BY BG"
MENU_01_VIP_BG = "LL BY BG"
MENU_02_VIP = "LL BY SubBG"
MENU_02_VIP_BG = "LL BY SubBG"
# Modified by Suchat S. 2020-10-24 for Change LL By Project
MENU_03_LCM = "LL BY Proj"


# Main Menu
LL_MSG_All = "LL SDH All"
LL_MSG_PROJ = "proj:"

# Select Sub BG SDH
LL_MSG_SUB_PERIOD = "LL SDH Sub"

# Peroid Select All BG
LL_MSG_ALLBG_PERIOD = "LL Period BY BG"

# Peroid Select All Sub BG
LL_MSG_ALLSUBBG_PERIOD = "LL Period BY SubBG"

# Peroid Select Actual incomde
AC_ACTUAL_INCOME = "Actual Income"
LL_MSG_AC_Y2D = "Actual Income Period Y2D"
LL_MSG_AC_DAILY = "Actual Income Daily"

# Peroid Select Gross incomde
BOOKING_INCOME = "Booking Period Y2D"

# AP Phone Book
LL_MSG_APPHONEBOOK = "AP"
LL_MSG_APPHONEBOOK2 = "ap"

# Executive Report
EXECUTIVE_REPORT = "Executive Report"
EXECUTIVE_PREFIX = "EX Period"
EXECUTIVE_YTD = "EX Period As of Current"
EXECUTIVE_QTD = "EX Period Quarter"

# Dashboard
DASHBOARD_CARD = "Dashboard"

# Register
REGISTER_MSG = "register=>emp: "
REGISTER_REJECT_MSG = "can not sign up, you are unauthorized!!"

# Demo App
DEMO_APP = "Demo App"

# Rich Menu
# RICH_MENU_MAIN = "richmenu-0fffa00a28636aeea4cdbb2673be6e8c"
# RICH_MENU_SECOND = "richmenu-ff31ac5e2075514e215a0a2d3bcdd035"
# RICH_MENU_MAIN = "richmenu-0fffa00a28636aeea4cdbb2673be6e8c"
# RICH_MENU_SECOND = "richmenu-ff31ac5e2075514e215a0a2d3bcdd035"
RICH_MENU_MAIN = os.environ.get("RICH_MENU_MAIN")
RICH_MENU_SECOND = os.environ.get("RICH_MENU_SECOND")

RICH_MENU_MAIN_IT = os.environ.get("RICH_MENU_MAIN_IT")
RICH_MENU_MAIN_LCM = os.environ.get("RICH_MENU_MAIN_LCM")
RICH_MENU_MAIN_MKT = os.environ.get("RICH_MENU_MAIN_MKT")
RICH_MENU_MAIN_SUBBG = os.environ.get("RICH_MENU_MAIN_SUBBG")
RICH_MENU_MAIN_VIP = os.environ.get("RICH_MENU_MAIN_VIP")
RICH_MENU_MAIN_VIP2 = os.environ.get("RICH_MENU_MAIN_VIP2")
RICH_MENU_SECOND_IT = os.environ.get("RICH_MENU_SECOND_IT")
RICH_MENU_SECOND_LCM = os.environ.get("RICH_MENU_SECOND_LCM")
RICH_MENU_SECOND_MKT = os.environ.get("RICH_MENU_SECOND_MKT")
RICH_MENU_SECOND_SUBBG = os.environ.get("RICH_MENU_SECOND_SUBBG")
RICH_MENU_SECOND_VIP = os.environ.get("RICH_MENU_SECOND_VIP")
RICH_MENU_SECOND_VIP2 = os.environ.get("RICH_MENU_SECOND_VIP2")

# Check PM
CHECK_PM = "ตรวจสอบค่า PM 2.5"
API_AIRVISUAL_KEY="997fd440-6a2e-48a9-9336-7cb0eaef4a99"
API_AIRVISUAL_URI = "https://api.airvisual.com/v2"

# Virus Corona
VIRUS = ["ไวรัสโคโรนา", "โคโรนา", "virus", "corona", "อู่ฮั่น", "ไวรัสจีน", "ไวรัส"]

HOT_ISSUE = "Hot Issue"

# Get Url Ticket Tableau Server
API_TABLEAU_TICKET = os.environ.get("API_TABLEAU_TICKET")

CRM_GETTOKEN_URL = os.environ.get("CRM_GETTOKEN_URL")
CRM_CLIENT_ID = os.environ.get("CRM_CLIENT_ID")
CRM_CLIENT_SECRET = os.environ.get("CRM_CLIENT_SECRET")
CRM_API_PROC = os.environ.get("CRM_API_PROC")

# VERSION
VERSION = ["version", "Version", "-v", "--version"]

# VERSION Test
VERSION_TEST = ["-vt"]
