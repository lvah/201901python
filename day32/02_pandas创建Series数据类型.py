"""
文件名: $NAME.py
日期: 25  
作者: lvah
联系: xc_guofan@qq.com
代码描述: 



常见的数据类型:
    - 一维: Series
    - 二维: DataFrame
    - 三维: Panel  ....
    - 四维: Panel4D  .....
    - N维: PanelND  ....

"""

import pandas as pd
import numpy as np
import  string


# 查看pandas版本信息
print(pd.__version__)

# ********************创建Series对象

#  1). 通过列表创建Series对象
array = ["粉条", "粉丝", "粉带"]
# 如果不指定索引， 默认从0开始;
s1 = pd.Series(data=array)
print(s1)
# 如果不指定索引， 默认从0开始;
ss1 = pd.Series(data=array, index=['A', 'B', 'C'])
print(ss1)

# 2). 通过numpy的对象Ndarray创建Series；
n = np.random.randn(5)   # 随机创建一个ndarray对象;
s2 = pd.Series(data=n)
print(s2)
# 修改元素的数据类型;
ss2 = s2.astype(np.int)
print(ss2)

# 3). 通过字典创建Series对象;
dict = {string.ascii_lowercase[i]:i for i in range(10)}
s3 = pd.Series(dict)
print(s3)