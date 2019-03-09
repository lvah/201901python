import os

from flask import Flask, render_template, request, redirect, url_for, flash, session
from functools import wraps
from flask_bootstrap import Bootstrap
from flask_mail import Message, Mail

from forms import RegisterForm, MailForm

users = [
    {
        'username': 'root',
        'password': 'root'
    },
    {
        'username': 'hello',
        'password': 'root'
    },

]

# 实现用户注册， 用户登录， 用户注销， 用户查看;
app = Flask(__name__)
app.config['SECRET_KEY'] = 'westos'
bootstrap = Bootstrap(app)

# 配置发送邮件的相关信息;
# 指定邮件服务器的域名或者IP
app.config['MAIL_SERVER'] = 'smtp.qq.com'

# 指定端口， 默认25， 但qq邮箱默认为 端口号465或587；
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = '976131979'
app.config['MAIL_PASSWORD'] = "zqzjbjvkjzvpbcgd"


def is_login(f):
    """用来判断用户是否登录成功"""

    @wraps(f)
    def wrapper(*args, **kwargs):
        # 判断session对象中是否有seesion['user'],
        # 如果包含信息， 则登录成功， 可以访问主页；
        # 如果不包含信息， 则未登录成功， 跳转到登录界面;；
        if session.get('user', None):
            return f(*args, **kwargs)
        else:
            flash("用户必须登录才能访问%s" % (f.__name__))
            return redirect(url_for('login'))

    return wrapper


def is_admin(f):
    """用来判断用户是否登录成功"""

    @wraps(f)
    def wrapper(*args, **kwargs):
        # 判断session对象中是否有seesion['user']等于root,
        # 如果包含信息， 则登录成功， 可以访问主页；
        # 如果不包含信息， 则未登录成功， 跳转到登录界面;；
        if session.get('user', None) == 'root':
            return f(*args, **kwargs)
        else:
            flash("只有管理员root才能访问%s" % (f.__name__))
            return redirect(url_for('login'))

    return wrapper


# 面试常问： 复习： 1. 装饰器的工作原理；  2. 如果有多个装饰器， 运行流程是怎样的?
@app.route('/')
@is_login
def index():
    return render_template('index.html')


@app.route('/register/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get("username", None)
        password = request.form.get('password', None)

        # 当所有的信息遍历结束， 都没有发现注册的用户存在， 则将注册的用户添加到服务器， 并跳转登录界面;
        for user in users:
            if user['username'] == username:
                return render_template('register.html', message="用户%s已经存在" % (username))
        else:
            users.append(dict(username=username, password=password))
            # return redirect('/login/')

            # 出现一个闪现信息;
            flash("用户%s已经注册成功， 请登录....." % (username), category='info')
            return redirect(url_for('login'))
    return render_template('register.html')


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get("username", None)
        password = request.form.get('password', None)

        # 当所有的信息遍历结束， 都没有发的用户存在， 则将注册的用户添加到服务器， 并跳转登录界面;
        for user in users:
            if user['username'] == username and user['password'] == password:
                #  将用户登录的信息存储到session中;
                session['user'] = username
                return redirect(url_for('index'))
        else:
            # 出现一个闪现信息;
            flash("用户%s密码错误， 请重新登录....." % (username))
            return redirect(url_for('login'))
    return render_template('login.html')


@app.route('/logout/')
def logout():
    #  将用户存储到session中的信息删除;
    session.pop('user')
    flash("注销成功........")
    return redirect(url_for('login'))


@app.route('/delete/<string:username>/')
def delete(username):
    for user in users:
        # 用户存在， 则删除;
        if username == user['username']:
            users.remove(user)
            flash("删除用户%s成功" % (username))
    # else:
    #     flash("用户%s不存在" % (username))

    # 删除成功， 跳转到/list/路由中.....
    return redirect(url_for('list'))


@app.route('/list/')
@is_login
@is_admin
def list():
    return render_template('list.html',
                           users=users)


@app.route('/upload/', methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        # 获取用户上传的文件对象
        f = request.files['faceImg']
        # 获取上传文件的文件名
        # print(f.filename)

        # 获取当前项目的目录位置;
        basepath = os.path.dirname(__file__)
        # print(__file__)       # /root/PycharmProjects/day34/app.py
        # print(basepath)       # /root/PycharmProjects/day34

        # /root/PycharmProjects/day34/static/img/face/xxx.png
        # 拼接路径， 保存到本地的位置;
        filepath = os.path.join(basepath, 'static', 'img', 'face', f.filename)

        # 保存文件
        f.save(filepath)
        flash("上传文件%s成功" % (f.filename))
        return redirect(url_for('upload'))
    else:
        return render_template('upload.html')


# 测试表单的应用案例
@app.route('/wtf/', methods=['GET', 'POST'])
def wtf():
    from forms import RegisterForm
    # 1. 实例化表单， 将来传递到前端， 进行生成对应的html;
    form = RegisterForm()
    # 2. 判断HTTP请求方式， 返回不同的内容
    # 第一个判断: 是否为post请求? 判断提交的数据是否符合form表单定义的验证?
    # if request.method == 'POST':
    #     print(request.form['name'])
    #     return  'post'

    if form.validate_on_submit():
        username = request.form['name']
        password = request.form['password']
        gender = request.form['gender']
        tech = request.form['tech']

        # 当所有的信息遍历结束， 都没有发现注册的用户存在， 则将注册的用户添加到服务器， 并跳转登录界面;
        for user in users:
            if user['username'] == username:
                flash(message="用户%s已经存在" % (username))
                return redirect(url_for('wtf'))
        else:
            users.append(dict(username=username, password=password))
            # return redirect('/login/')

            # 出现一个闪现信息;
            flash("用户%s已经注册成功， 请登录....." % (username))
            return redirect(url_for('login'))

    return render_template("wtf.html",
                           form=form)


def send_mail(to, subject, template, **kwargs):
    mail = Mail(app)
    # app.app_context(): 将之前Flask创建的app作为参数传入AppContext类中,
    # 用于存储当前app的相关信息;
    with app.app_context():
        msg = Message(subject=subject,
                      sender='976131979@qq.com',
                      recipients=to,
                      # body=render_template(template + '.txt', **kwargs),
                      html=render_template(template + '.html', **kwargs)
                      )

        mail.send(msg)




@app.route('/mail/', methods=['GET', 'POST'])
def mail():
    # 实例化表单
    form = MailForm()
    if form.validate_on_submit():
        # 获取用户提交的数据;
        toEmails = form.toEmails.data.split(',')
        toFilename = form.toFilename.data

        try:
            send_mail(toEmails, "西部开源邮件测试", toFilename)
        except Exception as e:
            flash("邮件发送失败, 失败原因: %s!" %(e))
        else:
            flash("邮件发送成功!")
        return  redirect(url_for('mail'))

    return  render_template('send_mail.html',
                            form = form)



if __name__ == '__main__':
    app.run(port=5001)
