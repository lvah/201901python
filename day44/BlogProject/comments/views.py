
# 用户提交对某篇博客的评论执行的视图函数
from django.shortcuts import get_object_or_404, redirect, render, HttpResponse
from django.urls import reverse

from blog.models import Post
from comments.forms import CommentForm


# 博客详情页提交评论要访问的视图函数；
from comments.models import Comment



def post_comment(request, id):
    """id: 值的是要评论博客的id"""
    # 获取要被评论的文章对象;
    post = get_object_or_404(Post, id=id)

    #  Django里面判断提交表单的HTTP请求方法;
    if request.method == 'POST':
        print("提交表单数据.........")
        # ****注意： 实例化表单， 需要用户post提交的数据；
        form = CommentForm(request.POST)
        # 判断表单提交的内容是否合法?
        print(form.is_valid())
        if form.is_valid():
            # 获取表单里面的内容并保存在数据库中
            comment = form.save(commit=False)
            # 并指定评论的博客对象
            comment.post = post
            # 更新博客的评论数量;
            post.comment_num += 1
            post.save()
            comment.save()
            print(Comment.objects.all())
        # return  redirect('/blog/detail/%s/' %(post.id))
        return  redirect(reverse('detail', kwargs={'id': post.id}))

