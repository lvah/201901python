"""
文件名: movie.py
日期: 2019-03-24  
作者: lvah
联系: xc_guofan@qq.com
代码描述: 



"""
from flask_wtf import FlaskForm
from flask_wtf.file import  FileAllowed
from wtforms import  StringField, FileField, TextAreaField, SelectField, DateField, SubmitField
from wtforms.validators import  DataRequired

from app.models import Tag


class BaseForm(FlaskForm):
    name = StringField(
        label="电影名",
        validators=[
            DataRequired()
        ]
    )
    url = FileField(
        label="电影文件",
        validators=[
            FileAllowed(['mp4', 'avi'], message="文件格式不正确. 只能接收mp4和avi格式")
        ]
    )
    info = TextAreaField(
        label="电影简介"
    )
    logo = FileField(
        label="电影封面",
        validators=[
            FileAllowed(['png', 'jpg'], message="文件格式不正确.")
        ]
    )

    star = SelectField(
        label="电影星级",
        coerce=int,
        choices=[(i+1, "%s星" %(i+1)) for i in range(5)]
    )

    tag_id = SelectField(
        label="电影标签",
        coerce=int,
        # choices=[(tag.id, tag.name) for tag in Tag.query.all()]
    )

    area = StringField(
        label="上映地区"
    )
    length = StringField(
        label="电影时长"
    )
    release_time = DateField(
        label="上映时间"
    )

    def __init__(self, *args, **kwargs):
        super(BaseForm, self).__init__(*args, **kwargs)
        # 当每次实例化表单时， 都重新查询标签的内容,
        self.tag_id.choices = [(tag.id, tag.name) for tag in Tag.query.all()]
class MovieForm(BaseForm):
    submit = SubmitField(
        label="添加电影"
    )

class EditMovieForm(BaseForm):
    submit = SubmitField(
        label="编辑电影"
    )
