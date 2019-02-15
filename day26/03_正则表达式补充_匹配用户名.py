"""
文件名: $NAME.py
日期: 15  
作者: lvah
联系: xc_guofan@qq.com
代码描述:




字符串是否包含中文 []表示匹配方括号的中任意字符，
\u4e00是Unicode中汉字的开始，\u9fa5则是Unicode中汉字的结束



    [\w\-\u4e00-\u9fa5]+

"""

import re
user = '西部开源123'
pattern = r'[\w\-\u4e00-\u9fa5]+'
print(re.findall(pattern, user))

