# 1.什么是Flask-Script?

Flask-Script用来生成shell命令；为在Flask里编写额外的脚本提供了支持。

- 这包括运行一个开发服务器，一个定制的Python命令行，用于执行
初始化数据库、定时任务和其他属于web应用之外的命令行任务的脚本。
- Flask-Script和Flask本身的工作方式类似。只需要定义和添加能从命令行中
被Manager实例调用的命令即可。






# 2. 为什么使用Flask-Script?
Flask的开发Web服务器支持很多启动设置选项，但只能在脚本中作为参数传给app.run()函数。
这种方式很不方便，传递设置选项的理想方式是使用命令行参数。
Flask-Scrip就是这么一个Flask扩展，为Flask程序添加一个命令行解析器。
Flask-Script自带了一组常用选项，而且还支持自定义命令。





# 3. 如何安装Flask-Script?
pip install flask_script



# 4. 如何配置Flask-Script?

创建一个Python模块运行你的命令脚本。可以任意起名，例如manage.py。
无需把所有的命令都放在同一个文件里，例如，在一个大型项目中，可以把相关联的命令放在不同的文件里。

```
from flask_script import Manager

app = Flask(__name__)
# Manager类将追踪所有的在命令行中调用的命令和处理过程的调用运行情况;
# configure your app
manager = Manager(app)

if __name__ == "__main__":
    # 将启动Manger实例接收命令行中的命令。
    manager.run()
```




- 实现功能

```

(2048) [root@foundation0 day36]# python manage.py 
usage: manage.py [-?] {shell,runserver} ...

positional arguments:
  {shell,runserver}
    shell            Runs a Python shell inside Flask application context.
    runserver        Runs the Flask development server i.e. app.run()  # 运行服务器， 可以指定host和端口
 1010  python manage.py  runserver 
 1011  python manage.py  runserver  -h
 1012  python manage.py  runserver  -h '0.0.0.0' -p 8089

optional arguments:
  -?, --help         show this help message and exit



```

# 5. 添加自定义命令的3中方式:
- 网站参考: https://flask-script.readthedocs.io/en/latest/
    - 定义Command的子类;
    - 使用command装饰器
    - 使用option装饰器







# 6. 命令行拓展开发

> Extension developers can easily create convenient sub-manager instance within their extensions to make it easy for a user to consume all the available commands of an extension.
Here is an example how a database extension could provide (ex. database.py):

