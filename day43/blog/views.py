from django.shortcuts import render, HttpResponse

# Create your views here.
from blog.models import Post


def index(request):
    posts = Post.objects.order_by('-created_time').all()
    return  render(request, 'blog/index.html', context={
        'posts':posts
    })


def detail(request, id):
    return  render(request, 'blog/detail.html')