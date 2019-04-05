"""
文件名: urls.py
日期: 2019-04-05  
作者: lvah
联系: xc_guofan@qq.com
代码描述: 



"""



from django.urls import path
from .views import index, detail

urlpatterns =[
    path('', index, name='index'),
    path('detail/<int:id>/', detail, name='detail')
]

