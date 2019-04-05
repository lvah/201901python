from django.http import HttpResponse
from django.shortcuts import render
# render_template
from booktest.models import BookInfo, HeroInfo


# Create your views here.

# Flask默认有request对象， 存储请求的所有信息；
# Django里面， 所有的视图函数， 必须传一个参数(request对象)
def index(request):
    # 主页希望显示所有的图书信息;
    books = BookInfo.objects.all()
    # return  HttpResponse(books)  # 如何返回字符串;
    return render(request, 'booktest/index.html',
                  context={
                      'books': books
                  })


# /detail/1/
# /detail/2/
def detail(request, id):
    b = BookInfo.objects.get(id=id)
    heros = b.heroinfo_set.all()
    # return  HttpResponse("detail %s" %(id))
    return render(request, 'booktest/detail.html',
                  context={
                      'heros': heros,
                      'book': b
                  })
