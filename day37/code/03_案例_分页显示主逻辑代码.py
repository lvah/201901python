# app.py文件中;

from datetime import datetime

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy, Pagination
from flask_bootstrap import Bootstrap
import pymysql
from sqlalchemy import desc, func

pymysql.install_as_MySQLdb()
app = Flask(__name__)



app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:redhat@localhost/UserTest'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
bt = Bootstrap(app)

### 用户和角色是什么关系?
#    - 一对一
#    - 一对多: 角色是一， 用户是多， 外键写在多的一端
#   - 多对多
class Role(db.Model):
    __tablename__ = "用户角色"
    # id号递增autoincrement=True
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20))
    # 反向引用, Role表中有属性users， User类中有role这个属性;
    users = db.relationship('User', backref='role')

    def __repr__(self):
        return "<Role %s>" % (self.name)


class User(db.Model):
    __tablename__ = "网站用户"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, index=True, nullable=False)  # unique=True用户名不能重复
    password = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(20), unique=True, index=True)
    # 设置默认值， 位当前用户的创建时间;
    add_time = db.Column(db.DateTime, default=datetime.now())
    #### 重要的： 用户角色id不能随便设置， 需要从Role中查询, （外键关联）
    role_id = db.Column(db.Integer, db.ForeignKey('用户角色.id'))

    # 定义了 __repr()__ 方法,返回一个具有可读性的字符串表示模型,可在调试和测试时使用。
    def __repr__(self):
        return "<User %s>" % (self.username)


# http://www.csdn.net/list/
# http://www.csdn.net/list/1/
# http://www.csdn.net/list/2/
@app.route('/list/')
@app.route('/list/<int:page>/')
def list(page=1):
    # 每页显示的数据
    per_page = 10
    # 返回的是 Pagination对象
    userPageObj = User.query.paginate(page=page, per_page=per_page)
    return render_template('list.html',
                           userPageObj=userPageObj
                           )

if __name__ == '__main__':
    app.run(port=5005)




