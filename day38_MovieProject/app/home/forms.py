"""
文件名: forms.py
日期: 2019-03-17  
作者: lvah
联系: xc_guofan@qq.com
代码描述: 



"""


from flask_wtf import  FlaskForm
from wtforms import  StringField, PasswordField, SubmitField
from wtforms.validators import  DataRequired, Length


class LoginForm(FlaskForm):
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
            Length(6, 12, message="密码长度必须为6-12")

        ]
    )
    submit = SubmitField(
        label="登录"
    )





