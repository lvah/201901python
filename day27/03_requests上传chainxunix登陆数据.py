"""
文件名: $NAME.py
日期: 16  
作者: lvah
联系: xc_guofan@qq.com
代码描述: 



"""


#  03_requests上传chainxunix登陆数据.py
#       给网站post提交登陆信息;
import requests

#  1). 上传数据；
url = 'http://bbs.chinaunix.net/member.php?mod=logging&action=login&loginsubmit=yes&loginhash=La2A2'
# url = 'http://account.chinaunix.net/login'
# postData = {
#     'username': 'LVah',
#     'password': 'gf132590'
# }



postData = {
    'username': 'T424117304',
    'password': 'T1997970120'
}
response = requests.post(url, data=postData)


# 2). 将获取的页面写入文件， 用于检测是否爬取成功;
with open('doc/chinaunix.html', 'wb') as f:
    f.write(response.content)



# 3). 查看网站的cookie信息
print(response.cookies)
for key, value in response.cookies.items():
    print(key + '=' + value)