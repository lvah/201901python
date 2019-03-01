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


# 1).
print(data.transpose())

# 2). 0轴 ， 1 轴
print(data.swapaxes(1, 0))

# 3).
print(data.T)