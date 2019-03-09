"""
文件名: $NAME.py
日期: 09  
作者: lvah
联系: xc_guofan@qq.com
代码描述: 



# Flask程序的基本结构
    - 模块的安装   pip
    - 虚拟环境     (Anaconda, virtualenv )
    - 实现简单的web服务网站?
    - 路由
        - 普通路由设置
        - 动态路由   @app.route('/users/<id>/')
        - 设置可以接收的HTTP请求的类型  @app.route('/login/', methods=['GET', 'POST'])
    - 视图函数
    - 安全上下文: request
        - request.user_agent
        - request.remote_addr
        - request.args.get('id')
        - request.args.get('name')
        - request.args.get('name')
    - 获取用户表单提交的内容
        - GET请求: request.args.get('key')
        - POST请求: request.form.get('key')

    - 返回页面常用的方法
        - redirect
        - render_template

    - 自定义错误页面: 装饰器@app.errorhandler(错误的状态码) 404/500/200/300/403



# Flask的模板
    - Jinja变量{{ 变量名  | 过滤器 }}
    - 过滤器
        - 内置过滤器:
        - 自定义过滤器
    - 语法结构
        - for循环
        - if语句
        - 宏macro的操作
            - 如何定义宏?
            - 如何调用宏?
        - include包含操作
        - 模板的继承
            {% extends 'base.html' %}


# Flask-Bootstrap
    - 基模板
    - 快速制作表单的宏('bootstrap/wtf.html as wtf'  ---> wtf.quick_form(form))


# Flask-wtf
    -  Form类(FlaskForm)
    -  各种Field类(StringField, PasswordField, SubmitField)
    -  Validator类(DataRequired(), Equalto(), )




# Flask-sqlalchemy




"""





