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
data[0, 0] = 80
print(data)

# 1. 获取最大值和最小值的位置;
# 获取当前数组里面最大值的索引;
max_item1 = np.argmax(data)
print(max_item1)

# 获取每一列的最大值对应的索引;
print(np.argmax(data, axis=0))
# 获取每一行的最大值对应的索引;
print(np.argmax(data, axis=1))

# 2. 创建一个全为0的数组;
print(np.zeros((3, 3), dtype=np.int))

# 3. 创建一个全为1的数组;
print(np.ones((3, 4)))

# 4. 创建一个对角线全为1的正方形数组（方阵）
print(np.eye(3))
