"""
文件名: $NAME.py
日期: 25  
作者: lvah
联系: xc_guofan@qq.com
代码描述: 



"""



import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


narr = np.arange(8).reshape(2, 4)
# DataFRame对象里面包含两个索引， 行索引(0轴， axis=0)， 列索引(1轴， axis=1)
d2 = pd.DataFrame(data=narr, index=['A', 'B'], columns=['views', 'loves', 'comments', 'tranfers'])
print(d2)



# **********************1). 查看基础属性***********************
print(d2.shape)  # 获取行数和列数;
print(d2.dtypes)  # 列数据类型
print(d2.ndim)  # 获取数据的维度
print(d2.index) # 行索引
print(d2.columns) # 列索引
print(d2.values, type(d2.values))   # 对象的值， 二维ndarray数组;



# ******************************2). 数据整体状况的查询*************
print(d2.head(1))  # 显示头部的几行， 默认5行
print(d2.tail(1))  # 显示头部的尾行， 默认5行

print("*"*10)
# 相关信息的预览： 行数， 列数， 列类型， 内存占用
print("info:", d2.info())

print("统计".center(50, '*'))
# 快速综合用计结果： 计数， 均值， 标准差， 最小值， 1/4位数， 中位数， 3/4位数， 最大值;
print(d2.describe())


# 3). 转置操作
print(d2.T)

# 4). 按列进行排序
print(d2)
# 按照指定列进行排序， 默认是升序， 如果需要降序显示，设置ascending=False;
print(d2.sort_values(by="views", ascending=False))


# 5). 切片及查询
print(d2[:1])   # 可以实现切片， 但是不能索引;
print('1:\n', d2['views'])   # 通过标签查询， 获取单列信息
print('2:\n', d2.views)   # 和上面是等价的;
print(d2[['views', 'comments']])  # 通过标签查询多列信息



# 6). 通过类似索引的方式查询;
#       - iloc(通过位置进行行数据的获取),
#        - loc(t通过标签索引行数据)
# print(d2[0])
print(d2)
print(d2.iloc[0])
print(d2.iloc[-1:])


# print(d2['A'])    # 报错
print(d2)
print(d2.loc['A'])



# 7). 更改pandas的值；
d2.loc['A'] = np.nan
print(d2)

# print(d2.info())
