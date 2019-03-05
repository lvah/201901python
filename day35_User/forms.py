"""
文件名: $NAME.py
日期: 01  
作者: lvah
联系: xc_guofan@qq.com
代码描述: 


# 专门存储表单的操作

"""

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, \
    RadioField, SelectField, SelectMultipleField, TextAreaField
from wtforms.validators import DataRequired, EqualTo, Length, Email, Regexp


class RegisterForm(FlaskForm):
    # StringField <input type='text' name='name' required>
    # PasswordField <input type='password' name='password' required>
    name = StringField(
        label="用户名",
        # 验证: 用户名不能为空的
        validators=[DataRequired(), ]
    )
    password = PasswordField(
        label="密码",
        validators=[
            DataRequired(),
            # 验证密码长度是否为6～8之间， 如果不是， 则报错;
            Length(6, 16, message="密码格式不正确"),
        ]
    )
    repassword = PasswordField(
        "确认密码",
        validators=[
            DataRequired(),
            # 验证当前表单输入的内容和password这个表单输入的内容是否一致， 如果不一致， 报错;
            EqualTo('password', message="密码不一致")

        ]
    )

    email = StringField(
        label="邮箱",
        validators=[
            DataRequired(),
            # 验证当前表单输入的内容是否为一个邮箱地址， 如果不是， 则报错;
            Email(message="邮箱格式错误!")

        ]
    )
    phone = StringField(
        label="电话号码",
        validators=[
            DataRequired(),
            # 验证当前表单输入的电话号码是否符合首位为1，由11位数字组成的正则表达式， 如果不是， 则报错;
            Regexp(r'1\d{10}', message="电话号码格式错误!")
        ]
    )


    # 可以实现单选按钮， 但是不美观，
    # gender = RadioField(
    #     label="性别",
    #     coerce=int,
    #     choices=[(1, "男"), (2, "女")]
    #
    # )


    gender = SelectField(
            label="性别",
            coerce=int,
            choices=[(1, "男"), (2, "女")]
    )


    tech = SelectMultipleField(
        label="擅长领域",
        coerce=int,
        choices=[(1, 'python'), (2, 'linux'), (3, 'java'), (4, 'php'), (5, 'ruby'), (6, 'c++')]
    )

    submit = SubmitField(label="注册")


    """
    # 单选框
       <form>
        
       男:  <input type="radio" name="gender"  value="1">
       女:  <input type="radio" name="gender"  value="2">
        
        </form>
    """



class MailForm(FlaskForm):
    # 接收邮件的地址
    toEmails =  TextAreaField(
        label="接收的邮箱地址",
        validators=[DataRequired()],
        # 表单的详细描述， 一般不写
        description="每个邮箱地址之间用逗号分隔"

    )


    toFilename  = SelectField(
        label="邮件内容的类型",
        # "company", 是传递给后台的， "公司简介"是在前端显示的;
        choices =[("company", "公司简介"), ("course", "课程简介")]
    )

    submit = SubmitField(
        label="发送"
    )