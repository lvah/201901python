"""
文件名: $NAME.py
日期: 15  
作者: lvah
联系: xc_guofan@qq.com
代码描述: 


urllib
urllib2



pyhton3中把urllib2里面的方法封装到urllib.request;
https://docs.python.org/3/library/urllib.html




HTTP常见的状态码有哪些：
    2xxx: 成功
    3xxx: 重定向
    4xxx: 客户端的问题
    5xxxx: 服务端的问题


    404： 页面找不到
    403： 拒绝访问
    200: 成功访问





    1 消息
    ▪ 100 Continue
    ▪ 101 Switching Protocols
    ▪ 102 Processing
    2 成功
    ▪ 200 OK
    ▪ 201 Created
    ▪ 202 Accepted
    ▪ 203 Non-Authoritative Information
    ▪ 204 No Content
    ▪ 205 Reset Content
    ▪ 206 Partial Content
    ▪ 207 Multi-Status
    3 重定向
    ▪ 300 Multiple Choices
    ▪ 301 Moved Permanently
    ▪ 302 Move temporarily

    ▪ 303 See Other
    ▪ 304 Not Modified
    ▪ 305 Use Proxy
    ▪ 306 Switch Proxy
    ▪ 307 Temporary Redirect
    4 请求错误
    ▪ 400 Bad Request
    ▪ 401 Unauthorized
    ▪ 402 Payment Required
    ▪ 403 Forbidden
    ▪ 404 Not Found
    ▪ 405 Method Not Allowed
    ▪ 406 Not Acceptable
    ▪ 407 Proxy Authentication Required
    ▪ 408 Request Timeout
    ▪ 409 Conflict
    ▪ 410 Gone
    ▪ 411 Length Required

    ▪ 412 Precondition Failed
    ▪ 413 Request Entity Too Large
    ▪ 414 Request-URI Too Long
    ▪ 415 Unsupported Media Type
    ▪ 416 Requested Range Not Satisfiable
    ▪ 417 Expectation Failed
    ▪ 421 too many connections
    ▪ 422 Unprocessable Entity
    ▪ 423 Locked
    ▪ 424 Failed Dependency
    ▪ 425 Unordered Collection
    ▪ 426 Upgrade Required
    ▪ 449 Retry With
    ▪ 451Unavailable For Legal Reasons

    5 服务器错误
    ▪ 500 Internal Server Error
    ▪ 501 Not Implemented
    ▪ 502 Bad Gateway
    ▪ 503 Service Unavailable
    ▪ 504 Gateway Timeout
    ▪ 505 HTTP Version Not Supported(http/1.1)
    ▪ 506 Variant Also Negotiates
    ▪ 507 Insufficient Storage
    ▪ 509 Bandwidth Limit Exceeded
    ▪ 510 Not Extended
    ▪ 600 Unparseable Response Headers


"""

from urllib import request
from urllib import error
try:
    url = 'http://www.baidu.com/hello.html'
    response = request.urlopen(url, timeout=0.01)
except error.HTTPError as e:
    print(e.code, e.headers, e.reason)
except error.URLError as e:
    print(e.reason)
else:
    content = response.read().decode('utf-8')
    print(content[:5])




