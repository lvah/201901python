"""
文件名: $NAME.py
日期: 22  
作者: lvah
联系: xc_guofan@qq.com
代码描述: 



"""



from pyecharts import  Liquid
import psutil


# cpu_percent = psutil.cpu_percent()
# print(cpu_percent)


from pyecharts import Liquid

# liquid = Liquid("xxxx")
# liquid.add("Liquid", [0.6])
# liquid.render()



from pyecharts import Liquid

liquid = Liquid("xxxx")
liquid.add("Liquid", [0.6, 0.5, 0.4, 0.3],  shape='pin')
liquid.render()