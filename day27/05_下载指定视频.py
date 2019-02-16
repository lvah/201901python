"""
文件名: $NAME.py
日期: 16  
作者: lvah
联系: xc_guofan@qq.com
代码描述: 




# url = 'https://gss0.bdstatic.com/-4o3dSag_xI4khGkpoWK1HF6hhy/baike/w%3D268%3Bg%3D0/sign=4f7bf38ac3fc1e17fdbf8b3772ab913e/d4628535e5dde7119c3d076aabefce1b9c1661ba.jpg'
url = "http://gslb.miaopai.com/stream/sJvqGN6gdTP-sWKjALzuItr7mWMiva-zduKwuw__.mp4"
"""
import requests
def get_content(url):
    try:
        user_agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.109 Safari/537.36"
        response = requests.get(url,  headers={'User-Agent': user_agent})
        print('a')
        response.raise_for_status()   # 如果返回的状态码不是200， 则抛出异常;
        response.encoding = response.apparent_encoding  # 判断网页的编码格式， 便于respons.text知道如何解码;
    except Exception as e:
        print("爬取错误")
    else:
        # print(response.url)
        print("爬取成功!")
        return  response.content  # 下载视频需要的是bytes类型

if __name__ == '__main__':
    url = 'https://gss0.bdstatic.com/-4o3dSag_xI4khGkpoWK1HF6hhy/baike/w%3D268%3Bg%3D0/sign=4f7bf38ac3fc1e17fdbf8b3772ab913e/d4628535e5dde7119c3d076aabefce1b9c1661ba.jpg'
    # url = "http://gslb.miaopai.com/stream/sJvqGN6gdTP-sWKjALzuItr7mWMiva-zduKwuw__.mp4"
    movie_content = get_content(url)
    print("正在下载....")
    with open('doc/movie.jpg', 'wb') as f:
        f.write(movie_content)
        print("下载电影完成.....")