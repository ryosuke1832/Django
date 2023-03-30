from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def index(request):
    posts = Post.objects.all()
    params = {
        'posts':posts,
    }
    return render(request, 'blog/index.html', params)

def detail(request, post_id):
    post = Post.objects.get(id=post_id)
    params = {
        'id':post_id,
        'post':post,
    }
    return render(request, 'blog/detail.html', params)