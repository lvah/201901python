import os

from werkzeug.utils import secure_filename

from app import app, db
from flask import render_template, flash, redirect, url_for, request
from app.admin import admin
from app.admin.forms.admin import AdminForm
from app.admin.forms.movie import MovieForm
from app.admin.utils import write_adminlog, is_admin_login, permission_control
from app.home import change_filename


# *************************************管理员操作**************************************
from app.models import Admin


@admin.route("/admin/add/", methods=['GET', 'POST'])
@is_admin_login
@permission_control
def admin_add():
    form = AdminForm()
    from werkzeug.security import generate_password_hash
    if form.validate_on_submit():
        data = form.data
        if Admin.query.filter_by(name=data['name']).count() == 1:
            flash('管理员已存在！', category='err')
            return redirect(url_for('admin.admin_add'))

        if not data['is_super']:
            data['is_super'] = 0

        add_admin = Admin(
            name=data['name'],
            password=generate_password_hash(data['pwd']),
            role_id=data['role_id'],
            is_super=data['is_super']
        )
        db.session.add(add_admin)
        db.session.commit()
        flash('管理员添加成功', category='ok')
    return render_template('admin/admin/add.html', form=form)


@admin.route("/admin/list/")
@admin.route("/admin/list/<int:page>/")
@is_admin_login
@permission_control
def admin_list(page=1):
    adminsPageObj = Admin.query.order_by(
        Admin.addtime.desc()
    ).paginate(page=page, per_page=app.config['PER_PAGE'])
    return render_template('admin/admin/list.html', adminsPageObj=adminsPageObj)
