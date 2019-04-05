from random import randint

from app import manager
# from app.models import  *
from app import db
from werkzeug.security import generate_password_hash

from app.models import User, Admin, Tag, Movie
from flask_migrate import MigrateCommand


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
        print("管理员%s已经存在" % (username))
    else:
        import getpass
        password = getpass.getpass("请输入管理员密码:")
        password_hash = generate_password_hash(password)
        admin = Admin(name=username, password=password_hash, is_super=True)
        db.session.add(admin)
        db.session.commit()
        print("创建超级用户%s成功" % (username))


@manager.command
def create_tag():
    """批量添加标签"""
    import pandas
    df = pandas.read_csv('movie.csv',
                         names=['name', 'logo', 'actors', 'release_time', 'detail_url', 'tag', 'area', 'length',
                                'info'])
    tags = df['tag'].unique()
    for tag in tags:
        if not Tag.query.filter_by(name=tag).first():
            tag = Tag(name=tag)
            db.session.add(tag)
            db.session.commit()
            print("添加标签%s成功" % (tag))


@manager.command
def create_movie():
    import csv
    movies = csv.reader(open('movie.csv'))
    for movie in movies:
        name = movie[0]
        logo = name + movie[1].split('/')[-1]
        actors = movie[2]
        release_time = movie[3]
        tag = movie[5]
        area = movie[6]
        length = movie[7]
        info = movie[-1]

        tag = Tag.query.filter_by(name=tag).first()
        if not tag:
            tag = Tag(name=tag)
            db.session.add(tag)
            db.session.commit()
            print("添加标签%s成功" % (tag))

        movie = Movie(name=name, logo=logo, tag_id=tag.id, release_time=release_time, area=area, star=randint(1, 5), length=length, info=info, url='20190324_15395101_videos.mp4')
        db.session.add(movie)
        db.session.commit()
        print("添加电影%s成功" %(name))

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
