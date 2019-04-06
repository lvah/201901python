"""
文件名: blog_tags.py
日期: 2019-04-06  
作者: lvah
联系: xc_guofan@qq.com
代码描述: 



"""
from django.db.models import Count

from blog.models import Post, Category, Tag
from django import template


register = template.Library()

# 告诉系统get_recent_posts是一个自定义模板标签
@register.simple_tag
def get_recent_posts(num=3):
    """获取最新的博客, 默认是3篇"""
    return  Post.objects.order_by('-created_time').all()[:num]

@register.simple_tag
def get_categories():
    """获取博客的所有分类"""
    # 聚合(group_by)
    # 给分类加一列属性(文章数量), 并且不显示文章数量小于等于0的分类;
    return  Category.objects.annotate(post_num  = Count('post')).filter(post_num__gt=0)

@register.simple_tag
def get_tags():
    """获取博客的所有标签"""
    return  Tag.objects.all()


@register.simple_tag
def get_archive():
    # print(Post.objects.dates('created_time', 'month', 'DESC'))
    return  Post.objects.dates('created_time', 'month', 'DESC')
