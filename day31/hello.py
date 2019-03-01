from pyecharts import Map
value =[155, 10, 66, 78, 33, 80, 190, 53, 49.6]
attr =["福建", "山东", "北京", "上海", "甘肃", "新疆", "河南", "广西", "西藏"]
map=Map("Map 结合 VisualMap 示例", width=1200, height=600)
map.add("", attr, value, maptype='china', is_visualmap=True, visual_text_color='#000')
# map.show_config()
map.render()
