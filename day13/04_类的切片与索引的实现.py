"""
int, float, str,

list: 特性:(增删改查, 索引， 切片， 重复， 循环<迭代>， 连接)
dict,
tuple,
set




# 1. python里面一切皆对象；
# 2. 如何给自己编写的类实现切片和索引的功能?
# 3. 实现索引的几个魔术方法?

 def __getitem__(self, y): # real signature unknown; restored from __doc__
        # x.__getitem__(y) <==> x[y]
        pass



li[0]
"""

class Student(object):
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores

    # 索引的是学生的成绩
    def __getitem__(self, index):  # 1).索引值的获取
        print(index, type(index))
        return self.scores[index]


    def __setitem__(self, key, value): # 2). 索引值的重新赋值
        self.scores[key] = value


    def __delitem__(self, key):  # 3). 删除索引值
        del  self.scores[key]



    def __mul__(self, other):  # 4). 实现*的效果， 具体返回什么取决于代码的业务需求
        """对于学生的每一门成绩乘3"""
        return  [i*other for i in self.scores]


    def __add__(self, other):  # 5). 连接的时候必须是同一种数据；类型
        # 将两个学生的成绩拼接起来
        return  self.scores + other.scores

    def __contains__(self, item): # 6). 判断某个元素是否存在于这个对象中?
        return  item in self.scores


    def __iter__(self):   # 7). 迭代， 使得该对象可以实现for循环
        # 将列表转换为迭代的类型， 可以for循环, 一定要返回iter类型的数据；
        return  iter(self.scores)

    def __lt__(self, other):  # 8). 比较两个对象的大小；
        return  (sum(self.scores)/3) < (sum(other.scores)/3)


liming = Student('liming', [100, 89, 100])

# # 1).索引值的获取
# print(liming[0])
# print(liming[1])
# print(liming[2])
#
# # 2).索引值的重新赋值
# liming[0] = 90
# print(liming[0])
#
# # 3). 删除索引值
# del liming[0]
# # print(liming[:2])
#


# # 1).切片值的获取
# print(liming[:2])
# print(liming[-2:])
#
#
# # 2).切片值的重新赋值
# liming[:2] = [10, 10]
# print(liming.scores)
#
# # 3). 删除切片值
# del liming[:2]
# print(liming.scores)

#
# # 4). 判断是否可以重复？
# print(liming * 3)
#
# # 5). 连接？
xiaohong = Student('小红', [100, 90, 90])
# print(xiaohong + liming)
#
#
#
# # 6). 成员操作符? 判断是否在对象里面存在?
# print(100 in xiaohong)
# print(101 in xiaohong)
# print(101 not in xiaohong)
#
#


# # 7). 实现for循环?
# for item in liming:
#     print(item)


# 8). 比较对象的大小？
# print(liming >  xiaohong)
print(liming <  xiaohong)
