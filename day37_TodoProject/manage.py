from app import manager, db
from app.views import  *

# 添加数据库操作的命令信息;
from app.models import User, Category, Todo

@manager.command
def dbinit():
    """数据库初始化信息"""
    db.drop_all()
    db.create_all()
    u = User(username='admin', email="admin@qq.com")
    u.password = 'admin'
    db.session.add(u)
    db.session.commit()
    print("用户%s创建成功......." % (u.username))

    c = Category(name="学习", user_id=1)
    db.session.add(c)
    print("分类%s创建成功...." % (c.name))

    t = Todo(content="学习Flask", category_id=1, user_id=1)
    db.session.add(t)
    print("任务%s添加成功....." % (t.content))
    db.session.commit()


if __name__ == '__main__':
    manager.run()
