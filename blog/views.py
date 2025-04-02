from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from .forms import PostForm

# Create your views here.


def index(request):
    # получение всех постов (select * from blog_post)
    posts = Post.objects.all()
    context = {"title": "Главная страница", "posts": posts}
    return render(request, template_name='blog/index.html', context=context)

def about(request):
    context = {"title": "О сайте"}
    return render(request, template_name='blog/about.html', context=context)

def add_post(request):
    if request.method == "GET":
        post_form = PostForm()
        context = {"title": "Добавить пост",'form': post_form}
        return render(request, template_name='blog/post_add.html', context=context)

    if request.method == "POST":
        post_form = PostForm(data=request.POST)
        if post_form.is_valid():
            post = Post()
            post.title = post_form.cleaned_data['title']
            post.text = post_form.cleaned_data['text']
            post.author = post_form.cleaned_data['author'] # request.user когда юзер зашёл под своим именем
            post.save()
            return index(request)

def read_post(request, pk):
    post = Post.objects.get(pk=pk) # post = Post.objects.filter(pk=pk).first() - если несколько нужно фильтровать
    context = {"title":"Информация о посте", "post": post}
    return render(request, template_name="blog/post_detail.html", context=context)