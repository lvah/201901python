"""
文件名: $NAME.py
日期: 22  
作者: lvah
联系: xc_guofan@qq.com
代码描述: 



"""

#  Funnel
from pyecharts import Funnel

x_movies_name = ["猩球崛起", "敦刻尔克", "蜘蛛侠", "战狼2"]
y_16 = [20, 40, 60, 80]
funnel = Funnel("xxxx")
funnel.add("电影信息", x_movies_name, y_16)
funnel.render()



