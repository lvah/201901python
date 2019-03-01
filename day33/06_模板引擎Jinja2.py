"""
文件名: $NAME.py
日期: 26  
作者: lvah
联系: xc_guofan@qq.com
代码描述:

# 1. 什么是Jinja2模板引擎?

1). python的Web开发中， 业务逻辑(实质就是视图函数的内容)和页面逻辑(html
文件)分开的， 使得代码的可读性增强， 代码容易理解和维护；


2). 模板渲染: 在html文件中，通过动态赋值 ，
    将重新翻译好的html文件(模板引擎生效) 返回给用户的过程。

3). 其他的模板引擎: Mako, Template, Jinja2




# 2. 语法


# 1). Jinja2变量显示语法: {{ 变量名 }}
#  完整的过滤器查看位置: http://jinja.pocoo.org/docs/templates/#builtin-filters
Jinja2变量内置过滤器:
        safe            渲染值时不转义
        capitalize      把值的首字母转换成大写,其他字母转换成小写
        lower           把值转换成小写形式
        upper           把值转换成大写形式
        title           把值中每个单词的首字母都转换成大写
        trim            把值的首尾空格去掉
        striptags       渲染之前把值中所有的 HTML 标签都删掉



如何自定义过滤器?

# 2). for循环:
    {% for i in li%}

    {% endfor %}

# 3). if语句
    {% if user == 'westos'%}


    {% elif user == 'hello' %}

    {% else %}

    {% endif%}




# 4). 宏的操作====相当于函数

- 如何定义宏?
<!--相当于python里面的定义函数, 后面使用的场景: 分页显示-->
{%  macro render(id) %}
    <h1>hello world {{ id }}</h1>
{% endmacro %}


- 如何调用宏?
<!--调用定义好的宏(类似于python中的函数)-->
{{ render(1) }}
{{ render(2) }}
{{ render(3) }}


# 5). include包含操作
如何使用: {% include  "06_inclued.html"%}


# 6). 模板的继承: 一般网站的导航栏和底部不会变化， 为了避免重复编写导航栏信息;
# - 如何定义模板?
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>{% block title %}  {% endblock %}</title>
    </head>
    <body>
    <div style="width: 100px; height: 200px" > 这是导航栏</div>
    {% block body %}

    hello

    {% endblock %}

    <div style="width: 100px; height: 200px" >这是底部</div>

    </body>
    </html>


# - 如何继承基模板?
{% extends  '06_base.html'%}

{% block title %}
    继承案例
{% endblock %}


{% block body %}
<span style="color: green">这是最新填的block内容</span>

{% endblock %}
"""


from flask import  Flask, render_template
app = Flask(__name__)

class User(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return  "<User: %s>" %(self.name)

@app.route('/')
def index():
    message = " this is a Message "
    li = ['fentiao', 'fensi', 'fendai']
    info = {
        'name': 'fentiao',
        'age':10
    }
    fentiao = User(name="粉条", age=5)
    tags = "<h1>hello world</h1>"

    return  render_template('06_index.html',
                            message=message,
                            names = li,
                            info=info,
                            fentiao=fentiao,
                            tags = tags
                         )



@app.route('/users/')
def users():
    usersinfo = [('user%s' %(i), "password%s" %(i)) for i in range(100)]
    return  render_template('06_users.html',
                            usersinfo = usersinfo
                            )



@app.route("/macro/")
def macro():
    return  render_template('06_macro.html')




@app.route('/extends/')
def extends():
    return  render_template('06_use_block.html')
# **********************自定义过滤器******************************
# 定义一个函数
def format_data(s):
    return  "这是一个过滤器：" + s
# 将该函数添加到默认过滤器中;
app.add_template_filter(format_data, 'fmt')


if __name__ == '__main__':
    app.run()









