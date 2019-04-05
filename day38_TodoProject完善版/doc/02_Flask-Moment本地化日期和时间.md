# 1. 为什么使用Flask-Moment?
   如果Web程序的用户来自世界各地，那么就思考如何让Web的世界和当地时间一致。
 服务器需要统一时间单位，这和用户所在的地理位置无关，所以一般会使用协调
 时间时（Coordinated Universal Time,UTC）。但是对于用户来说他们
 想看到的是自己所在的当地时间，而且使用当地惯用的格式。   


# 2. Flask-Moment实现原理?
 一个优雅的解决方法就是把时间单位发送给Web浏览器，转换成当地时间，
 然后渲染。Web浏览器可以更好的更成这一任务，因为他们能获得电脑中的
 时区和区域设置。
 
 
  有一个使用JavaScript开发的优秀客户端开源代码库，名为moment.js，
 它可以在浏览器中渲染日期和时间。Flask-Moment是一个Flask程序扩展，
 能把moment.js集成到Jinja2模板中。





# 3. 具体代码?


## 3-1. 模板的编写

- 除了moment.js.Flask_Moment还依赖jquery.js，要在HTML文档的引入这连个文件，这样可以选择使用哪个版本，
也可以使用扩展提供的辅助函数，从内容分发网络中引入通过测试的加新内容，必须使用JinJa2提供的super()函数。比如可以这样在基模板中的scripts块中引入这个库。


```

{% block script %}
{{ super()}}
{{ monent.include_moment()}}
{% endblock %}



```


## 3-2. 编辑视图函数

  为了处理时间，Flask-Moment向模板开放了monent类。
  所以代码可以把变量current_time（也就是UTC时间传给模板处理）传入模板进行渲染。就这样解决了本地时间问题



```
@app.route('/')
def index():
    return render_template('index.html',
                           current_time=datetime.utcnow())
```


## 3-3. 编辑页面逻辑

```
<p>The local date and time is {{ moment(current_time).format('LLL') }}.</p>
<p>That was {{ moment(current_time).fromNow(refresh=True) }}.</p>
```


# 4. 参考资料

Flask-Moment 实现了 moment.js 中的 format() 、 fromNow() 、 fromTime() 、 calendar() 、 valueOf()
和 unix() 方法。你可查阅文档(http://momentjs.com/docs/#/displaying/)学习 moment.js 提供的全部格式化选项。
