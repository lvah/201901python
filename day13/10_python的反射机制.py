"""
# 反射机制: 让对象告诉我们它的相关信息(对象拥有的属性和方法， 对象所属的类， 这个类是否有某个属性或者方法等等)
"""





# 1). 对象拥有的属性和方法
li = [1,2,3,4]
print(dir(li))
print(help(li.index))


import random
class Turtle(object):
    """
    乌龟类
    """
    # 构造函数什么时候执行? =---=====创建对象时执行
    def __init__(self):  # self指的是实例化的对象；
        # 乌龟的属性: x,y轴坐标和体力值
        # 乌龟的x轴， 范围1，10

        self.x = random.randint(1, 10)
        self.y = random.randint(1, 10)
        # 乌龟初始化体力为100
        self.power = 100

    # 类的方法:
    def move(self):
        # 乌龟的最大移动能力为2,[-2, -1, 0, 1, 2]
        move_skill = [-2, -1, 0, 1, 2]
        # 计算出乌龟的新坐标(10, 12)
        new_x = self.x + random.choice(move_skill)
        new_y = self.y + random.choice(move_skill)

        # 对于新坐标进行检验， 是哦否合法， 如果不合法， 进行处理
        self.x = self.is_vaild(new_x)
        self.y = self.is_vaild(new_y)

        # 乌龟每移动一次，体力消耗1
        self.power -= 1

    def is_vaild(self, value):
        """
        判断传进来的x轴坐标或者y轴坐标是否合法?

        1). 如果合法， 直接返回传进来的值；
        2). value<=0;  =====> abs(value);
        3). value > 10 ======> 10-(value-10);

        :param value:
        :return:
        """
        if 1 <= value <= 10:
            return value
        elif value < 1:
            return abs(value)
        else:
            return 10 - (value - 10)

    def eat(self):
        """
        当乌龟和鱼坐标重叠，乌龟吃掉鱼，乌龟体力增加20
        :return:
        """
        self.power += 20
turtle = Turtle()
print(dir(turtle))

# 2. 判断对象所属的类?
a = [1,2,3,4]
print(type(a))
print(type(turtle))

from datetime import  date
d = date(2018, 1,1)
print(type(d))

print(isinstance(1, str))
print(isinstance(turtle, Turtle))


# 3. 根据魔术方法来获取
print(turtle.__class__)
print(turtle.__dict__)
print(turtle.__doc__)


# 4. hasattr， getattr, setattr, delattr

print(hasattr(turtle, 'x'))
print(hasattr(turtle, 'x1'))
print(getattr(turtle, 'x'))
# print(getattr(turtle, 'x1'))

setattr(turtle, 'x', '100')
print(getattr(turtle, 'x'))
delattr(turtle, 'x')
print(hasattr(turtle, 'x'))