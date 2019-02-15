"""
文件名: $NAME.py
日期: 15  
作者: lvah
联系: xc_guofan@qq.com
代码描述: 



"""
from http import cookiejar
from urllib import request
from urllib.parse import urlencode
from urllib.request import HTTPCookieProcessor
cookieFileName = 'doc/chinaUnixCookie.txt'
cookie = cookiejar.MozillaCookieJar(filename=cookieFileName)
handler = HTTPCookieProcessor(cookie)
opener = request.build_opener(handler)
#  这里的url是chinaunix登陆的url;
loginUrl = 'http://bbs.chinaunix.net/member.php?mod=logging&action=login&loginsubmit=yes&loginhash=La2A2'

# 易错: POST data should be bytes, an iterable of bytes, or a file object.
postData = urlencode({
    'username': 'LVah',
    'password': 'gf132590'
}).encode('utf-8')

print(type(postData))
response = opener.open(loginUrl, data=postData)
print(response.code)
with open('doc/chinaunix.html', 'wb') as f:
    f.write(response.read())
# cookie.save(cookieFileName)

