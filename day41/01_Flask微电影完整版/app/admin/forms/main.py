"""
文件名: main.py
日期: 2019-03-24  
作者: lvah
联系: xc_guofan@qq.com
代码描述: 



"""

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FileField, TextAreaField
from wtforms.validators import DataRequired, Length, EqualTo, Email, Regexp
from flask_wtf.file import FileAllowed


class BaseForm(FlaskForm):
    username = StringField(
        label="用户名",
        validators=[
            DataRequired()

        ]
    )
    password = PasswordField(
        label="密码",
        validators=[
            DataRequired(),
            # Length(6, 12, message="密码长度必须为6-12")

        ]
    )


class LoginForm(BaseForm):
    submit = SubmitField(
        label="登录"
    )




class PwdForm(FlaskForm):
    old_pwd = PasswordField(
        label="旧密码",
        validators=[
            DataRequired()
        ],
    # <input name="xxx" placeholder="">
    render_kw = {
        'placeholder' : "请输入旧密码"
    }
    )
    new_pwd = PasswordField(
        label="新密码",
        validators=[
            DataRequired()
        ],
        render_kw={
            'placeholder': "请输入新密码"
        }
    )

    submit = SubmitField(
        label="修改密码"
    )