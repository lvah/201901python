"""
文件名: .py
创建时间: 2019-01-15 15:
作者: lvah
联系方式: 976131979@qq.com
代码描述:


# namedtuple的需求：

t = ("kiosk", 'pts/0', 'localhost')

info = {'kiosk' : {
            'name': "kiosk",
            'node': 'localhost'
}}
因为元组的局限性：不能为元组内部的数据进行命名，所以往往我们并不知道一个元组所要表达的意义，
所以在这里引入了 collections.namedtuple 这个工厂函数，来构造一个带字段名的元组。
具名元组的实例和普通元组消耗的内存一样多，因为字段名都被存在对应的类里面。这个类跟普通的对象
实例比起来也要小一些，因为 Python 不会用 __dict__ 来存放这些实例的属性。


# 如何实现
def namedtuple(typename, field_names, *, verbose=False, rename=False, module=None):
    - typename: 元组名称
    - field_names : 元组中元素的名称
    - rename: 如果元素名称中包含python关键字， 必须设置rename=True




"""

# 1. 判断是否可迭代?
import random
from collections import Iterable
print(isinstance('hello', Iterable))


# 2. 字典key值次数统计
from collections import  Counter
# 跟踪某个key值出现的次数, 是一个无序的容器 类型.
ips = ['172.25.254.%s' %(random.randint(1, 25)) for ip in range(1000)]
c = Counter(ips)
print(c.most_common())
print(c.most_common(3))

# 3. 命名元组
from collections import  namedtuple
User = namedtuple("User", ['name', 'age', 'scores'])
u = User('fentiao', 10, 100)
print(u)
print(u.name)
print(u.age)
print(u.scores)


