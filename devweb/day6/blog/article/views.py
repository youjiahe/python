from django.shortcuts import render,HttpResponse
from .models import Article
# Create your views here.
def index(request):
    articles = Article.objects.all()
    return render(request,'index.html',{'articles':articles})
def hello(request):
    return HttpResponse('<h1>hello</h1>')

