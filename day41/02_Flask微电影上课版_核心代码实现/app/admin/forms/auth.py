"""
文件名: auth.py
创建时间: 2019-03-22 14:
作者: lvah
联系方式: 976131979@qq.com
代码描述:


"""
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class BaseForm(FlaskForm):
    name = StringField(
        label='权限名称',
        validators=[
            DataRequired('请输入权限名称！')
        ],
    )
    url = StringField(
        label='访问链接',
        validators=[
            DataRequired('请输入访问链接！')
        ],
    )


class AuthForm(BaseForm):
    submit = SubmitField(
        label='添加权限',
    )


class EditAuthForm(BaseForm):
    submit = SubmitField(
        label='更新权限',
    )
