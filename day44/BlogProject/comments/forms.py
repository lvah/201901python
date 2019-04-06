"""
文件名: forms.py
日期: 2019-04-06  
作者: lvah
联系: xc_guofan@qq.com
代码描述: 



"""




from django import forms

#
# class CommentForm(forms.Form):
#     name = forms.CharField(
#
#     )
from comments.models import Comment
class CommentForm(forms.ModelForm):
    class Meta():
        # 指定该表单关联的数据库对象;
        model = Comment
        # 如果不指定， 数据库对象的每个属性都需要创建表单;
        # 如果指定fields, 只需要创建指定属性的表单;
        fields = ['name', 'email', 'text']


