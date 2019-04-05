"""
文件名: user.py
日期: 2019-03-24  
作者: lvah
联系: xc_guofan@qq.com
代码描述: 



"""

import os

from werkzeug.utils import secure_filename

from app import app, db
from flask import render_template, flash, redirect, url_for, request
from app.admin import admin
from app.admin.utils import write_adminlog, is_admin_login, permission_control
from app.models import User


@admin.route("/user/list/")
@admin.route("/user/list/<int:page>/")
@is_admin_login
@permission_control
def user_list(page=1):
    usersPageObj = User.query.paginate(page=page, per_page=app.config['PER_PAGE'])
    return render_template('admin/user/list.html', usersPageObj=usersPageObj, app=app)


@admin.route("/user/view/<int:user_id>/")
@is_admin_login
@permission_control
def user_view(user_id=None):
    if user_id:
        user = User.query.get_or_404(user_id)
        return render_template('admin/user/view.html',
                               user=user,
                               app=app)


@admin.route("/user/delete/<int:id>/")
@is_admin_login
@permission_control
def user_del(id=None):
    if id:
        user = User.query.get_or_404(id)
        # 删除同时要从磁盘中删除封面文件
        file_save_path = app.config['FC_DIR']  # 头像上传保存路径
        # 如果存在将进行删除，不判断，如果文件不存在删除会报错
        if os.path.exists(os.path.join(file_save_path, user.face)):
            os.remove(os.path.join(file_save_path, user.face))

        # 删除数据库，提交修改
        db.session.delete(user)
        db.session.commit()
        # 删除后闪现消息
        flash('删除会员%s成功！' % (user.name), category='ok')
        write_adminlog('删除会员%s成功！' % (user.name))
        return redirect(url_for('admin.user_list', page=1))
