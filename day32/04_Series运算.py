"""
文件名: $NAME.py
日期: 25  
作者: lvah
联系: xc_guofan@qq.com
代码描述: 


"""
import pandas as pd
import numpy as np
import  string

s1  = pd.Series(np.arange(5), index=list(string.ascii_lowercase[:5]))
s2  = pd.Series(np.arange(2, 8), index=list(string.ascii_lowercase[2:8]))

print(s1)
print(s2)

# *****************8按照对应的索引进行计算， 如果索引不同，则填充为Nan;


# 加法
print(s1 + s2)
print(s1.add(s2))


# -
print(s1 - s2)
print(s1.sub(s2))


# *
print(s1 * s2)
print(s1.mul(s2))


# /
print(s1 / s2)
print(s1.div(s2))



# 求中位数
print(s1)
print(s1.median())


# 求和
print(s1.sum())


# max
print(s1.max())

# min
print(s1.min())

