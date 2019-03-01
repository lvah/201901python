"""
文件名: $NAME.py
日期: 22  
作者: lvah
联系: xc_guofan@qq.com
代码描述: 


Numpy：
    - 什么numpy？
    - numpy基础概念
    - numpy常用的方法
    - numpy常用的统计方法

- 什么numpy？
    快速， 方便的科学计算基础库(主要时数值的计算， 多维数组的运算);




- 轴的理解(axis): 0轴， 1轴， 2轴
    - 一维数组: [1,2,3,45]    ----0轴
    - 二维数组: [[1,2,3,45], [1,2,3,45]]     ----0轴, 1轴，


"""

import numpy as np


# 1. numpy中如何创建数组(矩阵)?
# 方法1：
a = np.array([1,2,3,4,5])
b = np.array([1,2,3,4,5])
c1 = np.array(range(1,6))
print(a+b)



# 方法2：
c2 = np.arange(1,6)
print(c1)
print(c2)


# 数组的类名: numpy.ndarray
print(type(c1))

# 查看数据元素的类型
print(c1.dtype)

# 2. 修改数组的数据类型
print(c1.astype('float'))
print(c1.astype('bool'))
print(c1.astype('?'))  # ?是bool类型的代号;

# 创建的时候指定数据类型
print(np.array([1,2,3,4], dtype=np.float))


# 3. 修改浮点数的小数位数
c3 = np.array([1.234556, 3.45464456, 5.645657567])
print(np.round(c3, 2))
