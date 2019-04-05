"""
文件名: collect.py
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
from app.admin.forms.movie import MovieForm
from app.admin.utils import write_adminlog, is_admin_login, permission_control
from app.models import MovieCollect


# ********************************收藏管理***********************


@admin.route("/collect/list/")
@admin.route("/collect/list/<int:page>/")
@is_admin_login
@permission_control
def collect_list(page=1):
    moviecollectsPageObj = MovieCollect.query.paginate(page=page, per_page=app.config['PER_PAGE'])
    return render_template('admin/collect/list.html', moviecollectsPageObj=moviecollectsPageObj, app=app)


@admin.route("/collect/delete/<int:id>")
@is_admin_login
@permission_control
def collect_del(id=None):
    if id:
        moviecollect = MovieCollect.query.get_or_404(id)
        db.session.delete(moviecollect)
        db.session.commit()
        flash('删除%s用户对%s电影收藏成功！' % (moviecollect.user.name, moviecollect.movie.name), category='ok')
        write_adminlog('删除%s用户对%s电影收藏成功')
        return redirect(url_for('admin.comment_list', page=1))
