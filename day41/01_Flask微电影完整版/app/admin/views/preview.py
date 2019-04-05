"""
文件名: preview.py
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
from app.admin.forms.preview import PreviewForm
from app.admin.utils import write_adminlog, is_admin_login, permission_control
from app.home import change_filename
from app.models import Preview


@admin.route('/preview/add/', methods=['POST', 'GET'])
@is_admin_login
@permission_control
def preview_add():
    form = PreviewForm()
    if form.validate_on_submit():
        data = form.data
        # 判断预告标题是否已经存在?
        if Preview.query.filter_by(name=data['name']).count() == 1:
            flash('预告标题已存在，请检查！', category='err')
            return redirect(url_for('admin.preview_add'))
        # 存储预告封面;
        file_logo = secure_filename(form.logo.data.filename)  # 获取上传文件名字
        file_save_path = app.config['PREVIEW_UP_DIR']  # 文件上传保存路径
        if not os.path.exists(file_save_path):
            os.makedirs(file_save_path)  # 如果文件保存路径不存在，则创建一个多级目录
        logo = change_filename(file_logo)  # 文件重命名
        form.logo.data.save(os.path.join(file_save_path ,logo))  # 保存文件到磁盘中

        # 写入数据库;
        preview = Preview(
            name=data['name'],
            logo=logo  # 只在数据库中保存文件名
        )
        db.session.add(preview)
        db.session.commit()
        flash('添加预告%s成功' % (preview.name), 'ok')
        write_adminlog('添加预告%s成功' % (preview.name))
        return redirect(url_for('admin.preview_add'))
    return render_template('admin/preview/add.html', form=form)


@admin.route('/preview/list/')
@admin.route('/preview/list/<int:page>/')
@is_admin_login
@permission_control
def preview_list(page=1):
    previewsPageObj = Preview.query.paginate(page=page, per_page=app.config['PER_PAGE'])
    return render_template('admin/preview/list.html', previewsPageObj=previewsPageObj, app=app)


@admin.route('/preview/delete/<int:id>/')
@is_admin_login
@permission_control
def preview_del(id=None):
    if id:
        preview = Preview.query.filter_by(id=id).first_or_404()
        # 删除电影同时要从磁盘中删除电影的文件和封面文件
        file_save_path = app.config['PREVIEW_UP_DIR']  # 文件上传保存路径
        # 如果存在将进行删除，不判断，如果文件不存在,删除会报错
        if os.path.exists(os.path.join(file_save_path, preview.logo)):
            os.remove(os.path.join(file_save_path, preview.logo))

        # 删除数据库，提交修改，注意后面要把与电影有关的评论都要删除
        db.session.delete(preview)
        db.session.commit()
        # 删除后闪现消息
        flash('删除预告%s成功！' % (preview.name), category='ok')
        write_adminlog('删除预告%s成功！' % (preview.name))
    return redirect(url_for('admin.preview_list', page=1))


@admin.route('/preview/edit/<int:id>/', methods=['POST', 'GET'])
@is_admin_login
@permission_control
def preview_edit(id=None):
    preview = Preview.query.get_or_404(id)
    form = PreviewForm(
        name=preview.name,
    )
    # 不验证上传文件
    form.logo.validators = []

    if form.validate_on_submit():
        data = form.data
        if Preview.query.filter_by(name=data['name']).count() == 1 and preview.title != data['title']:
            flash('预告标题已存在，请重新输入', category='err')
            return redirect(url_for('admin.preview_edit', id=id))

        preview.name = data['name']

        print(data['logo'], type(data['logo']), form.logo.data, type(form.logo.data))
        # <FileStorage: 'ssh.jpg' ('image/jpeg')> <class 'werkzeug.datastructures.FileStorage'>
        # <FileStorage: 'ssh.jpg' ('image/jpeg')> <class 'werkzeug.datastructures.FileStorage'>
        # 上面两种方式结果一样

        # 文件保存路径操作
        file_save_path = app.config['PREVIEW_UP_DIR']  # 文件上传保存路径
        if not os.path.exists(file_save_path):
            os.makedirs(file_save_path)  # 如果文件保存路径不存在，则创建一个多级目录
        if form.logo.data:  # 当有上传新的图片
            if os.path.exists(os.path.join(file_save_path, preview.logo)):
                os.remove(os.path.join(file_save_path, preview.logo))  # 删除旧图片
            file_logo_name = form.logo.data.filename
            preview.logo = change_filename(file_logo_name)  # 得到新的文件名，保存到输入局
            form.logo.data.save(file_save_path + preview.logo)
        db.session.commit()
        flash('预告%s信息修改成功' % (preview.name), category='ok')
        write_adminlog('预告%s信息修改成功' % (preview.name))
        return redirect(url_for('admin.preview_edit', id=id))
    return render_template('admin/preview/edit.html', form=form, preview=preview)
