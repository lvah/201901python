"""
文件名: $NAME.py
日期: 22  
作者: lvah
联系: xc_guofan@qq.com
代码描述: 



"""



from pyecharts import  Pie


attr = ["男", '女', '其他']
data = [100, 180, 2]


pie = Pie("example")
# 是否直接显示label信息
pie.add("", attr, data, is_label_show=True)
pie.render()