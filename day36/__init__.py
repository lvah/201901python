from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
import pymysql

pymysql.install_as_MySQLdb()
app = Flask(__name__)

# 将配置信息独立成一个文件， 便于将来修改;
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)
bt = Bootstrap(app)
