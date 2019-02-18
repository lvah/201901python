"""
文件名: $NAME.py
日期: 18  
作者: lvah
联系: xc_guofan@qq.com
代码描述: 

jieba(结巴)：切割中文的模块;
wordcloud:
pillow: python3中专门用来处理图像的模块;
numpy:
matplotlib:

"""
import re

import jieba
from PIL import Image
from wordcloud import wordcloud
import numpy as np
# text = "马云曾公开表态称对钱没兴趣称其从来没碰过钱上了微博热搜"




#  实现处理英文的词云比较简单


# 1. 切割和处理英文字符,
data = []
with open('/tmp/passwd') as f:
    for line in f:
        result1 = re.split(r'\s|:|/', line)
        # 如果item存在数据并且不是空格或者数字， 则继续进行处理;
        result2 = [item for item in result1 if not re.findall(r'\s+|\d+', item) and item]
        # print(result2)
        data.extend(result2)


# 2). 打开图片， 获取图片的数据信息;
imgObj = Image.open('./doc/wordcloud.jpg')
img_mask = np.array(imgObj)
# print(img_mask)
#
# 3). 创建词云对象， 设置属性
wcObj = wordcloud.WordCloud(
    mask = img_mask,
    background_color="snow",
    min_font_size=5,
    max_font_size=50,
    width=1000,
    height=1000,
    )
# 4). 生成图片;
# 词云绘制时， 默认之处理字符串类型， 怎么分隔每个单词? 必须以逗号分隔符分割
wcObj.generate(",".join(data))
wcObj.to_file('doc/wcObj.png')
