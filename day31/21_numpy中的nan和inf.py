"""
文件名: $NAME.py
日期: 22  
作者: lvah
联系: xc_guofan@qq.com
代码描述: 

nan(not a number): 表示不是一个数字, 代表的是数据缺失
inf(infinity): inf代表正无穷， -inf代表负无穷


# nan的特殊属性:
    - 两个nan的值是不相等的, 是float类型:
    >>> np.nan == np.nan
    False

    >>> np.nan != np.nan
    True

    - 如何判断有多少个缺失值:

        data = np.arange(12, dtype=np.float).reshape(3, 4)
        data
        array([[ 0.,  1.,  2.,  3.],
               [ 4.,  5.,  6.,  7.],
               [ 8.,  9., 10., 11.]])
        data[:2, 2] = np.nan
        data
        array([[ 0.,  1., nan,  3.],
               [ 4.,  5., nan,  7.],
               [ 8.,  9., 10., 11.]])
        np.count_nonzero(data!=data)
        2
        data!=data
        array([[False, False,  True, False],
               [False, False,  True, False],
               [False, False, False, False]])

        # 判断data里面的缺失值
        np.isnan(data)
        array([[False, False,  True, False],
               [False, False,  True, False],
               [False, False, False, False]])

        np.count_nonzero(np.isnan(data))
        2

    	data[np.isnan(data)]=0


"""




import numpy as np

print(np.nan)
print(np.inf)
print(-np.inf)
