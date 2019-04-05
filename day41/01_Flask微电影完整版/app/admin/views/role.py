"""
文件名: role.py
日期: 2019-03-24  
作者: lvah
联系: xc_guofan@qq.com
代码描述: 



"""

import os

from werkzeug.utils import secure_filename

from app import app, db
from flask import render_template, flash, redirect, url_for,request
from app.admin import admin
from app.admin.forms.movie import MovieForm
from app.admin.forms.role import RoleForm, EditRoleForm
from app.admin.utils import write_adminlog, is_admin_login, permission_control
from app.home import change_filename


# **************************管理员角色操作********************************
from app.models import Role


@admin.route("/role/add/", methods=['GET', 'POST'])
@is_admin_login
@permission_control
def role_add():
    form = RoleForm()
    if form.validate_on_submit():
        data = form.data
        if Role.query.filter_by(name=data['name']).count() == 1:
            flash('管理员角色已存在！', category='err')
            return redirect(url_for('admin.role_add'))
        print(data['auths'])
        print(",".join(list(map(str, data['auths']))))
        role = Role(
            name=data['name'],
            # 默认多选返回的是一个列表, 里面存储的是权限的id号;
            auths=",".join(list(map(str, data['auths'])))
        )
        db.session.add(role)
        db.session.commit()
        flash('角色地址%s添加成功！' % (role.name), category='ok')
        write_adminlog('角色地址%s添加成功！' % (role.name))
    return render_template('admin/role/add.html', form=form)


@admin.route("/role/list/")
@admin.route("/role/list/<int:page>/")
@is_admin_login
@permission_control
def role_list(page=1):
    rolesPageObj = Role.query.order_by(Role.addtime.desc()).paginate(page=page, per_page=app.config['PER_PAGE'])
    return render_template('admin/role/list.html', rolesPageObj=rolesPageObj)


@admin.route("/role/delete/<int:id>/")
@is_admin_login
@permission_control
def role_del(id=None):
    if id:
        role = Role.query.get_or_404(id)
        db.session.delete(role)
        db.session.commit()
        flash('删除角色地址%s成功' % (role.name), category='ok')
        write_adminlog('删除角色地址%s成功' % (role.name))
        return redirect(url_for('admin.role_list', page=1))


@admin.route("/role/edit/<int:id>/", methods=['GET', 'POST'])
@is_admin_login
@permission_control
def role_edit(id=None):
    role = Role.query.get_or_404(id)
    form = EditRoleForm(
        name=role.name,
        auths=list(map(lambda item: int(item), role.auths.split(','))) if role.auths else ''  # 换回int型列表
    )
    if form.validate_on_submit():
        data = form.data
        if Role.query.filter_by(name=data['name']).count() == 1 and role.name != data['name']:
            flash('角色名已存在！', category='err')
            return redirect(url_for('admin.role_edit', id=id))
        role.name = data['name']
        role.auths = ",".join(map(str, data['auths']))
        db.session.commit()
        flash('角色<%s>修改成功！' % (role.name), category='ok')
        write_adminlog('角色地址<%s>修改成功！' % (role.name))
    return render_template('admin/role/edit.html', form=form)






