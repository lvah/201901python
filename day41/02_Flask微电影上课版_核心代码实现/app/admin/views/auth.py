"""
文件名: auth.py
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
from app.admin.forms.auth import AuthForm
from app.admin.utils import write_adminlog, is_admin_login

# ***********************************权限管理操作*****************************
from app.models import Auth


@admin.route("/auth/add/", methods=['GET', 'POST'])
@is_admin_login
def auth_add():
    form = AuthForm()
    if form.validate_on_submit():
        data = form.data
        if Auth.query.filter_by(url=data['url']).count() == 1:
            flash('权限链接地址已存在！', category='err')
            return redirect(url_for('admin.auth_add'))
        auth = Auth(
            name=data['name'],
            url=data['url']
        )
        db.session.add(auth)
        db.session.commit()
        flash('权限地址%s添加成功！' % (auth.name), category='ok')
        write_adminlog('权限地址%s添加成功！' % (auth.name))
    return render_template('admin/auth/add.html', form=form)


@admin.route("/auth/list/")
@admin.route("/auth/list/<int:page>/")
@is_admin_login
def auth_list(page=1):
    authsPageObj = Auth.query.order_by(Auth.addtime.desc()).paginate(page=page, per_page=app.config['PER_PAGE'])
    return render_template('admin/auth/list.html', authsPageObj=authsPageObj)


@admin.route("/auth/delete/<int:id>/")
@is_admin_login
def auth_del(id=None):
    if id:
        auth = Auth.query.get_or_404(id)
        db.session.delete(auth)
        db.session.commit()
        flash('删除权限地址%s成功' % (auth.name), category='ok')
        write_adminlog('删除权限地址%s成功' % (auth.name))
        return redirect(url_for('admin.auth_list', page=1))


@admin.route("/auth/edit/<int:id>/", methods=['GET', 'POST'])
@is_admin_login
def auth_edit(id=None):
    auth = Auth.query.get_or_404(id)
    form = AuthForm(
        name=auth.name,
        url=auth.url
    )
    if form.validate_on_submit():
        data = form.data
        if Auth.query.filter_by(url=data['url']).count() == 1 and auth.url != data['url']:
            flash('权限链接地址已存在！', category='err')
            return redirect(url_for('admin.auth_edit', id=id))
        auth.name = data['name']
        auth.url = data['url']
        db.session.commit()
        flash('权限地址<%s>修改成功！' % (auth.url), category='ok')
        write_adminlog('权限地址<%s>修改成功！' % (auth.url))
    return render_template('admin/auth/edit.html', form=form)
