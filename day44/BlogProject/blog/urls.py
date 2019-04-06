"""
文件名: urls.py
日期: 2019-04-05  
作者: lvah
联系: xc_guofan@qq.com
代码描述: 



"""



from django.urls import path
from .views import index, detail, category, tag, archive, search

urlpatterns =[
    path('', index, name='index'),
    path('detail/<int:id>/', detail, name='detail'),
    path('category/<int:id>/', category, name='category'),
    path('tag/<int:id>/', tag, name='tag'),
    path('archive/<int:year>/<int:month>/', archive, name='archive'),
    path('search/', search, name='search'),
]

