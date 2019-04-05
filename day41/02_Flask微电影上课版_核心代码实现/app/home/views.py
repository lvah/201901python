"""
文件名: views.py
日期: 2019-03-17  
作者: lvah
联系: xc_guofan@qq.com
代码描述: 



"""
# 导入home的蓝图对象
import json
import os

import requests
from sqlalchemy import desc

from app import db, app
from app.home.forms import LoginForm, RegisterForm, EditUserForm, PwdForm, CommentForm
from app.home.utils import is_login, change_filename
from app.models import User, Comment, Userlog, MovieCollect, Movie, Preview, Tag

from . import home
from flask import render_template, flash, session, redirect, url_for, request, abort
from werkzeug.security import generate_password_hash


@home.route('/')
@home.route('/<int:page>/')
def index(page=1):
    # 预告信息
    previews = Preview.query.all()
    # 标签信息
    tags = Tag.query.all()
    # 星级信息[{'num':1, 'info':'1星'}, {'num':2, 'info':'2星'}.........]
    star_list = [{'num': num + 1, 'info': '%s星' % (num + 1)} for num in range(5)]

    # 上映时间信息(只显示近5年的)
    import time
    now_year = int(time.localtime().tm_year)
    # list(range(2019, 2014, -1))
    # [2019, 2018, 2017, 2016, 2015]
    year_range = [year for year in range(now_year, now_year - 5, -1)]
    page_movies = Movie.query
    tag_id = request.args.get('tag_id', 0)
    if tag_id:
        page_movies = page_movies.filter_by(tag_id=tag_id)

    star_num = request.args.get('star_num', 0)
    if star_num:
        page_movies = page_movies.filter_by(star=star_num)

    year = request.args.get('year', 0)
    if year:
        # release_time : Date ----- 2019-10-10
        from sqlalchemy import extract
        page_movies = page_movies.filter(extract('year', Movie.release_time) == year)
        print(str(extract('year', Movie.release_time)))
    # 播放数为1----从高到低进行排序；
    # 播放数为0----从低到高进行排序；
    play_num = request.args.get('play_num', 1)
    if play_num == 1:
        page_movies = page_movies.order_by(Movie.play_num.desc())  # 降序
    else:
        page_movies = page_movies.order_by(Movie.play_num.asc())  # 升序

    # Movie.query.filter_by(tag_id=tag_id)
    page_movies = page_movies.paginate(page, per_page=app.config['PER_PAGE'])
    return render_template('home/index.html',
                           previews=previews,
                           tags=tags,
                           star_list=star_list,
                           year_range=year_range,
                           page_movies=page_movies,
                           app=app)


# 注册页面
@home.route('/register/', methods=['POST', 'GET'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        # 1. 从前端获取用户输入的值;
        email = form.email.data
        username = form.username.data
        password = form.password.data

        # 2. 判断用户是否已经存在? 如果返回位None，说明可以注册;
        u = User.query.filter_by(name=username).first()
        if u:
            flash("用户%s已经存在" % (u.name))
            return redirect(url_for('home.register'))
        else:
            u = User(name=username, email=email)
            u.password = generate_password_hash(password)  # 对于密码进行加密
            db.session.add(u)
            db.session.commit()
            flash("注册用户%s成功" % (u.name))
            return redirect(url_for('home.login'))
    return render_template('home/register.html',
                           form=form)


@home.route('/login/', methods=['POST', 'GET'])
def login():
    from app.models import User, Userlog
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user = User.query.filter_by(name=username).first()
        if user and user.verify_password(password):
            # session信息的保存
            session['user_id'] = user.id
            session['user'] = user.name
            flash("用户%s登录成功" % (user.name))
            remote_ip = request.remote_addr
            # 将登录信息写到日志中;
            userlog = Userlog(user_id=user.id,
                              ip=remote_ip,
                              area='xxx内网IP')
            db.session.add(userlog)
            db.session.commit()

            # 从index蓝图里面寻找index函数;
            return redirect(url_for('home.user'))
        else:
            flash("用户登录失败")
            return redirect(url_for('home.login'))
    return render_template('home/login.html',
                           form=form)


@home.route('/logout/')
@is_login
def logout():
    session.pop('user_id', None)
    session.pop('user', None)

    return redirect(url_for('home.login'))


@home.route('/user/', methods=['GET', 'POST'])
@is_login
def user():
    form = EditUserForm()
    # 先在页面表单显示用户已经填写的信息
    user = User.query.filter_by(name=session.get('user')).first()
    form.username.data = user.name
    form.email.data = user.email
    form.phone.data = user.phone
    if form.validate_on_submit():
        # request.form   - 获取表单填写的内容
        username = request.form['username']
        email = request.form['email']
        phone = request.form['phone']
        info = request.form['info']
        # 1. 判断更改的用户名是否已经存在;  --- 邮箱和电话自己判断, 此处省略
        if username != user.name and \
                User.query.filter_by(name=username).count():
            flash("用户名%s已经存在" % (username))
            return redirect(url_for('home.user'))

        if User.query.filter_by(email=email).count() and \
                email != user.email:
            flash("邮箱%s已经注册" % (email))
            return redirect(url_for('home.user'))

        #  保存更改的信息到数据库中;(难点： 存储用户头像)
        #  *****存储用户的头像;
        file_save_path = app.config['FC_DIR']
        if not os.path.exists(file_save_path):
            os.makedirs(file_save_path)
        # 判断是否上传了新的头像;
        if form.face.data:
            # 判断之前是否已经有用户头像， 如果有， 则删除;
            if user.face and os.path.exists(os.path.join(file_save_path, user.face)):
                print(user.face)
                os.remove(os.path.join(file_save_path, user.face))  # 删除旧头像

            # 保存新的头像， 获取用户头像文件的文件名
            face_name = form.face.data.filename
            face_name = change_filename(face_name)
            print(face_name)
            # 保存新的头像文件
            form.face.data.save(os.path.join(file_save_path, face_name))
            user.face = face_name

        user.name = username
        user.email = email
        user.phone = phone
        user.info = info

        db.session.add(user)
        db.session.commit()
        flash("修改会员信息成功")
        # ******修改用户信息， 如果修改的是用户名， 一定要登录出， 再重新登录。
        logout()
        return redirect(url_for('home.login'))
    return render_template('home/user.html',
                           form=form)


# 修改密码
@home.route('/pwd/', methods=['GET', 'POST'])
def pwd():
    form = PwdForm()
    if form.validate_on_submit():
        # 获取当前登录用户的密码
        user = User.query.filter_by(name=session.get('user')).first()
        print(session.get('name'))
        # 判断用户的旧密码是否正确
        if user.verify_password(form.old_pwd.data):
            # ********数据库里面的是password
            user.password = generate_password_hash(form.new_pwd.data)
            db.session.add(user)
            db.session.commit()
            flash("密码更新成功")
        else:
            flash("旧密码错误, 请重新输入")
        return redirect(url_for('home.pwd'))
    return render_template('home/pwd.html', form=form)


@home.route('/comments/')
@home.route('/comments/<int:page>/')
def comments(page=1):
    commentsPageObj = Comment.query.filter_by(user_id=session.get('user_id')
                                              ).paginate(page, per_page=app.config['PER_PAGE'])
    return render_template('home/comments.html',
                           commentsPageObj=commentsPageObj)


# 记录用户登录日志
@home.route('/userlog/')
@home.route('/userlog/<int:page>/')
def userlog(page=1):
    userlogsPageObj = Userlog.query.filter_by(user_id=session.get('user_id')
                                              ).paginate(page, per_page=app.config['PER_PAGE'])

    return render_template('home/userlog.html',
                           userlogsPageObj=userlogsPageObj)


@home.route('/moviecollect/')
@home.route('/moviecollect/<int:page>/')
def moviecollect(page=1):
    moviecollectsPageObj = MovieCollect.query.filter_by(user_id=session.get('user_id')
                                                        ).paginate(page, per_page=app.config['PER_PAGE'])
    return render_template('home/moviecollect.html',
                           moviecollectsPageObj=moviecollectsPageObj
                           )


@home.route('/play/<int:id>/', methods=['GET', 'POST'])  # id号指的是电影的id号;
@home.route('/play/<int:id>/<int:page>/', methods=['GET', 'POST'])  # id号指的是电影的id号;
def play(id=None, page=1):
    form = CommentForm()
    if form.validate_on_submit():
        print(form.content.data)
        # 提交评论必须登录；
        if session.get('user'):
            # 保存用户的评论信息
            comment = Comment(content=form.content.data,
                              movie_id=id,
                              user_id=session.get('user_id')
                              )
            db.session.add(comment)
            db.session.commit()
            flash("评论提交成功")
        else:
            flash("提交评论失败， 请先登录")
        return redirect(url_for('home.play', id=id), )

    if not id: abort(404)
    if not page: page = 1
    movie = Movie.query.get_or_404(id)
    # 获取当前电影的所有评论数量
    count = Comment.query.filter_by(movie_id=id).count()
    # 获取评论信息(评论会员的头像, 名称， 电影名， 评论时间， 评论内容)
    commentsPageObj = Comment.query.filter_by(movie_id=id).paginate(
        page, per_page=app.config['PER_PAGE'])
    return render_template('home/play.html',
                           movie=movie,
                           count=count,
                           commentsPageObj=commentsPageObj,
                           form=form,
                           app=app)


@home.route('/moviecollect/add/')
@is_login
def add_moviecollect():
    movie_id = request.args.get('movie_id', '')
    user_id = request.args.get('user_id', '')
    # 判断某用户是否收藏该电影
    collectCount = MovieCollect.query.filter_by(user_id=user_id, movie_id=movie_id).count()
    # 如果已经收藏， 则返回ok=0
    if collectCount == 1:
        data = dict(ok=0)
    # 如果没有收藏, 添加收藏到数据库中， 并且返回ok=1
    else:
        moviecollect = MovieCollect(
            user_id=user_id,
            movie_id=movie_id
        )
        db.session.add(moviecollect)
        db.session.commit()
        data = dict(ok=1)
    # 因为数据要传给前端的Ajax， 所有必须转成json格式;
    import json
    return json.dumps(data)
