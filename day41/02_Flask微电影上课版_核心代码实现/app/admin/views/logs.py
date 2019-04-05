"""
文件名: logs.py
日期: 2019-03-24  
作者: lvah
联系: xc_guofan@qq.com
代码描述: 



"""


import os

from werkzeug.utils import secure_filename

from app import app, db
from flask import render_template, flash, redirect, url_for, request, session
from app.admin import admin
from app.admin.forms.movie import MovieForm
from app.admin.utils import write_adminlog, is_admin_login
from app.home import change_filename
from app.models import Movie, Admin, AdminOplog, Adminlog, Userlog


# **************************管理员操作日志*****************************
@admin.route("/logs/operate_log/")
@admin.route("/logs/operate_log/<int:page>/")
@is_admin_login
def logs_operate_log(page=1):
    admin_id = session.get('admin_id')
    admin = Admin.query.get_or_404(admin_id)
    if admin.is_super:
        adminOplogPageObj = AdminOplog.query.paginate(page, per_page=app.config['PER_PAGE'])
    else:
        adminOplogPageObj = AdminOplog.query.filter_by(admin_id=admin_id
                                                       ).paginate(page,
                                                                  per_page=app.config['PER_PAGE'])

    return render_template('admin/logs/operate_log.html',
                           adminOplogPageObj=adminOplogPageObj)


# 管理员登录日志
@admin.route("/logs/admin_log/")
@admin.route("/logs/admin_log/<int:page>/")
@is_admin_login
def logs_admin_log(page=1):
    admin_id = session.get('admin_id')
    admin = Admin.query.get_or_404(admin_id)
    if admin.is_super:
        adminlogPageObj = Adminlog.query.paginate(page, per_page=app.config['PER_PAGE'])
    else:
        adminlogPageObj = Adminlog.query.filter_by(admin_id=admin_id
                                                   ).paginate(page,
                                                              per_page=app.config['PER_PAGE'])
    return render_template('admin/logs/admin_log.html',
                           adminlogPageObj=adminlogPageObj)


@admin.route("/logs/user_log/")
@admin.route("/logs/user_log/<int:page>/")
@is_admin_login
def logs_user_log(page=1):
    userlogPageObj = Userlog.query.paginate(page,
                                            per_page=app.config['PER_PAGE'])
    return render_template('admin/logs/user_log.html',
                           userlogPageObj=userlogPageObj)
