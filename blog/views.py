from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    context = {"title": "Главная страница"}
    return render(request, template_name='blog/index.html', context=context)

def about(request):
    return HttpResponse("<h1>О сайте</h1>")