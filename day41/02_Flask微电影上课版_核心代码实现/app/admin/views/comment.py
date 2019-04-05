"""
文件名: comment.py
日期: 2019-03-24  
作者: lvah
联系: xc_guofan@qq.com
代码描述: 



"""

from app import app, db
from flask import render_template, flash, redirect, url_for, request
from app.admin import admin
from app.admin.utils import write_adminlog, is_admin_login
from app.models import User, Comment


# ***************************评论管理*****************************
@admin.route("/comment/list/")
@admin.route("/comment/list/<int:page>/")
@is_admin_login
def comment_list(page=1):
    commentsPageObj = Comment.query.paginate(page, per_page=app.config['PER_PAGE'])
    return render_template('admin/comment/list.html', commentsPageObj=commentsPageObj)


@admin.route("/comment/delete/<int:id>/")
@is_admin_login
def comment_delete(id=None):
    if id:
        comment = Comment.query.get_or_404(id)
        db.session.delete(comment)
        db.session.commit()
        flash('删除%s用户%s电影评论成功！' % (comment.user.name, comment.movie.name), category='ok')
        write_adminlog('删除%s用户%s电影评论成功！' % (comment.user.name, comment.movie.name))
        return redirect(url_for('admin.comment_list', page=1))
