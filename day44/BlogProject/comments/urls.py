"""
文件名: urls.py
日期: 2019-04-06  
作者: lvah
联系: xc_guofan@qq.com
代码描述: 



"""
from django.urls import path
from .views import  post_comment

urlpatterns = [
    # /comments/post/id
    path('post/<int:id>/', post_comment, name='post_comment'),
]


