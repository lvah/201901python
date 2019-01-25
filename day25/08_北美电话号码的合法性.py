"""
文件名: $NAME.py
日期: 25  
作者: lvah
联系: xc_guofan@qq.com
代码描述: 

问题描述:
    北美电话的常用格式:(eg: 2703877865)
            前3位: 第一位是区号以2~9开头 , 第2位是0~8, 第三位数字可任意;
            中间三位数字:第一位是交换机号, 以2~9开头, 后面两位任意
            最后四位数字: 数字不做限制;

pattern = r'[2-9][0-8]\d[2-9]\d\d\d\d\d\d'


"""
import re
# pattern = r'[2-9][0-8]\d[2-9]\d\d\d\d\d\d'   # 传统方式
pattern = r'[2-9][0-8]\d[2-9]\d{6}'   # 利用重复符号方式
string = "phone: 1777777777"
print(re.findall(pattern, string))




