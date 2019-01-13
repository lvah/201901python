"""

Python中至少有三种比较常见的方法类型，即实例方法，类方法、静态方法。它们是如何定义的呢？
如何调用的呢？它们又有何区别和作用呢？

首先，这三种方法都定义在类中。
实例方法
    定义：第一个参数必须是实例对象，该参数名一般约定为“self”，通过它来传递实例的属性和方法（也可以传类的属性和方法）；
    调用：只能由实例对象调用。

类方法
    定义：使用装饰器@classmethod。第一个参数必须是当前类对象，该参数名一般约定为“cls”，
         通过它来传递类的属性和方法（不能传实例的属性和方法）；
    调用：实例对象和类对象都可以调用。

静态方法
    定义：使用装饰器@staticmethod。参数随意，没有“self”和“cls”参数，但是方法体中不能使用类或实例的任何属性和方法；
    调用：实例对象和类对象都可以调用。




# 源代码:
    @classmethod
    def today(cls):
        "Construct a date from time.time()."
        t = _time.time()
        return cls.fromtimestamp(t)

    @classmethod
    def fromordinal(cls, n):
        y, m, d = _ord2ymd(n)
        return cls(y, m, d)




"""



from datetime import  date
class Date(object):
    def __init__(self, year, month, day):
        self.__year = year
        self.__month = month
        self.__day = day

    # 实例方法,
    def echo(self):
        print("%s %s %s" % (self.__year, self.__month, self.__day))

    # 默认情况下， 需要将所有相关日期的操作封装到Date类中；
    # 如果不做任何改变， s实质上时实例化的对象本身， 不是我们想要的字符串；
    @classmethod  # 类方法
    def as_string(cls, s):  # "2019-10-10"
        year, month, day = s.split('-')
        return  cls(year, month, day)  # cls实质上就是Date


    @staticmethod
    def is_valid(s):
        year, month, day = map(int, s.split('-'))
        return year > 0 and 0 < month <= 12 and 1 <= day <= 31


if __name__ == "__main__":
    # 实例化日期类
    d = Date(2019, 10, 2)
    s = "2019-10-10"
    # Date.as_string(s).echo()
    print(Date.is_valid(s))




