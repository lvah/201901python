import json
from functools import wraps

from app import app, db

# 网站首页
from app.forms import RegisterForm, LoginForm, AddTodoForm, EditTodoForm
from flask import render_template, flash, redirect, url_for, session, request

from app.models import User, Todo


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


@app.route('/')
def index():
    return redirect(url_for('list'))


# 注册页面
@app.route('/register/', methods=['POST', 'GET'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        # 1. 从前端获取用户输入的值;
        email = form.email.data
        username = form.username.data
        password = form.password.data

        # 2. 判断用户是否已经存在? 如果返回位None，说明可以注册;
        u = User.query.filter_by(username=username).first()
        if u:
            flash("用户%s已经存在" % (u.username))
            return redirect(url_for('register'))
        else:
            u = User(username=username, email=email)
            u.password = password
            db.session.add(u)
            db.session.commit()
            flash("注册用户%s成功" % (u.username))
            return redirect(url_for('login'))
    return render_template('register.html',
                           form=form)


# 登录页面
@app.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        # 1. 判断用户是否存在?
        u = User.query.filter_by(username=username).first()
        if u and u.verify_password(password):
            session['user_id'] = u.id
            session['user'] = u.username
            flash("登录成功!")
            return redirect(url_for('index'))
        else:
            flash("用户名或者密码错误!")
            return redirect(url_for('login'))

    return render_template('login.html',
                           form=form)


@app.route('/logout/')
@is_login
def logout():
    session.pop('user_id', None)
    session.pop('user', None)

    return redirect(url_for('login'))


# 添加任务
@app.route('/todo/add/', methods=['GET', 'POST'])
@is_login
def todo_add():
    form = AddTodoForm()
    if form.validate_on_submit():
        # 获取用户提交的内容
        content = form.content.data
        category_id = form.category.data

        # 添加到数据库中
        # 用户登录才可以添加任务，
        todo = Todo(content=content,
                    category_id=category_id,
                    user_id=session.get('user_id'))
        db.session.add(todo)
        db.session.commit()
        flash("任务添加成功")
        return redirect(url_for('todo_add'))
    return render_template('todo/add_todo.html',
                           form=form)


# 编辑任务
@app.route('/todo/edit/<int:id>/', methods=['GET', 'POST'])
@is_login
def todo_edit(id):
    form = EditTodoForm()
    # *****重要: 编辑时需要获取原先任务的信息， 并显示到表单里面;
    todo = Todo.query.filter_by(id=id).first()
    form.content.data = todo.content
    form.category.data = todo.category_id
    if form.validate_on_submit():
        # 更新时获取表单数据一定要使用request.form方法获取， 而form.content.data并不能获取用户更新后提交的表单内容;
        # print(request.form)
        # content = form.content.data   # error
        # category_id = form.category.data   # error
        content = request.form.get('content')
        category_id = request.form.get('category')

        # 更新到数据库里面
        todo.content = content
        todo.category_id = category_id
        db.session.add(todo)
        db.session.commit()
        flash("更新任务成功")
        return redirect(url_for('list'))
    return render_template('todo/edit_todo.html',
                           form=form)


# 删除任务: 根据任务id删除
@app.route('/todo/delete/<int:id>/')
@is_login
def todo_delete(id):
    todo = Todo.query.filter_by(id=id).first()
    db.session.delete(todo)
    db.session.commit()
    flash("删除任务成功")
    return redirect(url_for('list'))


# 查看任务
@app.route('/todo/list/')
@app.route('/todo/list/<int:page>/')
@is_login
def list(page=1):
    # 任务显示需要分页
    # Todo.query.paginate(page, per_page=5)
    todoPageObj = Todo.query.filter_by(user_id=session.get('user_id')).paginate(page, per_page=app.config['PER_PAGE'])  # 在config.py文件中有设置;
    return render_template('todo/list_todo.html',
                           todoPageObj=todoPageObj,
                           )


# 修改任务状态为完成
@app.route('/todo/done/<int:id>/')
@is_login
def done(id):
    todo = Todo.query.filter_by(id=id).first()
    todo.status = True
    db.session.add(todo)
    db.session.commit()
    flash("修改状态成功")
    return redirect(url_for('list'))


# 修改任务状态为未完成
@app.route('/todo/undo/<int:id>')
@is_login
def undo(id):
    todo = Todo.query.filter_by(id=id).first()
    todo.status = False
    db.session.add(todo)
    db.session.commit()
    flash("修改状态成功")
    return redirect(url_for('list'))


@app.route('/showTodo/')
@is_login
def showTodo():
    done_count = Todo.query.filter_by(status=True).count()
    undone_count = Todo.query.filter_by(status=False).count()
    return render_template('todo/show_todo.html',
                           info={
                               '已完成': done_count,
                               '未完成': undone_count

                           })


@app.route('/newShowTodo/')
@is_login
def newShowTodo():
    return render_template('todo/new_show_todo.html')


@app.route('/get_data/')
@is_login
def get_data():
    done_count = Todo.query.filter_by(status=True).count()
    undone_count = Todo.query.filter_by(status=False).count()
    info = {
        'info': ["已完成", "未完成"],
        'count': [done_count, undone_count]
    }
    # 解决中文编码问题
    return json.dumps(info, ensure_ascii=False)


@app.route('/disk/')
def get_disk():
    import psutil
    cpuInfo = json.dumps({'CPU占有率', psutil.cpu_percent()},
                         ensure_ascii=False)

    return cpuInfo




