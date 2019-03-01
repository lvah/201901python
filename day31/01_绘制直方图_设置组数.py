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



直方图更多的应用场景:
    - 用户年龄的分布状态;
    - 一段时间内用户的点击数分布状态;
    - 用户活跃时间的分布状态.
"""
import random
from matplotlib import pyplot as plt

y = [random.randint(60, 180) for i in range(250)]

d = 10  # 组距
# 组数
num_bins = (max(y) - min(y)) // d

# 设置x轴的刻度范围,
plt.xticks(list(range(min(y), max(y) + d))[::d])

plt.grid(linestyle='-.', alpha=0.3)

# 直方图绘制数据分为20个分组;
plt.hist(y, num_bins)
plt.savefig('doc/02_hist.png')
