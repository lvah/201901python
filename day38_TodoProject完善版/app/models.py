from app import db
from werkzeug.security import  generate_password_hash, check_password_hash
from datetime import  datetime



# 用户和任务的关系: 一对多， 用户是一， 任务是多，
# 用户和分类的关系:
class User(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String(20), unique=True)
    password_hash = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(30), unique=True)
    add_time = db.Column(db.DateTime, default=datetime.utcnow()) # 账户创建时间
    # 1).  User添加属性todos; 2). Todo添加属性user;
    todos = db.relationship('Todo', backref="user")
    categories = db.relationship('Category', backref='user')

    @property
    def password(self):
        """u.password"""
        raise  AttributeError("密码属性不可以读取")

    @password.setter
    def password(self, password):
        """u.password = xxxxx """
        self.password_hash = generate_password_hash(password)


    def verify_password(self, password):
        """验证密码是否正确"""
        return  check_password_hash(self.password_hash, password)

    def __repr__(self):
        return  "<User %s>" %(self.username)

# 任务和分类的关系： 一对多
# 分类是一， 任务是多, 外键写在多的一端
class Todo(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    content = db.Column(db.String(100)) # 任务内容
    status = db.Column(db.Boolean, default=False) # 任务的状态
    # datetime.now()你当前所在时区的时间;
    # 使用协调时间时（Coordinated Universal Time,UTC）协调世界各地的时差问题;
    #   美国时间: 2019-3-15 00:00   北京时间: 2019-03-16 12:00  ***
    add_time = db.Column(db.DateTime, default=datetime.utcnow())  # 任务创建时间
    # 任务的类型,关联另外一个表的id
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    # 任务所属用户;
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return  "<Todo %s>" %(self.content[:6])


class Category(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(20), unique=True)
    add_time = db.Column(db.DateTime, default=datetime.utcnow())  # 任务创建时间
    # 1). Category添加一个属性todos, 2). Todo添加属性category；
    todos = db.relationship('Todo', backref='category')

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return  "<Category %s>" %(self.name)





