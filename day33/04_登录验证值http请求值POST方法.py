"""
文件名: $NAME.py
日期: 26  
作者: lvah
联系: xc_guofan@qq.com
代码描述: 



"""
from flask import  Flask, request, render_template, redirect
app = Flask(__name__)


@app.route('/')
def index():
    return  "这是主页"


# 默认路由只支持get方法， 如何指定接受post方法?
@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # 难点: post请求提交的数据如何获取?
        print(request.form)
        username = request.form.get('username', None)

        password = request.form.get('password', None)
        # 如果用户名和密码正确， 跳转到主页;
        if username == 'root' and password == 'redhat':
            return  redirect('/')
        # 如果登录不正确， 则警告红色信息;还是在登录页面;
        else:
            # 可以给html传递变量
            return  render_template('login_post.html',
                                    errMessages="用户名或者密码错误"
                                    )
    else:
        return  render_template('login_post.html')


@app.errorhandler(404)
def page_not_found(e):
    return  render_template("404.html"), 404

@app.errorhandler(500)
def internal_server_error(e):
    return  render_template("500.html"), 500
if __name__ == '__main__':
    app.run()







