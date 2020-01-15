from flask import Flask, jsonify
from flask_restful import Api
from dotenv import load_dotenv
from flask_cors import CORS
from marshmallow import ValidationError

from db import db
from ma import ma

from resources.chatbot import ChatBot, ChatBotRegister
from resources.vw_chatbot_mst_project import MstProject
from resources.userauthen import UserLogin
from resources.vw_crm_line_userroleproj import UserRoleProject
from resources.vw_crm_line_userroleproj2 import UserRoleProject2
from resources.chatbot_mst_user import ChatBotMstUserRole, ChatBotMstUserList

app = Flask(__name__)

api = Api(app, prefix="/api/v1")
CORS(app, resources=r"/api/*", allow_headers="Content-Type")

load_dotenv(".env", verbose=True)
app.config.from_object("config")
app.config.from_envvar("APPLICATION_SETTING")


@app.route('/')
def hello_world():
    return 'AP Line Chat Bot Hello World! v2.0.1'


api.add_resource(ChatBot, "/webhook")
api.add_resource(ChatBotRegister, "/register")
api.add_resource(MstProject, "/getallproj")
api.add_resource(UserLogin, "/checkauthorized")
api.add_resource(UserRoleProject, "/getroleproj/<string:userid>")
api.add_resource(UserRoleProject2, "/getroleproj2/<string:userid>")
api.add_resource(ChatBotMstUserList, "/listuserrole")
api.add_resource(ChatBotMstUserRole, "/userrole/<string:_user_empcode>")

if __name__ == '__main__':
    db.init_app(app)
    ma.init_app(app)
    app.run(host="0.0.0.0", port=5000, debug=True)
