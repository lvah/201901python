"""
文件名: $NAME.py
日期: 01  
作者: lvah
联系: xc_guofan@qq.com
代码描述: 

flask-wtf
    - 避免重复操作， 表单操作很多;
    - 防止表单遭遇跨站请求伪造(csrf===cross-site request forgery);


1. 为什么使用Flask-WTF？
    request对象公开了所有客户端发送的请求信息。特别是request.form可以访问POST请求提交的表单数据。
    尽管Flask的request对象提供的支持足以处理web表单，但依然有许多任务会变得单调且重复。
    表单的HTML代码生成和验证提交的表单数据就是两个很好的例子。
优势：
    Flask-WTF扩展使得处理web表单能获得更愉快的体验。该扩展是一个封装了与框架无关的WTForms包的Flask集成。


2. 什么是表单处理?

    在网页中，为了和用户进行信息交互总是不得不出现一些表单。
    flask设计了WTForm表单库来使flask可以更加简便地管理操作表单数据。
    WTForm中最重要的几个概念如下：

    1). Form类，开发者自定义的表单必须继承自Form类或者其子类。
    Form类最主要的功能是通过其所包含的Field类提供对表单内数据的快捷访问方式。

　　2). 各种Field类，即字段。一般而言每个Field类都对应一个input的HTML标签。
    比如WTForm自带的一些Field类比如BooleanField就对应<input type="checkbox">，
    SubmitField就对应<input type="submit">等等。

　　3). Validator类。这个类用于验证用户输入的数据的合法性。
    比如Length验证器可以用于验证输入数据的长度，
    FileAllowed验证上传文件的类型等等。

　　另外，flask为了防范csfr(cross-site request forgery)攻击，
   默认在使用flask-wtf之前要求app一定要设置过secret_key。
   最简单地可以通过app.config['SECRET_KEY'] = 'xxxx'来配置。



3. 常见的Field类

　　PasswordField　　   密码字段，自动将输入转化为小黑点
　　DateField　　       文本字段，格式要求为datetime.date一样
　　IntergerField　　   文本字段，格式要求是整数
　　DecimalField　　    文本字段，格式要求和decimal.Decimal一样
　　FloatField　　      文本字段，值是浮点数
　　BooleanField　　    复选框，值为True或者False
　　RadioField　　      一组单选框
　　SelectField　　     下拉列表，需要注意一下的是choices参数确定了下拉选项，
                       但是和HTML中的<select> 标签一样，其是一个tuple组成的列表，
                       可以认为每个tuple的第一项是选项的真正的值，而第二项是alias。
　　MultipleSelectField　　可选多个值的下拉列表





Validator是验证函数:
    Validator是验证函数，把一个字段绑定某个验证函数之后，flask会在接收表单中的数据之前对数据做一个验证，
    如果验证成功才会接收数据。验证函数Validator如下，具体的validator可能需要的参数不太一样，这里只给出
    一些常用的，更多详细的用法可以参见wtforms/validators.py文件的源码，参看每一个validator类需要哪些参数：

　　*基本上每一个validator都有message参数，指出当输入数据不符合validator要求时显示什么信息。

　　Email　　
            验证电子邮件地址的合法性，要求正则模式是^.+@([^.@][^@]+)$
　　EqualTo　　
            比较两个字段的值，通常用于输入两次密码等场景，可写参数fieldname，
            不过注意其是一个字符串变量，指向同表单中的另一个字段的字段名
　　IPAddress　　
            验证IPv4地址，参数默认ipv4=True,ipv6=False。如果想要验证ipv6可以
            设置这两个参数反过来。
　　Length　　
            验证输入的字符串的长度，可以有min,max两个参数指出要设置的长度下限和上限,
            注意参数类型是字符串，不是INT!!
　　NumberRange　　
            验证输入数字是否在范围内，可以有min和max两个参数指出数字上限下限，注意参数
            类型是字符串，不是I数里可以设置%(min)s和%(max)s两个格式化部分，来告诉前端
            这个范围到底是多少。其他validator也有这种类似的小技巧，可以参看源码。
　　Optional　　
            无输入值时跳过同字段的其他验证函数
　　Required　　
            必填字段
　　Regexp　　
            用正则表达式验证值，参数regex='正则模式'
　　URL　　
            验证URL，要求正则模式是^[a-z]+://(?P<host>[^/:]+)(?P<port>:[0-9]+)?
            (?P<path>\/.*)?$
　　AnyOf　　
            确保值在可选值列表中。
　　NoneOf　　
            确保值不在可选值列表中




# flask-wtf的使用流程
    # 1). 编写forms.py文件， 定义一个关于表单的类;(***注意： 一定要有提交的按钮);
    # 2). 业务逻辑文件app.py中，
            - 实例化表单类;  form = RegisterForm()
            - 验证表单内容是否提交成功?   form.validate_on_submit():
            - 获取表单里面的内容(两种方法):
                - 通过request对象获取: request.form['key值']；
                - 通过form对象获取: form.key值.data

    # 3). 表现逻辑文件wtf.html中:
            - 导入wtf模块: {% import "bootstrap/wtf.html" as wtf %}
            - 自动生成表单对应的html：  {{ wtf.quick_form(form) }}



"""





