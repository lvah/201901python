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

# # 取第一行的数据
# data[0] = 0
# print(data)
#
# # 获取多行列
# data.T[:2] = 0
# print(data)


# # 布尔索引: 复杂的条件: data中所有大于8的数字都替换为0；
# # 返回一个三行四列的数组， 存储的是Bool值
# print(data>8)
# data[data>8] = 0
# print(data)


# 复杂的条件: data中所有大于8的数字都替换为0， 否则替换为1； a>b?a:b
# print(data)
# data[data<=8] = 1
# data[data>8] = 0
# print(data)
print(np.where(data <= 8, 1, 0))

# 裁剪: 如果data<=8, 替换称8， 如果data>=10, 替换为10;
print(data)
print(data.clip(8, 10))

# ************************************************
# 数组的拼接
t1 = np.arange(12).reshape(2, 6)
t2 = np.arange(12).reshape(2, 6)
t3 = np.arange(12).reshape(2, 6)

# 竖直拼接(vertically)
print(np.vstack((t1, t2, t3)))
# 水平拼接(horizontally)
print(np.hstack((t1, t2, t3)))

# *************************************************
# 数组的行列交换
t4 = np.arange(12).reshape(2, 6)
# 行交换（第一行和第二行进行交换）
print("原数据:\n", t4)
t4[[0, 1], :] = t4[[1, 0], :]
print("替换后的数据:\n", t4)

# 列交换（第3列和第5列进行交换）
print("原数据:\n", t4)
t4[:, [2, 4]] = t4[:, [4, 2]]
print("替换后的数据:\n", t4)
