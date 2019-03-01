"""
文件名: $NAME.py
日期: 22  
作者: lvah
联系: xc_guofan@qq.com
代码描述: 



"""


from pyecharts import Map

import numpy as np

value = [155, 10, 66, 78, 33, 80, 190, 53, 49.6]
attr = [
    "福建", "山东", "北京", "上海", "甘肃", "新疆", "河南", "广西", "西藏"
    ]

#  background_color="#404a59"
map = Map("Map 结合 VisualMap 示例", width=1200, height=600, )
map.add(
    "",
    attr,
    value,
    maptype="china",
    is_visualmap=True,
    visual_text_color="#000",
)
map.render()