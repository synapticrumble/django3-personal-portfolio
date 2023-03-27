from django.shortcuts import get_object_or_404, render, redirect
from .models import Blog

def all_blogs(request):
    blogs = Blog.objects.order_by('-date')
    return render(request, 'blog/all_blogs.html', {'blogs':blogs})


def detail(request,blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html',{'blog':blog})
    # blog_detail = Blog.objects.get(pk=pk)
    # if blog_detail:
    #     return render(request, 'blog/detail.html',{'id':blog_id})
    # else:
    #     redirect('/')


