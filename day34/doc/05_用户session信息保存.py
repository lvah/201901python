"""
文件名: $NAME.py
日期: 28  
作者: lvah
联系: xc_guofan@qq.com
代码描述:



# cookie: 客户端浏览器的缓存;
# session: 服务端缓存;


#  1). **********session的作用是什么?

    Session 对象存储特定用户会话所需的属性及配置信息。这样，当用户在应用程序的 Web 页之间跳转时，
    存储在 Session 对象中的变量将不会丢失，而是在整个用户会话中一直存在下去。当用户请求来自应用程序的
    Web 页时，如果该用户还没有会话，则 Web 服务器将自动创建一个 Session 对象。当会话过期或被放弃后，
    服务器将终止该会话。Session 对象最常见的一个用法就是存储用户的首选项。



from flask import  Flask, session
import  random
app  = Flask(__name__)
app.config['SECRET_KEY'] =  random._urandom(24)
# 设置是24位的字符， 每次运行服务器的secret_key都是不同的，
# 服务器重启后会清除上一次存储的session信息值;


# 2). ******设置session值；
@app.route('/')
def index():
    # 如何设置session的key-value值
    session['name'] = 'westos'
    return "hello world"



@app.route('/get/')
def get():
    # 3). *********如何获取session?
    return  session.get('name')



@app.route('/delete/')
def delete():
    # 4). ************如何删除?
    print(session.get('name'))
    session.pop('name')
    print(session.get('name'))
    return  'delete'






"""





