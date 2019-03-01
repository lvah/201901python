"""
文件名: $NAME.py
日期: 22  
作者: lvah
联系: xc_guofan@qq.com
代码描述: 


- 求和
- 均值
- 中值
- 最大值
- 最小值
- 极差
- 标准差： 代表的是数据的波动稳定情况， 数字越大， 越不稳定;

"""


import numpy as np
data = np.arange(12, dtype=np.float).reshape(3, 4)
print(data.sum())
# 每一列数据的和；
print(data.sum(axis=0))
# 每一行数据的和；
print(data.sum(axis=1))

# - 均值
print(data.mean())
print(data.mean(axis=0))
print(data.mean(axis=1))

# - 中值
print(data)
print(np.median(data))
print(np.median(data, axis=0))
print(np.median(data, axis=1))

# - 最大值
print(data.max())
print(data.max(axis=0))
print(data.max(axis=1))

# - 最小值
# - 极差
print(np.ptp(data))
print(np.ptp(data, axis=0))
print(np.ptp(data, axis=1))


# - 标准差： 代表的是数据的波动稳定情况， 数字越大， 越不稳定;
print(data.std())
print(data.std(axis=0))
print(data.std(axis=1))
