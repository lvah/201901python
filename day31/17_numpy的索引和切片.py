"""
文件名: $NAME.py
日期: 22  
作者: lvah
联系: xc_guofan@qq.com
代码描述: 



"""


import numpy as np

# 将一维数组转换为3行4列的二维数组
data = np.arange(12).reshape((3, 4))
print(data)

# 取第一行的数据
print(data[0])

#  取第一列的数据
print(data.T[0])
print(data[:, 1])

# 获取多行
print(data[:2])

# 获取多行列
print(data.T[:2])
print(data[:, :2])


# 获取指定行的前几列;
print(data)
print(data[[0,2], :2])
print(data[:2, [0,2]])


