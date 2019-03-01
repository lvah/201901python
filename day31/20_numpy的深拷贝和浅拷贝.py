"""
文件名: $NAME.py
日期: 22  
作者: lvah
联系: xc_guofan@qq.com
代码描述: 


# 列表的深拷贝和浅拷贝
    - 浅拷贝:  a= b[::]   a = copy.copy(b)
    - 深拷贝: a = copy.deepcopy(b)



- numpy中的拷贝
    - data1 = data: 完全不复制， 两个变量相互影响， 指向同一块内存空间；
    - data2 = data[::], 会创建新的对象data2，
        但是data的数据完全由data2保管， 两个的数据变化是一致的;
    - data3 = data.copy(), 深拷贝， 两个变量不湖影响;




import numpy as np
data = np.arange(8).reshape(2,4)
data
array([[0, 1, 2, 3],
       [4, 5, 6, 7]])
data1 = data
id(data)
140444611238448
id(data1)
140444611238448
data2 = data[::]
id(data)
140444611238448
id(data2)
140444621241360
id(data[0])
140444621241200
id(data2[0])
140444620515568
data
array([[0, 1, 2, 3],
       [4, 5, 6, 7]])
data2
array([[0, 1, 2, 3],
       [4, 5, 6, 7]])
np.where(data2<4,4,10)
array([[ 4,  4,  4,  4],
       [10, 10, 10, 10]])
data2
array([[0, 1, 2, 3],
       [4, 5, 6, 7]])
data2[0] = 0
data2
array([[0, 0, 0, 0],
       [4, 5, 6, 7]])
data
array([[0, 0, 0, 0],
       [4, 5, 6, 7]])
data3 = data.copy()
data
array([[0, 0, 0, 0],
       [4, 5, 6, 7]])
data3
array([[0, 0, 0, 0],
       [4, 5, 6, 7]])
data3[0] = 10
data3
array([[10, 10, 10, 10],
       [ 4,  5,  6,  7]])
data
array([[0, 0, 0, 0],
       [4, 5, 6, 7]])
"""
