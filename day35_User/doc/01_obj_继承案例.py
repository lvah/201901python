"""
文件名: $NAME.py
日期: 01  
作者: lvah
联系: xc_guofan@qq.com
代码描述: 



"""



class Animal(object):
    def __init__(self, name):
        self.name = name
             
    def eat(self):
        
        print("%s正在吃。。。。。。" %(self.name))




class Cat(Animal):
    # 1. 猫有两个属性， name， age
    def __init__(self, name, age):
        # 执行父类的构造方法;
        super(Cat, self).__init__(name)
        self.age = age


    # 2. 猫在chi的时候， 显示两次, 
    # "%s正在吃。。。。。。"
    # "%s正在吃鱼。。。。。。"
    def eat(self):
        super(Cat, self).eat()
        print("%s正在吃鱼。。。。。。" %(self.name))



cat = Cat("粉条", 5)
cat.eat()