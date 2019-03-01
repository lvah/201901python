"""
文件名: $NAME.py
日期: 22  
作者: lvah
联系: xc_guofan@qq.com
代码描述: 



"""
import random

from pyecharts import Line


# 图表的x轴的数据, 是一个可迭代的数据类型
x_times = list(range(0,30))
# 图表的y轴的数据, 是一个可迭代的数据类型
y_temp_3 = [random.randint(20, 35) for i in range(30)]
y_temp_10 = [random.randint(20, 35) for j in range(30)]


line  = Line("折线图")
#
# line.add("", x_times, y_temp_3, mark_line=['max'], mark_point=['min'])
# line.add("", x_times, y_temp_10, mark_line=['max'], mark_point=['min'])

# # 折线图---阶梯图
# line.add("", x_times, y_temp_3, mark_line=['max'], mark_point=['min'], is_step=True)
# line.add("", x_times, y_temp_10, mark_line=['max'], mark_point=['min'], is_step=True)


# pip install echarts-countries-pypkg
# pip install echarts-china-provinces-pypkg
# pip install echarts-china-cities-pypkg
# pip install echarts-china-counties-pypkg
# # # 折线图---面积图
# 设置透明度
line.add("", x_times, y_temp_3,  is_fill=True, area_color='red', area_opacity=0.3)
line.add("", x_times, y_temp_10,  is_fill=True, area_color='green', area_opacity=0.2)

line.render()