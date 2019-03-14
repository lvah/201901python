from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
import pymysql
from flask_script import  Manager
from flask_migrate import  Migrate

pymysql.install_as_MySQLdb()
app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:redhat@localhost/UserTest'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config.from_pyfile('../config.py')


db = SQLAlchemy(app)
bt = Bootstrap(app)
manager = Manager(app)
migrate = Migrate(app, db)

