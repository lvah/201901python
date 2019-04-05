"""
文件名: preview.py
日期: 2019-03-24  
作者: lvah
联系: xc_guofan@qq.com
代码描述: 



"""


from flask_wtf import FlaskForm
from wtforms import StringField, FileField, SubmitField
from wtforms.validators import DataRequired


class BaseForm(FlaskForm):
    name = StringField(
        label='预告标题',
        validators=[
            DataRequired('请输入预告标题！')
        ],
    )
    logo = FileField(
        label='预告封面',
        validators=[
            DataRequired('请上传预告封面！')
        ],
    )


class PreviewForm(BaseForm):
    submit = SubmitField(
        label='添加预告',
    )


class EditPreviewForm(BaseForm):
    submit = SubmitField(
        label='编辑预告',
    )



