from app import manager
# from app.models import  *
from app import  db
from werkzeug.security import  generate_password_hash

from app.models import User, Admin
from flask_migrate import  MigrateCommand


@manager.command
def initdb():
    """初始化数据库表"""
    db.drop_all()
    db.create_all()
    u = User(name='westos', password=generate_password_hash('westos'))
    db.session.add(u)
    db.session.commit()
    print("初始化数据库成功......")


@manager.command
def createsuperuser():
    """创建超级用户"""
    username = input("请输入管理员名称:")
    if Admin.query.filter_by(name=username).first():
        print("管理员%s已经存在" %(username))
    else:
        import getpass
        password = getpass.getpass("请输入管理员密码:")
        password_hash = generate_password_hash(password)
        admin = Admin(name=username, password=password_hash, is_super=True)
        db.session.add(admin)
        db.session.commit()
        print("创建超级用户%s成功" %(username))



manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()