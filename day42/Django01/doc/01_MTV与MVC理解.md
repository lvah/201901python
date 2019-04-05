# Django2.1文档地址
https://media.readthedocs.org/pdf/django/2.1.x/django.pdf

# MVC框架和MTV框架
- MVC，全名是Model View Controller，是软件工程中的一种软件架构模式，把软件系统分为三个基本部分：模型(Model)、视图(View)和控制器(Controller)，具有耦合性低、重用性高、生命周期成本低等优点。

- Django框架的设计模式借鉴了MVC框架的思想，也是分成三部分，来降低各个部分之间的耦合性。Django框架的不同之处在于它拆分的三部分为：Model（模型）、Template（模板）和View（视图），也就是MTV框架。


- 什么是MTV呢?
```
        Model(模型)：负责业务对象与数据库的对象(ORM)

        Template(模版)：负责如何把页面展示给用户

        View(视图)：负责业务逻辑，并在适当的时候调用Model和Template
```


此外，Django还有一个urls分发器，它的作用是将一个个URL的页面请求分发给不同的view处理，view再调用相应的Model和Template





# MVC

软件架构模式: 

    M : model---- 数据库模型
    V： view------视图函数
    C ： controller --- 控制器
    
优点: 
    耦合性低，重用性     
   
    
/login/
/logout/
/register/    


# MTV
M: model
T: template(负责把页面展示给用户)
V: view(负责业务逻辑， 在适当的时候调用Model或者Template)


# Django： MTV




```
- 客户端浏览器输入url地址: http://127.0.0.1:8000/
- 确认信息（4个）------ /
- / -----执行哪些逻辑代码



@app.route('/')
def index():
    return 'index‘
```