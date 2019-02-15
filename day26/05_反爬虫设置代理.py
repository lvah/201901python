"""
文件名: $NAME.py
日期: 15  
作者: lvah
联系: xc_guofan@qq.com
代码描述: 




# Ip代理

# 1. 为什么?
# 2. 如何防止IP被封？
    - 设置延迟: time.sleep(random.randint(1,3))
    - 使用IP代理， 让其他的IP代替你的IP访问页面;

# 3. 如何获取代理IP？
https://www.xicidaili.com/  (西刺代理网站提供)


# ProxyHandler ======> Request()
# Opener ======  urlopen()
# 安装Opener



# 4. 如何检测代理是否成功?        http://httpbin.org/get



"""
from urllib.request import ProxyHandler, build_opener, install_opener, urlopen
from urllib import  request




def use_proxy(proxies, url):
    # 1. 调用urllib.request.ProxyHandler
    proxy_support = ProxyHandler(proxies=proxies)
    # 2. Opener 类似于urlopen
    opener = build_opener(proxy_support)
    # 3. 安装Opener
    install_opener(opener)

    # user_agent =  "Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0"
    # user_agent =  "Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0"
    user_agent = 'Mozilla/5.0 (iPad; CPU OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3'
    # 模拟浏览器;
    opener.addheaders = [('User-agent', user_agent)]
    urlObj = urlopen(url)
    content = urlObj.read().decode('utf-8')
    return  content

if __name__ == '__main__':
    url = 'http://httpbin.org/get'
    proxies = {'https': "111.177.178.167:9999", 'http': '114.249.118.221:9000'}
    use_proxy(proxies, url)
