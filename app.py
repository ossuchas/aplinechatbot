from flask import Flask, jsonify
from flask_restful import Api
from dotenv import load_dotenv
from flask_cors import CORS
from marshmallow import ValidationError

from db import db
from ma import ma

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'AP Line Chat Bot Hello World!'

@app.route('/webhook')
def hello_world():
    return 'Def Webhhok for AP!'


if __name__ == '__main__':
    db.init_app(app)
    ma.init_app(app)
    # app.run(host="0.0.0.0", port=5000, debug=True)
    app.run(port=5000)
