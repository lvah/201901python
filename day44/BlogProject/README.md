# 项目名称
支持Markdown语法和代码高亮的个人博客系统
基于xxx技术的xxxx系统

# 项目简介
(用了什么技术， 实现了什么功能， 特色点)
支持Markdown语法和代码高亮的个人博客系统采用了Django开发框架和pyhton编程语言， 
后台数据库使用Mariadb持久化存储， 前台模板使用Bootstrap前端框架， 可满足用户个人信息设置和博客发布于共享的需求, 
提供用户的注册， 登录， 管理文章， 文章评论等功能。


# 项目部署


- 数据库设置
- 依赖包安装
- 数据库迁移
- 创建超级用户
- 后台添加数据
- 运行服务





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
### 实现步骤:
- 设计详情页的URL地址;
- 编写详情页的视图函数
- 编写详情页模板；
- 模板继承；
### 难点一: url的反向获取
```
 <a href="/blog/detail/{{ post.id }}/" class="more-link">继续阅读 <span class="meta-nav">→</span></a>
```
在需要解析URL的地方，对于不同层级，Django提供了不同的工具用于URL反查：
- 在模板语言中：使用url模板标签。(也就是写前端网页时）
```
 <a href="{% url 'detail'  post.id %}" class="more-link">继续阅读 <span class="meta-nav">→</span></a>
```
- 在Python代码中：使用reverse()函数。（也就是写视图函数等情况时）
- 在更高层的与处理Django模型实例相关的代码中：使用get_absolute_url()方法。(也就>是在模型model中)

### 难点二: 主页和详情页的模板继承
- 如何设置模板?
- 如何继承模板?










# 特色设置


## 1.支持Markdown语法和代码高亮


> 为了让博客文章具有良好的排版，显示更加丰富的格式，我们使用 Markdown 语法来书写我们的博文。Markdown 是一种 HTML 文本标记语言，只要遵循它约定的语法格式，Markdown 的渲染器就能够把我们写的文章转换为标准的 HTML 文档，从而让我们的文章呈现更加丰富的格式，例如标题、列表、代码块等等 HTML 元素。由于 Markdown 语法简单直观，不用超过 5 分钟就可以掌握常用的标记语法，因此大家青睐使用 Markdown 书写 HTML 文档。下面让我们的博客也支持使用 Markdown 书写。

- 安装python Markdown
- 视图层渲染Markdown文本
- Django的过滤器safe
- Pygments实现代码高亮
> Pygments 的工作原理是把代码切分成一个个单词，然后为这些单词添加 css 样式，不同的词应用不同的样式，这样就实现了代码颜色的区分，即高亮了语法。



## 2. 页面侧边栏(使用自定义模板标签)


### 2-1. 什么场景需要自定义模板标签?
- 什么是模板标签?

```
{% for post in posts %}
{% endfor %}


{% if post %}
{% endif %}
```


### 2-2. 如何自定义模板标签?








## 3. 博客的分类于归档

```
# 设计路由地址
- 获取分类信息的url地址:   /category/<int:id>/
- 获取标签信息的url地址:   /tag/<int:id>/
```




## 4. 博客评论提交与显示(**Django 表单的使用)






## 5. 分页显示



```



- Paginator 类的常用方法
```
from django.core.paginator import Paginator

# 1). 实例化分页对象
# 对 item_list 进行分页，每页包含 3 个数据。
item_list = ['john', 'paul', 'george', 'ringo']
p = Paginator(item_list, 3)


# 2). 取特定页的数据：
# 取第 2 页的数据
page2 = p.page(2)
page2.object_list



# 3).查询特定页的当前页码数：
page2.number


# 4). 查看分页后的总页数：
p.num_pages



# 5). 是否存在上一页/下一页?
page2.has_previous()
page2.previous_page_number()
page2.has_next()
page2.next_page_number()
```





```






