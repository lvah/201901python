# Django 2.0 新款URL配置详解



Django2.0发布后，很多人都拥抱变化，加入了2的行列。
但是和1.11相比，2.0在url的使用方面发生了很大的变化，下面介绍一下：


```
urlpatterns = [
    path('articles/2003/', views.special_case_2003),
    path('articles/<int:year>/', views.year_archive),
    path('articles/<int:year>/<int:month>/', views.month_archive),
    path('articles/<int:year>/<int:month>/<slug:slug>/', views.article_detail),
]


注意：
        要捕获一段url中的值，需要使用尖括号，而不是之前的圆括号；
        可以转换捕获到的值为指定类型，比如例子中的int。默认情况下，捕获到的结果保存为字符串类型，不包含/这个特殊字符；
        匹配模式的最开头不需要添加/，因为默认情况下，每个url都带一个最前面的/，既然大家都有的部分，就不用浪费时间特别写一个了。


匹配例子：
        /articles/2005/03/ 将匹配第三条，并调用views.month_archive(request, year=2005, month=3)；
        /articles/2003/匹配第一条，并调用views.special_case_2003(request)；
        /articles/2003将一条都匹配不上，因为它最后少了一个斜杠，而列表中的所有模式中都以斜杠结尾；
        /articles/2003/03/building-a-django-site/ 将匹配最后一个，并调用views.article_detail(request, year=2003, month=3, slug="building-ae"
        
        
```




# path转换器


默认情况下，Django内置下面的路径转换器：

        - str：匹配任何非空字符串，但不含斜杠/，如果你没有专门指定转换器，那么这个是默认使用的；
        - int：匹配0和正整数，返回一个int类型
        - slug：可理解为注释、后缀、附属等概念，是url拖在最后的一部分解释性字符。该转换器匹配任何ASCII字符以及连接符和下划线，比如’ building-your-1st-django-site‘；
        - uuid：匹配一个uuid格式的对象。为了防止冲突，规定必须使用破折号，所有字母必须小写，例如’075194d3-6885-417e-a8a8-6c931e272f00‘ 。返回一个UUID对象；
        - path：匹配任何非空字符串，重点是可以包含路径分隔符’/‘。这个转换器可以帮助你匹配整个url而不是一段一段的url字符串。





# 使用正则表达式


Django2.0的url虽然改‘配置’了，但它依然向老版本兼容。而这个兼容的办法，就是用re_path()方法代替path()方法。re_path()方法在骨子里，根本就是以什么太大的差别？


```
urlpatterns = [
    path('articles/2003/', views.special_case_2003),
    re_path('articles/(?P<year>[0-9]{4})/', views.year_archive),
    re_path('articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/', views.month_archive),
    re_path('articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<slug>[\w-_]+)/', views.article_detail),
]


```


与path()方法不同的在于两点：
        year中匹配不到10000等非四位数字，这是正则表达式决定的
        传递给视图的所有参数都是字符串类型。而不像path()方法中可以指定转换成某种类型。在视图中接收参数时一定要小心。