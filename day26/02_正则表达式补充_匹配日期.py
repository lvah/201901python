"""
文件名: $NAME.py
日期: 15  
作者: lvah
联系: xc_guofan@qq.com
代码描述:


# 2019-1-3
# 2019-1.4

# \1: 代表的是一定要与第一个分组的内容保持一致， 否则不匹配;
\d{4}(\-|\/|.)\d{1,2}\1\d{1,2}

"""

import re

date = '2019-10-10'
pattern = r'\d{4}(\-|\/|.)\d{1,2}\1\d{1,2}'

reObj = re.search(pattern, date)
if reObj:
    print(reObj.group())
    print(reObj.groups())


