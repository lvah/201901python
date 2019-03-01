"""
文件名: $NAME.py
日期: 22  
作者: lvah
联系: xc_guofan@qq.com
代码描述: 




CSV(逗号分隔符文件),广义的csv文件可以不是逗号分隔；
显示: 以Excel表格的方式打开;


"""

import numpy as np

fname = "doc/eg6-a-student-data.txt"
dtype = np.dtype([('gender', '|S1'), ('height', 'f2')])
# fname： 文件的名称， 可以是文件名， 也可以是ugz或者bz2的压缩文件;
# dtype： 数据类型， 可选， 默认是float;
# delimiter： 分隔符字符串， 默认情况是任何的空格，
# skiprows: 跳过前xx行， 一般情况跳过第一行;
#  usecols: 读取指定的列， 可以是元组；
# unpack： 如果为True， 对返回的数组对象转置；
data = np.loadtxt(fname=fname, dtype=dtype, skiprows=9, usecols=(1, 3), unpack=True)
print(data)
