
@admin.route('/tag/edit/<int:id>/', methods=['POST', 'GET'])
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
def tag_del(id):
    if id:
        tag = Tag.query.filter_by(id=id).first_or_404()
        db.session.delete(tag)
        db.session.commit()
        # 删除后闪现消息
        flash('删除标签%s成功！' % (tag.name), category='ok')
        write_adminlog('删除标签%s成功！' % (tag.name))
        return redirect(url_for('admin.tag_list', page=1))

