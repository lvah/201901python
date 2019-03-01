"""
文件名: $NAME.py
日期: 22  
作者: lvah
联系: xc_guofan@qq.com
代码描述: 




# 数据来源: https://en.wikipedia.org/wiki/Histogram#Examples
The U.S. Census Bureau found that there were 124 million people who work outside of
their homes.[9] Using their data on the time occupied by travel to work, the table
below shows the absolute number of people who responded with travel times "at least
30 but less than 35 minutes" is higher than the numbers for the categories above and
 below it. This is likely due to people rounding their reported journey time.[citation
 needed] The problem of reporting values as somewhat arbitrarily rounded numbers is a
 common phenomenon when collecting data from people.[citation needed]


Data by absolute numbers
Interval  Width	Quantity	Quantity/width
0	5	4180	836
5	5	13687	2737
10	5	18618	3723
15	5	19634	3926
20	5	17981	3596
25	5	7190	1438
30	5	16369	3273
35	5	3212	642
40	5	4122	824
45	15	9200	613
60	30	6461	215
90	60	3435	57




哪些数据可以绘制直方图?
    - 连续的数据；
    - 没有统计过的数据； ------原始数据

    # seaborn
"""

from matplotlib import pyplot as plt

# 公司到家的的距离
interval = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 60, 90]
# 间距
width = [5, 5, 5, 5, 5, 5, 5, 5, 15, 30, 60]
# 对应的人数
quantity = [836, 2737, 3723, 3926, 3596, 1438, 3273, 642, 824, 613, 215, 57]
# 设置图形的大小
plt.figure(figsize=(10, 10))

# 绘制条形图
# plt.bar(range(12), quantity, width=1)
# 绘制折线图
plt.plot(interval, quantity)
# 设置x轴的刻度
# _x = [i-0.5 for i in range(12)]
# plt.xticks(_x, labels=interval)
plt.xticks(interval)
# 设置网格
plt.grid(linestyle='-.', alpha=0.5)

# gca====get current axis 获取当前的坐标轴
ax = plt.gca()
# 设置右边框和上边框;
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# 设置x轴为下边框
ax.xaxis.set_ticks_position('bottom')
# 设置y轴为作边框
ax.yaxis.set_ticks_position('left')
# 设置x轴和y轴的交点为(0, 0)点;
ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('data', 0 ))

# 保存图片
plt.savefig('doc/03_bar.png')