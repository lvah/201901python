"""
文件名: $NAME.py
日期: 21  
作者: lvah
联系: xc_guofan@qq.com
代码描述: 


案例: 
    假设你获取到了某年内地电影票房前20的电影(列表a)和电影票房数据(列表b),那么如何更加直观的展示该数据?

    a = ["战狼2”,"速度与激情8”,"功夫瑜伽”,"西游伏妖篇”,"变形金刚5：最后的骑士”,"摔跤吧！爸爸”,
    "加勒比海盗5：死无对证”,"金刚：骷髅岛”,"极限特工：终极回归”, "侠：英雄归来”,"悟空传”,"银河护卫队2”,"情圣”,"新木乃伊”,]

    b=[56.01,26.94,17.53,16.49,15.45,12.96,11.8,11.61,11.28,11.12,10.49,
    10.3,8.75,7.55,7.32,6.99,6.88,6.86,6.58,6.23] 单位:亿

"""


from matplotlib import pyplot as plt
from matplotlib import font_manager

#  中文显示乱码问题;
myfont = font_manager.FontProperties(fname="/usr/share/fonts/cjkuni-uming/uming.ttc", size=18)
titlefont = font_manager.FontProperties(fname="/usr/share/fonts/cjkuni-uming/uming.ttc", size=24)


y_money = [56.01, 26.94, 17.53, 16.49, 15.45, 12.96, 11.8, 11.61, 11.28, 11.12, 10.49,
     10.3, 8.75, 7.55, 7.32, 6.99, 6.88, 6.86, 6.58, 6.23]
x_movies = ["流浪地球%s" %(i) for i in range(len(y_money))]

#   如何设置图片的大小；
plt.figure(figsize=(30, 10))
# (1,2)  -====('a', 10)
# 生成竖向的条形图
# plt.bar(range(len(x_movies)), y_money, color='orange', width=0.5)
# # 生成横向的条形图
plt.barh(range(len(x_movies)), y_money, color='orange', height=0.7)

# 修改刻度信息的配置
# plt.xticks(range(len(y_money)), labels=x_movies, fontproperties=myfont, rotation=45)
plt.yticks(range(len(y_money)), labels=x_movies, fontproperties=myfont, rotation=45)

# 3). x轴和y轴的描述信息；
plt.title("某年内地电影票房前20的电影和电影票房数据", fontproperties=titlefont)
plt.xlabel("电影名", fontproperties=myfont)
plt.ylabel("电影票房(单位:亿)", fontproperties=myfont)
plt.savefig('doc/bar.png')







