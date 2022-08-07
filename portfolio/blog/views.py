from django.shortcuts import render, get_object_or_404
from .models import *

def all_blog(request):
    posts = Posts.objects.order_by('-date')
    context = {
        'text': 'hello',
        'posts': posts
    }
    return render(request, 'all_blog.html', context)

def detail(request, blog_id):
    post = get_object_or_404(Posts, pk=blog_id)
    context = {
        'post': post
    }
    return render(request, 'detail.html',context)