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




array = ["粉条", "粉丝", "粉带"]
s1 = pd.Series(data=array)
print(s1)


# 1). 修改Series索引
print(s1.index)
s1.index = ['A', 'B', 'C']
print(s1)


# 2). Series纵向拼接;
array = ["粉条", "粉丝", "粉带"]
# 如果不指定索引， 默认从0开始;
s2 = pd.Series(data=array)
s3 = s1.append(s2)
print(s3)

# 3). 删除指定索引对应的元素;
s3 = s3.drop('C')  # 删除索引为‘C’对应的值;
print(s3)


# 4). 根据指定的索引查找元素
print(s3['B'])
s3['B'] = np.nan
print(s3)


# 5). 切片操作  --- 同列表
print(s3[:2])
print(s3[::-1])
print(s3[-2:])  # 显示最后两个元素