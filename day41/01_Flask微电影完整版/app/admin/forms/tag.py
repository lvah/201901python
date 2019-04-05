"""
文件名: tag.py
日期: 2019-03-24  
作者: lvah
联系: xc_guofan@qq.com
代码描述: 



"""
from flask_wtf import FlaskForm
from wtforms  import  StringField, SubmitField
from wtforms.validators import  DataRequired

class BaseForm(FlaskForm):
    name = StringField(
        label="标签名",
        validators=[
            DataRequired()
        ]
    )
class TagForm(BaseForm):
    submit = SubmitField(
        label="添加标签"
    )

class EditTagForm(BaseForm):
    submit = SubmitField(
        label="编辑标签"
    )