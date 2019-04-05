"""
文件名: main.py
日期: 2019-03-24  
作者: lvah
联系: xc_guofan@qq.com
代码描述: 



"""
from flask import session, flash, request, redirect, url_for, render_template
from werkzeug.security import generate_password_hash

from app import db
from app.admin import admin
from app.admin.forms.main import LoginForm, PwdForm
from app.admin.utils import is_admin_login, permission_control
from app.models import  Admin, Adminlog



@admin.errorhandler(404)
def page_not_found(error):
    return  render_template('admin/404.html'), 404



@admin.errorhandler(500)
def server_error(error):
    return  render_template('admin/500.html'), 500




@admin.errorhandler(403)
def no_permission(error):
    return  render_template('admin/403.html'), 403





@admin.route('/')
@is_admin_login
def index():
    return  render_template('admin/base.html')


@admin.route('/login/', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        name = form.username.data
        password = form.password.data
        admin = Admin.query.filter_by(name=name).first()
        if admin and admin.verify_password(password):
            # session信息的保存
            session['admin_id'] = admin.id
            session['admin'] = admin.name
            flash("管理员%s登录成功" % (admin.name))
            remote_ip = request.remote_addr
            # 将登录信息写到日志中;
            adminlog = Adminlog(admin_id=admin.id,
                              ip=remote_ip,
                              area='xxx内网IP')
            db.session.add(adminlog)
            db.session.commit()

            # 从index蓝图里面寻找index函数;
            return redirect(url_for('admin.index'))
        else:
            flash("管理员登录失败")
            return redirect(url_for('admin.login'))
    return render_template('admin/login.html',
                           form=form)


@admin.route('/logout/')
@is_admin_login
def logout():
    session.pop('admin_id', None)
    session.pop('admin', None)
    return redirect(url_for('admin.login'))



# 修改密码
@admin.route('/pwd/', methods=['GET', 'POST'])
def pwd():
    form = PwdForm()
    if form.validate_on_submit():
        # 获取当前登录用户的密码
        admin = Admin.query.filter_by(name=session.get('admin')).first()
        # 判断用户的旧密码是否正确
        if admin.verify_password(form.old_pwd.data):
            # ********数据库里面的是password
            admin.password = generate_password_hash(form.new_pwd.data)
            db.session.add(admin)
            db.session.commit()
            flash("密码更新成功")
        else:
            flash("旧密码错误, 请重新输入")
        return redirect(url_for('admin.pwd'))
    return render_template('admin/pwd.html', form=form)

