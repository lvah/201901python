"""


总结：
    1). Python内置的@property装饰器就是负责把一个方法变成属性调用的;
    2). @property本身又创建了另一个装饰器@state.setter，负责把一个
        setter方法变成属性赋值，于是，我们就拥有一个可控的属性操作.
    3). @property广泛应用在类的定义中，可以让调用者写出简短的代码，
        同时保证对参数进行必要的检查，这样，程序运行时就减少了出错的可能性。

源代码应用范例: 让属性只读：
    from datetime import  date

    # Read-only field accessors
    @property
    def year(self):
        # year (1-9999)
        return self._year

    @property
    def month(self):
        # month (1-12)
        return self._month

    @property
    def day(self):
        # day (1-31)
        return self._day

/home/kiosk/anaconda2/envs/2048/lib/python3.6/datetime.py

"""


from datetime import  date
from datetime import  time
import time


from colorFont import  *
class Book(object):
    def __init__(self, name, kind, state):
        self.name = name
        self.kind = kind
        # 0： 借出  1： "未借出"
        # 书的状态只能是0或者1， 如果是其他， 应该报错；
        # 查看书状态， 希望是汉字形式， 有实际意义的；
        self.__state  = 0

    @property   # 将这个方法转换为类的属性; print(book.state)
    def state(self):
        if self.__state == 0:
            return  ERRRED + "借出"
        elif self.__state == 1:
            return  OKGREEN + "未借出"

    @state.setter  # book.state = 0
    def state(self, value):
        if value in (0,1):
            # 更新书状态
            self.__state = value
        else:
            print(ERRRED + "更新错误， 必须是0或者1")

    @state.deleter  # del book.state
    def state(self):
        del self.__state
        print(OKGREEN + "删除书状态成功!")

if __name__ == "__main__":
    # book = Book("python核心编程", 'python', 1)
    # # book.set_state(3)  # book.state = 3
    # # print(book.get_state())  # print(book.state)
    # book.state = 0
    # print(book.state)
    # del book.state


    d = date(2019, 10, 10)
    print(d.year)
    print(d.month)
    print(d.day)


    # d.year = 2020     # 此处不成功， year是只读的
    # del d.year        # 此处不成功， year是只读的
    print(d.year)



