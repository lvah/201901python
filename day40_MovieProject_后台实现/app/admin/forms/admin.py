"""
文件名: admin.py
创建时间: 2019-03-22 15:
作者: lvah
联系方式: 976131979@qq.com
代码描述:


"""

from wtforms.validators import DataRequired, ValidationError, EqualTo
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, SelectField
from wtforms.validators import DataRequired

from app.models import Role


class BaseForm(FlaskForm):
    name = StringField(
        label='管理员名称',
        validators=[
            DataRequired('请输入管理员名称！')
        ],
    )

    pwd = PasswordField(
        label='管理员密码',
        validators=[
            DataRequired('请输入管理员密码！')
        ],
    )
    repwd = PasswordField(
        label='管理员确认密码',
        validators=[
            DataRequired('请输入管理员确认密码！'),
            EqualTo('pwd', message='两次密码不一致')
        ],
    )
    is_super = SelectField(
        label='是否超级管理员',
        description='默认为普通管理员',
        coerce=int,
        choices=[(0, '普通管理员'), (1, '超级管理员')],

    )
    role_id = SelectField(
        label='所属角色',
        validators=[
            DataRequired('请选择所属角色！')
        ],
        coerce=int,
        # choices=[(role.id, role.name) for role in Role.query.all()],
        description='所属角色',

    )

    def __init__(self, *args, **kwargs):
        super(BaseForm, self).__init__(*args, **kwargs)
        self.role_id.choices = [(v.id, v.name) for v in Role.query.all()]


class AdminForm(BaseForm):
    submit = SubmitField(
        label='添加管理员',
    )


class EditAdminForm(BaseForm):
    submit = SubmitField(
        label='编辑管理员',
    )
