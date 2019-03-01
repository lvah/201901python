"""
文件名: $NAME.py
日期: 26  
作者: lvah
联系: xc_guofan@qq.com
代码描述: 

Flask是python编写的， Web应用框架；微内核的web框架;  ---小型网站
Django:全能型框架;  --- 大型网站（ERP）
Tornado:




需要掌握:
    - 如何实现简单的web服务网站?
    - 什么是路由?
    - 什么是视图函数?

"""

# 1. 导入Flask类
from flask import Flask
app = Flask(__name__)

# 实现主页
@app.route('/')
def index():
    return  "这是网站的主页"

# 基本路由   /login/---访问路径
# 视图函数   告诉app当用户访问/login/这个路径时， 执行login函数的内容， 最终将return的内容返回给客户端;
@app.route('/login/')
def login():
    return  '<h1 style="color:red">login......</h1>'


if __name__ == '__main__':
    # 运行Flask应用
    # 127.0.0.1----回环地址IP， 每台主机都有====localhost
    # 如何设置， 使得服务奇特主机的浏览器可以访问?  '0.0.0.0'开放所有的IP， 使得可以访问
    # 如何修改端口?  # 可能会报错:Address already in use
    app.run(host='0.0.0.0', port=8080)

