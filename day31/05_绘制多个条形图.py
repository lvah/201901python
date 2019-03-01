"""
文件名: $NAME.py
日期: 22  
作者: lvah
联系: xc_guofan@qq.com
代码描述: 





"""

from pyecharts import Bar

x_movies_name = ["猩球崛起", "敦刻尔克", "蜘蛛侠", "战狼2"]
y_16 = [15746, 312, 4497, 319]
y_15 = [12357, 156, 2045, 168]
y_14 = [2358, 399, 2358, 362]

bar = Bar(title="某年内地电影票房前20的电影 matplotlib.font_manager.FontProperties ", subtitle="子标题")
bar.add("2017-09-14", x_movies_name, y_14, mark_line=['min', 'max'], mark_point=['average'])
bar.add("2017-09-15", x_movies_name, y_15)
bar.add("2017-09-16", x_movies_name, y_16)

bar.render()
