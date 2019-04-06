from django.core.paginator import EmptyPage, PageNotAnInteger
from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from markdown import markdown
# Create your views here.
from blog.models import Post
from comments.forms import CommentForm
from comments.models import Comment


def index(request):
    all_posts = Post.objects.order_by('-created_time').all()

    from django.core.paginator import Paginator
    # posts的所有对象， 每页显示5篇博客;
    postsObj = Paginator(all_posts, per_page=5)
    # 获取用户访问的页数
    page = request.GET.get('page')
    if not page: page = 1
    try:
        postObj  = postsObj.page(page)
        posts = postObj.object_list
        print(posts)
    except (EmptyPage, PageNotAnInteger):
        posts = postsObj.page(1).object_list

    # print("打印第一页的数据:", postsObj.page(1).object_list)
    # # 异常： EmptyPage， PageNotAnInteger
    return render(request, 'blog/index.html', context={
        'posts': posts,
        'postObj': postObj
    })


def detail(request, id):
    # 根据博客的id号进行查询博客是否存在;
    # post = Post.objects.filter(id=id).first()
    # 和上面的效果类似， 如果在Post类里面找到id=id的博客信息， 则返回对象；
    post = get_object_or_404(Post, id=id)
    # 更改博客的阅读量
    post.read_num += 1
    # 写入数据库;
    post.save()
    # 在详情页显示时， 希望转成html字符串;

    post.body = markdown(
        post.body,
        extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.toc',  # 可以自动生成目录的拓展,
            'markdown.extensions.codehilite',  # 代码高亮
        ]

    )

    # 创建评论表单类
    form = CommentForm()
    # print(post.body)
    # 获取当前博客的所有评论和评论数量
    comments = Comment.objects.filter(post=id).all()

    return render(request, 'blog/detail.html',
                  context={
                      'post': post,
                      'form': form,
                      'comments': comments,
                  })


# 查询分类
def category(request, id):
    # 查询指定分类的所有博客;
    posts = Post.objects.filter(category_id=id).all()
    # 并显示在页面中;
    return render(request, 'blog/index.html',
                  context={'posts': posts})


def tag(request, id):
    # 查询指定标签的所有博客;
    posts = Post.objects.filter(tags=id).all()
    # 并显示在页面中;
    return render(request, 'blog/index.html',
                  context={'posts': posts})


# 归档查询
def archive(request, year, month):
    # 根据归档的年月进行查询符合条件的博客文章;(目前查询有问题;)
    posts = Post.objects.filter(created_time__year=year,
                                created_time__month=month
                                ).order_by('-created_time')
    return render(request, 'blog/index.html',
                  context={
                      'posts': posts
                  })


def search(request):
    name = request.GET.get('name')
    posts = Post.objects.filter(title__icontains=name).all()
    return render(request, 'blog/index.html', context={
        'posts':posts
    })