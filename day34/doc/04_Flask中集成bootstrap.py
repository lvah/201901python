"""
文件名: $NAME.py
日期: 28  
作者: lvah
联系: xc_guofan@qq.com
代码描述: 

# 1. 什么是Bootstrap?
    Bootstrap(http://getbootstrap.com/)是 Twitter 开发的一个开源框架,
    它提供的用户界面组件可用于创建整洁且具有吸引力的网页,而且这些网页还能兼容
    所有现代 Web 浏览器。

# 2. Flask中如何集成Bootstrap?
    使用 pip 安装Flask-Bootstrap 的 Flask 扩展,简化集成的过程。
    from flask.ext.bootstrap import Bootstrap
    bootstrap = Bootstrap(app)



# 3. Flask-Bootstrap实现了什么?
- 利用 Jinja2 的模板继承机制,让程序扩展一个具有基本页面结构的基模板,其中
就有用来引入 Bootstrap 的元素。
{ % extends "bootstrap/base_other.html" % }

- 基模板中定义了可在衍生模板中重定义的块。
        块名                    说 明
        doc                     整个 HTML 文档
        html_attribs            <html> 标签的属性
        html <html>             标签中的内容
        head <head>             标签中的内容
        title <title>           标签中的内容
        metas                   一组 <meta> 标签
        styles                  层叠样式表定义
        body_attribs            <body> 标签的属性
        body                    <body> 标签中的内容
        navbar                  用户定义的导航条
        content                 用户定义的页面内容
        scripts                 文档底部的 JavaScript 声明


- 程序需要向已经有内容的块中添加新内容,必须使用 Jinja2 提供的 super() 函数。

{% block scripts %}
{{ super() }}
<script type="text/javascript" src="my-script.js"></script>
{% endblock %}

"""





