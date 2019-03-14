from flask import  Flask
from flask_sqlalchemy import  SQLAlchemy
from flask_bootstrap import  Bootstrap
from flask_script import Manager
import  pymysql

app = Flask(__name__)

# 数据库报错问题
pymysql.install_as_MySQLdb()

# 读取配置文件的配置信息
app.config.from_pyfile('../config.py')
db = SQLAlchemy(app)
manager = Manager(app)
bt = Bootstrap(app)









