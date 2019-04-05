"""
文件名: forms.py
日期: 2019-03-17  
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
            Length(6, 12, message="密码长度必须为6-12")

        ]
    )


class LoginForm(BaseForm):
    submit = SubmitField(
        label="登录"
    )


class RegisterForm(BaseForm):
    repassword = PasswordField(
        label="确认密码",
        validators=[
            EqualTo('password', message="两次密码不一致")
        ]
    )
    email = StringField(
        label="邮箱",
        validators=[
            Email(message="邮箱格式不正确")
        ]
    )

    submit = SubmitField(
        label="注册"
    )


class EditUserForm(FlaskForm):
    username = StringField(
        label="用户名",
        validators=[
            DataRequired()

        ]
    )
    email = StringField(
        label="邮箱",
        # validators=[
        #     Email(message="邮箱格式不正确")
        # ]
    )

    phone = StringField(
        label="电话",
        # validators=[
        #     Regexp(r'1\d{10}', message="电话号码格式不正确")
        # ]
    )
    face = FileField(
        label="用户头像",
        validators=[
            # *******限制用户上传文件的格式
            FileAllowed(['png', 'jpg'], message="用户头像格式错误， 必须为png或者jpg")

        ]
    )

    info = TextAreaField(
        label="用户简介",
    )

    submit = SubmitField(
        label="更新信息"
    )


class PwdForm(FlaskForm):
    old_pwd = PasswordField(
        label="旧密码",
        validators=[
            DataRequired()
        ],
        # <input name="xxx" placeholder="">
        render_kw={
            'placeholder': "请输入旧密码"
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


class CommentForm(FlaskForm):
    content = TextAreaField(
        label="内容",
        validators=[DataRequired(),
                    ],
        render_kw={
            'placeholder': "评论内容",
            'id': 'input_content'
        }
    )
    submit = SubmitField(
        label="提交评论",
        render_kw={
            'class': 'btn btn-success pull pull-right'
        }
    )
