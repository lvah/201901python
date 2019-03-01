"""
文件名: $NAME.py
日期: 26  
作者: lvah
联系: xc_guofan@qq.com
代码描述: 

访问的网址如下:
    # http://www.douban.org/123457677/comments/
    # http://www.douban.org/123457673/comments/
    # http://www.douban.org/123457674/comments/
    # http://www.douban.org/123457675/comments/



动态路由:
    http://www.douban.org/<>/comments/
"""

# request叫做请求上下文
from flask import  Flask, request
app = Flask(__name__)

# 常用动态路由的规则:
#     1). url路由的一部分可以标记为变量, <变量名>;
#     2):. flask中路由变量可以指定的类型: int, string, float, uuid
@app.route("/<int:id>/comments/")
def comments(id):
    return "这是一个%s评论页面" %(id)


# 字符穿
@app.route("/welcome/<string:username>/")
def welcome(username):
    return  "<h1>欢迎用户%s登陆网站</h1>" %(username)




# *****************
#  重点request：
#       Flask 从客户端收到请求时,要让视图函数能访问一些对象,这样才能处理请求。
#       请求对象就是一个很好的例子,它封装了客户端发送的 HTTP 请求。即request；
# 解决问题:
#       特殊的URL地址: http://www.baidu.com/query?id=123&name=westos
# http://127.0.0.1:5000/login2/?username=westos&password=westos
@app.route('/query')
def query():
    # 获取客户端的用户代理;
    user_agent = request.user_agent
    # 获取客户端的IP地址;
    req_addr = request.remote_addr
    # 获取用户请求url地址里面key值对应的value值;
    id = request.args.get('id')
    name = request.args.get('name')

    # 查看客户端的HTTP请求方式;
    reqMethod = request.method

    # 将字符串信息返回给客户端浏览器/其他, 默认以html方式显示， 如果需要换行， 加html的标签<br/>;
    return  """
    请求的用户代理: %s  <br/>
    请求的客户端Ip： %s  <br/>
    请求的id号: %s   <br/>
    用户名: %s  <br/>
    请求方式: %s
    """ %(user_agent, req_addr, id, name, reqMethod)

if __name__ == '__main__':
    app.run()








