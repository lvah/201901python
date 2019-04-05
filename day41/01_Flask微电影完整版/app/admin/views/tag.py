"""
文件名: tag.py
日期: 2019-03-24  
作者: lvah
联系: xc_guofan@qq.com
代码描述: 



"""
from app import app, db
from flask import render_template, flash, redirect, url_for,request
from app.admin import admin
from app.admin.forms.tag import TagForm, EditTagForm
from app.admin.utils import write_adminlog, permission_control, is_admin_login
from app.models import Tag


@admin.route('/tag/list/')
@admin.route('/tag/list/<int:page>/')
@is_admin_login
@permission_control
def tag_list(page=1):
    tagsPageObj = Tag.query.paginate(page, per_page=app.config['PER_PAGE'])
    return render_template('admin/tag/list.html',
                           tagsPageObj=tagsPageObj)

@admin.route('/tag/add/', methods=['POST', 'GET'])
@is_admin_login
@permission_control
def tag_add():
    form = TagForm()
    if form.validate_on_submit():
        name = form.name.data
        # 判断添加的标签是否存在?
        tag = Tag.query.filter_by(name=name).first()
        if tag:
            flash("标签%s已经存在" % (tag.name))
            return redirect(url_for('admin.tag_add'))
        tag = Tag(name=name)
        db.session.add(tag)
        db.session.commit()
        flash("标签%s添加成功" % (tag.name))
        # ******将添加标签的操作记录到数据库中
        write_adminlog("标签%s添加成功" % (tag.name))
        return redirect(url_for('admin.tag_add'))
    return render_template('admin/tag/add.html',
                           form=form)

@admin.route('/tag/edit/<int:id>/', methods=['POST', 'GET'])
@is_admin_login
@permission_control
def tag_edit(id):
    form = EditTagForm()
    tag = Tag.query.filter_by(id=id).first_or_404()
    old_tagname = tag.name
    form.name.data = tag.name
    if form.validate_on_submit():
        name = request.form['name']
        # 判断要更新的标签名是否已经存在?
        if name != tag.name and Tag.query.filter_by(name=name).first():
            flash("标签%s已经存在" % (name))
            return redirect(url_for('admin.tag_list', page=1))
        tag.name = name
        db.session.add(tag)
        db.session.commit()
        flash("更新标签为%s成功!" % (name), category='ok')
        write_adminlog("更新标签(%s)为%s成功!" % (old_tagname, name))
        return redirect(url_for('admin.tag_list', page=1))
    return render_template('admin/tag/edit.html',
                           form=form)

@admin.route('/tag/delete/<int:id>/')
@is_admin_login
@permission_control
def tag_del(id):
    if id:
        tag = Tag.query.filter_by(id=id).first_or_404()
        db.session.delete(tag)
        db.session.commit()
        # 删除后闪现消息
        flash('删除标签%s成功！' % (tag.name), category='ok')
        write_adminlog('删除标签%s成功！' % (tag.name))
        return redirect(url_for('admin.tag_list', page=1))
