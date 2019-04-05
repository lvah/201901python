"""
文件名: role.py
创建时间: 2019-03-22 15:
作者: lvah
联系方式: 976131979@qq.com
代码描述:


"""

from flask_wtf import FlaskForm
from wtforms import StringField, FileField, SubmitField, SelectMultipleField
from wtforms.validators import DataRequired

from app.models import Auth


class BaseForm(FlaskForm):
    name = StringField(
        label='角色名称',
        validators=[
            DataRequired('请输入角色名称！')
        ],
    )
    auths = SelectMultipleField(
        label='权限列表',
        description='请选择权限列表！(可多选)',
        coerce=int,
        # choices=[(item.id, item.name) for item in Auth.query.all()]
    )

    def __init__(self, *args, **kwargs):
        super(BaseForm, self).__init__(*args, **kwargs)
        self.auths.choices = [(item.id, item.name) for item in Auth.query.all()]


class RoleForm(BaseForm):
    submit = SubmitField(
        label='添加角色',

    )


class EditRoleForm(BaseForm):
    submit = SubmitField(
        label='编辑角色',
    )
