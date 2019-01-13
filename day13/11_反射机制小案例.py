"""



 https://www.csdn.net/nav/newarticles
 https://www.csdn.net/nav/watchers
 https://www.csdn.net/nav/news
 https://www.csdn.net/nav/ai
 https://www.csdn.net/bbs/newarticles
 https://www.csdn.net/bbs/watchers
 https://www.csdn.net/bbs/news
 https://www.csdn.net/bbs/ai


"""


class Web(object):
    def bbs(self):
        return "<h1>bbs</h1>"

    def news(self):
        return "<h1>news</h1>"

    def music(self):
        return "<h1>music</h1>"

    def movie(self):
        return "<h1>movie</h1>"
    # 假设下面还有50个
def run():
    flask = Web()
    # 用户输入url地址： http://www.baidu.com/news
    url = input('url:').split('/')[-1]
    if hasattr(flask, url):
        return getattr(flask, url)()
    else:
        return '404'


if __name__ == '__main__':
    while True:
        print(run())
