"""
文件名: $NAME.py
日期: 22  
作者: lvah
联系: xc_guofan@qq.com
代码描述: 


mem: 80%
cpu: 50%
"""


from pyecharts import  Gauge
import psutil


cpu_percent = psutil.cpu_percent()
print(cpu_percent)
gauge = Gauge("CPU使用率")
gauge.add("cpu", "CPU使用率", cpu_percent)
gauge.render()
