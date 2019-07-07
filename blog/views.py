from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from .models import Blog
from django.core.paginator import Paginator
from django.utils import timezone


# Create your views here.

def home(request):
    blogs = Blog.objects 
    blog_list = Blog.objects.all()
    paginator = Paginator(blog_list, 3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'home.html', {'blogs':blogs, 'posts':posts})

def detail(request, blog_id):
    blog_details = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'datails': blog_details})

def new(request):
    return render(request, 'new.html')

def create(request):
    if request.method == "POST":
        blog = Blog()
        blog.title = request.POST['title']
        blog.body = request.POST['body']
        blog.pub_date = timezone.datetime.now()
        blog.save()
        return redirect('/blog/' + str(blog.id))
    else:
        return HttpResponse('잘못된 접근입니다.')

def edit(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    if request.method == "POST":
        blog.title = request.POST['title']
        blog.body = request.POST['body']
        blog.pub_date = timezone.datetime.now()
        blog.save()
        return redirect('/blog/'+ str(blog.id)) # int-> str '/blog/1 '
    elif request.method == "GET":
        return render(request,'edit.html',{'blog':blog})

def delete(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    blog.delete()
    return redirect('/')