<h1>基于Flask的微电影管理系统</h1>

# 项目介绍

实现了微电影前后台管理。采用异步的方式,通过AJAX从服务端获取数据,并使用jQuery动态更新数据。
网站实现的功能包括首页显示、注册登录、会员中心, 电影播放页面、搜索页面、收藏页面,评论页面, 标签管理,电
影管理,权限管理等。 



# 项目技术
- Flask + Bootstrap + MySQL + Nginx

- Flask-wtf: 

- Flask-Moment:
```
Flask-Moment又是一个flask的扩展模块，用来处理时间日期等信息。用这个模块主要是考虑到两点，
        - 第一是为了让不同时区的用户看到的都是各自时区的实际时间，而不是服务器所在地的时间。
        - 第二是对于一些时间间隔的处理，如果要手动处理很麻烦，如果有模块就很好了。
```
- Flask-Mail
- Flask-Bootstrap
- Flask-sqlchemy
- Flask-Migrate
- Flask-Script
```
Flask-Scropt插件为在Flask里编写额外的脚本提供了支持。这包括运行一个开发服务器，
一个定制的Python命令行，用于执行初始化数据库、定时任务和其他属于web应用之外的命
令行任务的脚本。
```

- Ueditor

```
UEditor是由百度WEB前端研发部开发的所见即所得的开源富文本编辑器，具有轻量、可定制、用户体验优秀等特点。
```
- Ajax

```



```


# 难点分析



# 项目部署
## 安装依赖模块

```
pip  install -r requirement.txt 
```
## 导入sql数据
```
mysql -uroot -predhat MovieProject < movieWeb.sql
```

## 修改MySQL密码和数据库位置
```
# config.py
SQLALCHEMY_DATABASE_URI = "mysql://root:redhat@localhost/MovieProject"
``` 

## 启动服务
```
python manage.py  runserver


```




# 效果图展示





