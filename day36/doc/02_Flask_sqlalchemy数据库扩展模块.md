# 1. 什么是Flask-SQLAlchemy?
Flask-SQLAlchemy 是一个 Flask 扩展,简化了在 Flask 程序中使用 SQLAlchemy 的操作。
SQLAlchemy 是一个很强大的关系型数据库框架,支持多种数据库后台。SQLAlchemy 提
供了高层 ORM,也提供了使用数据库原生 SQL 的低层功能。



# 2. 如何安装Flask-SQLAlchemy?

pip install flask-sqlalchemy


# 3. 如何配置数据库?

```
from flask_sqlalchemy import SQLAlchemy
basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
            'sqlite:///' + os.path.join(basedir, 'data.sqlite')
# sqlchemy将会追踪对象的修改并且发送信号
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
```


# 4. 连接mysql数据库报错解决

```
import pymysql
pymysql.install_as_MySQLdb()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:redhat@localhost/UserTest'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# 实例化对象
db = SQLAlchemy(app)
```




# 5. 如何定义模型?

- 模型这个术语表示程序使用的持久化实体。
- 模型列类型
- 模型列属性
```
class User(db.Model):
    # 默认情况下表名为类的名称， 如果想要重新设置表名， __tablename__
    # 类变量 __tablename__ 定义在数据库中使用的表名.
    __tablename__ = "用户信息"
    # db.Column 类构造函数的第一个参数是数据库列和模型属性的类型。
    # db.Column 中其余的参数指定属性的配置选项。
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=Flase)  # unique=True用户名不能重复
    password = db.Column(db.String(20), nullable=Flase)
    email = db.Column(db.String(20), unique=True)

```

