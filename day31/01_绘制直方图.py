"""
文件名: $NAME.py
日期: 22  
作者: lvah
联系: xc_guofan@qq.com
代码描述: 


250部电影的时长， 电影时长的分布状态;

把数据分为多少组进行统计?
    - 如果数据在100个以内， 一般分为5-12组；
    - 组距:每个小组里面端点的距离;
组数 = 极差 / 组距

"""
import random
from matplotlib import  pyplot as plt

y = [random.randint(60,180) for i in range(250)]

# 直方图绘制数据分为20个分组;
plt.hist(y, 20)
plt.savefig('doc/01_hist.png')




