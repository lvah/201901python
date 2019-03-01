"""
文件名: $NAME.py
日期: 26  
作者: lvah
联系: xc_guofan@qq.com
代码描述: 




HTTP请求的方法:
    GET:
        1). 获取页面信息;
        2). 可以提交数据信息;但是数据不安全;
        http://127.0.0.1:5000/login2/?username=westos&password=westos
    POST:
        提交服务端需要的请求信息；有利于数据的安全性;

    PUT：

    DELETE：

"""

from flask import Flask, render_template, request, redirect

app = Flask(__name__)
@app.route('/')
def index():
    return  "<h1>主页</h1>"

@app.route('/login/')
def login():
    # 一般情况， 不会直接把html文件内容直接返回；
    # 而是将html文件保存到当前的templates目录中；
    #       1). 通过render_template方法调用;
    #       2). 默认情况下,Flask 在程序文件夹中的 templates 子文件夹中寻找模板。
    return  render_template('login.html')


@app.route('/login2/')
def login2():
    # 获取用户输入的用户名
    username = request.args.get('username', None)
    password = request.args.get('password', None)
    # 逻辑处理， 用来判断用户和密码是否正确;
    if username == 'root' and password == 'redhat':
        # 重定向到指定路由；
        return  redirect('/')
        # return "登录成功"
    else:
        return  "登录失败"

if __name__ == '__main__':
    app.run()
