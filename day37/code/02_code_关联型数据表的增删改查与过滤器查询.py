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


if __name__ == '__main__':
    db.drop_all()
    db.create_all()

    # ***********************1. 添加数据
    # 1). 添加角色
    role1 = Role(name="普通用户")
    role2 = Role(name="会员")
    role3 = Role(name="管理员")

    db.session.add_all([role1, role2, role3])
    db.session.commit()
    # 2). 添加用户
    user1 = User(username="westos1", password="westos1",
                 email="westos1@qq.com", role_id=1)
    db.session.add(user1)
    db.session.commit()

    # **********************2. 查看数据信息
    print(User.query.all())
    print(Role.query.all())

    # 批量添加用户100个是普通用户， 50个是VIP用户， 10个管理员
    for item in range(100):
        user = User(
            username="fentiao%s" % (item),
            password="fentiao",
            email="fentiao%s" % (item),
            role_id=1
        )
        db.session.add(user)

    for item in range(50):
        user = User(
            username="vip%s" % (item),
            password="vip",
            email="vip%s" % (item),
            role_id=2
        )
        db.session.add(user)

    for item in range(10):
        user = User(
            username="admin%s" % (item),
            password="admin",
            email="admin%s" % (item),
            role_id=3
        )
        db.session.add(user)

    # 将批量添加的用户提交到数据库中.
    db.session.commit()

    # 获取所有的普通用户
    common_users = User.query.filter_by(role_id='1').all()
    print(common_users)
    vip_users = User.query.filter_by(role_id='2').all()
    print(vip_users)

    # 获取所有的普通用户转化成的sql语句查看;
    print(User.query.filter_by(role_id='1'))
    print(User.query)

    # filter过滤器的使用（更偏向于SQL语句）
    common_users = User.query.filter(User.role_id == 1).all()
    print(common_users)

    # limit过滤器, 只显示返回结果的前几条数据;
    common_users_limit = User.query.filter(User.role_id == 1).limit(5).all()
    print(common_users_limit)

    # offset过滤器: 偏移显示
    common_users_offset = User.query.filter(User.role_id == 1).offset(2).limit(3).all()
    print(common_users_offset)

    # order_by排序过滤器, 默认是升序的， 如果要降序desc(属性名)
    common_users_order = User.query.order_by(User.role_id).all()
    print(common_users_order)
    # 降序
    common_users_desc_order = User.query.order_by(desc(User.role_id)).all()
    print(common_users_desc_order)

    # group_by, 分组统计
    users_analysis = User.query.add_columns(func.count(User.role_id)).group_by(User.role_id).all()
    print(users_analysis)

    # get方法
    print(User.query.get(1))
    # print(User.query.get_or_404(1000))

    # count
    print(User.query.filter_by(role_id=1).count())
    print(User.query.filter_by(role_id=2).count())
    print(User.query.filter_by(role_id=3).count())

    # paginate分页的对象
    # page=2： 要显示第2页的数据， per_page=5： 每页显示数据的条数
    # 101+50+10
    usersPageObj = User.query.paginate(page=2, per_page=5)

    print("当前页面的记录数:", usersPageObj.items)
    print("分页查询的源sql语句:", usersPageObj.query)
    print("当前显示的页数:", usersPageObj.page)
    print("上一页的页数:", usersPageObj.prev_num)
    print("下一页的页数:", usersPageObj.next_num)
    print("是否包含上一页:", usersPageObj.has_prev)
    print("是否包含下一页:", usersPageObj.has_next)
    print("总页数:", usersPageObj.pages)
    print("每页记录的数量:", usersPageObj.per_page)
    print("记录总数:", usersPageObj.total)

    # *********************
    print("页码显示:", list(usersPageObj.iter_pages()))
    print("上一页的数据:", usersPageObj.prev().items)
    print("下一页的数据:", usersPageObj.next().items)



    # Role表反向引用
    print("反向引用".center(100, '*'))
    admin_role = Role.query.filter_by(name="管理员").first()
    print(admin_role.id)
    print(admin_role.name)
    print(admin_role.users)


    # User表中
    admin_user = User.query.filter_by(username='admin1').first()
    admin_user_id = admin_user.role_id
    print(Role.query.filter_by(id=admin_user_id).first().name)

    #
    admin_user = User.query.filter_by(username='admin1').first()
    print(admin_user.role.name)



