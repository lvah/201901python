"""
文件名: $NAME.py
日期: 25  
作者: lvah
联系: xc_guofan@qq.com
代码描述: 

表示分组
        | : 匹配| 左右任意一个表达式即可;
        (ab): 将括号中的字符作为一个分组
        \num: 引用分组第num个匹配到的字符串
        (?P<anme>): 分组起别名
        (?P=name) : 引用分组的别名

"""
import re

print(re.findall(r'westos|hello', "hellowestos"))
# 进行分组的时候， findall方法只返回分组里面的内容;
print(re.findall(r'(http|https)(.+)', 'http_hello'))

# search
sreObj = re.search(r'(http|https)(.+)', 'http_hello')
if sreObj:
    # group方法会返回匹配的所有内容;
    print(sreObj.group())
    # groups方法返回分组里面的内容;
    print(sreObj.groups())



# 需求: 获取标签里面的文字, 并判断标签是否成对出现?
htmlStr = "<html><p>welcome to westos!</p></html>"
pattern = r'<(\w+)><(\w+)>(.+)</\2></\1>'
print(re.findall(pattern, htmlStr))
print(re.findall(pattern, htmlStr)[0][2])

# 需求: 分组起别名?
htmlStr = "<html><p>welcome to westos!</p></html>"
pattern = r'<(?P<FirstTag>\w+)><(?P<SecondTag>\w+)>(?P<Text>.+)' \
          r'</(?P=SecondTag)></(?P=FirstTag)>'
print(re.findall(pattern, htmlStr))
sreObj = re.search(pattern, htmlStr)
if sreObj:
    print(sreObj.group())
    print(sreObj.groups())
    print(sreObj.groupdict())
    print(sreObj.groupdict()['Text'])

