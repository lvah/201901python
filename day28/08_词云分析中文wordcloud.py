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

def gen_wordcloud(text, filename):


    # 1). 强调分割中有问题的词;
    jieba.suggest_freq(('微博'), True)
    jieba.suggest_freq(('热搜'), True)

    #  2). 难点: 如何切割中文, jieba, lcut
    result = jieba.lcut(text)
    print(result)

    # 绘制词云
    # 3). 打开图片， 获取图片的数据信息;
    imgObj = Image.open('./doc/wordcloud.jpg')
    img_mask = np.array(imgObj)
    # print(img_mask)
    # 4). 创建词云对象， 设置属性
    wcObj = wordcloud.WordCloud(
        mask = img_mask,   # 数据如何填充到图片
        background_color="snow",  # 北京颜色
        font_path="/usr/share/fonts/wqy-zenhei/wqy-zenhei.ttc",  # 如果是中文， 指定字体库(fc-list :lang=zh)
        min_font_size=5,  # 图片中最小的字体大小
        max_font_size=50,   # 图片中最小的字体大小
        width=1000,  # 图片宽度
        height=1000, # 高
        )
    # 5). 生成图片;
    # 词云绘制时， 默认之处理字符串类型， 怎么分隔每个单词? 必须以逗号分隔符分割
    wcObj.generate(",".join(result))
    wcObj.to_file(filename)


if __name__ == '__main__':
    text = "马云曾公开表态称对钱没兴趣称其从来没碰过钱上了微博热搜"
    filename = 'doc/wcObj.png'
    gen_wordcloud(text, filename)