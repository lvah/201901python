# 项目名称
支持Markdown语法和代码高亮的个人博客系统
基于xxx技术的xxxx系统

# 项目简介
(用了什么技术， 实现了什么功能， 特色点)
支持Markdown语法和代码高亮的个人博客系统采用了Django开发框架和pyhton编程语言， 
后台数据库使用Mariadb持久化存储， 前台模板使用Bootstrap前端框架， 可满足用户个人信息设置和博客发布于共享的需求, 
提供用户的注册， 登录， 管理文章， 文章评论等功能。




# 项目实现步骤


## 1.数据库模型设计



## 2.URL路由配置
- 如何实现路由分发?




## 3.Django Admin后台发布文章






## 4.博客首页设置


### 难点一：截取中文的博客内容

```
# 模板引擎: 
    Flask ---Jinja2
    Django ----Django模板引擎


Django的模板过滤器: 
    截取字符串的前几个字符: 
        1). 全部为英文； {{ 'cdfrgelkjugth' | truncatewords: '30' }}
        2). 截取中文: {{ 'dfrfrhgyth' | slice:"30" }}
```


### 难点二: 静态文件目录位置指定(BlogProject/settings.py)
```
# 设置静态资源位置；
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
```


## 5. 博客详情页设置


实现步骤:
- 设计详情页的URL地址;
- 编写详情页的视图函数
- 编写详情页模板；
- 模板继承；






















