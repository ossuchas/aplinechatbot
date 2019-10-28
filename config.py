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
# LINE_API="https://api.line.me/v2/bot/message/reply"
LINE_API = os.environ.get("LINE_API")

REPLY_WORDING = ["ถามหน่อย", "สอบถาม", "มีอะไรจะถาม"]
