"""
文件名: $NAME.py
日期: 22  
作者: lvah
联系: xc_guofan@qq.com
代码描述: 

list ====== 特殊的数组
数组和列表的区别:
    - 数组: 存储的时同一种数据类型;
    - list:容器， 可以存储任意数据类型;

"""

# 一维数组和数组的计算
a = [1, 2, 3, 4]
b = [2, 3, 4, 5]
add = lambda x: x[0] + x[1]
# [(1,2), (2,3), (3,4), (4,5)]
print([add(item) for item in zip(a, b)])

mul = lambda x: x[0] * x[1]
# [(1,2), (2,3), (3,4), (4,5)]
print([mul(item) for item in zip(a, b)])

# 二维数组和数组的计算

c = [[1, 2, 3, 4],
     [1, 2, 3, 4]]
d = [[2, 3, 4, 5],
     [2, 3, 4, 5]]
#
# print(c*d)
# print(c+d)

