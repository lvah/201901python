"""
文件名: $NAME.py
日期: 25  
作者: lvah
联系: xc_guofan@qq.com
代码描述: 


# 绘制电影时长和电影排名之间的关系
"""

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


filename = 'doc/special_top250.csv'
data = pd.read_csv(filename)
print(data.head())
# 获取电影时长
x_series = data.movie_duration
# 获取电影排名
y_series = data.num




from pyecharts import  Scatter
scatter = Scatter("散点图")
scatter.add("", x_series, y_series)
scatter.render()







