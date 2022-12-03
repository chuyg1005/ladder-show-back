from flask import Flask
from config import Config

from flask_sqlalchemy import SQLAlchemy
import pymysql

# 配置跨域支持
from flask_cors import CORS

pymysql.install_as_MySQLdb()

from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)


CORS(app, supports_credentials=True)