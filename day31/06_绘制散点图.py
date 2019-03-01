"""
文件名: $NAME.py
日期: 22  
作者: lvah
联系: xc_guofan@qq.com
代码描述: 



"""

from pyecharts import EffectScatter, Scatter, Scatter3D

x_march = list(range(1, 32))
y_temp_march = [11, 17, 16, 11, 12, 11, 12, 6, 6, 7, 8, 9, 12, 15, 14, 17, 18, 21, 16, 17, 20, 14, 15, 15, 15, 19, 21,
                22, 22, 22, 23]


# scatter= EffectScatter("北京3月份每天白天的最高气温随时间(天)变化的散点图")
scatter= Scatter("北京3月份白天变化的散点图", subtitle="xxxx")
# symbol_size散点图标记的大小;
scatter.add("3 月", x_march, y_temp_march, symbol_size=10, line_color='red')
scatter.add("4 月", x_march, y_temp_march, symbol_size=30)
scatter.render()


