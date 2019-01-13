"""
# 什么时异常?
    在程序运行过程中影响程序正常运行的内容，


# 为什么需要异常处理?
    可以让你的程序更加健壮， 可以清晰的快速修复异常。





1). print(s)
NameError: name 's' is not defined

2). li = [1,2,3]
li[10]
IndexError: list index out of range


3). 10/0
ZeroDivisionError: division by zero

>>> d = dict(a=1, b=2)
>>> d
{'a': 1, 'b': 2}
>>> d['c']
Traceback (most recent call last):
  File "<input>", line 1, in <module>
KeyError: 'c'
4).d = dict(a=1, b=2)
d
{'a': 1, 'b': 2}
d['c']
KeyError: 'c'



5).

AttributeError: 'Student' object has no attribute 'scores'

"""

# print(s)
class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def echo(self):
        return  self.name

    def __str__(self):
        return  "Student(%s)" %(self.name)



s = Student('黎明', 30)
# print(s.scores)
# s.echo1()


# FileNotFoundError: [Errno 2] No such file or directory: '/tmp/aa'
with open('/tmp/aa') as f:
    print(f.read()[:10])




