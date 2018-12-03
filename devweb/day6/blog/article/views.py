from django.shortcuts import render,HttpResponse,redirect
from .models import Article
from django.utils import timezone
# Create your views here.
def index(request):
    if request.method=='POST':
        title=request.POST.get('title')
        content=request.POST.get('content')
        pub_date = timezone.now()

        if title.strip() and content.strip():
            # Article.objects.create(
            #     title=title,
            #     text=content,
            #     pub_date=pub_date
            # )
            Article.objects.get_or_create(
                title=title,
                text=content,
            )

    articles = Article.objects.all()
    return render(request,'index.html',{'articles':articles})

# def hello(request):
#     return HttpResponse('<h1>hello</h1>')

def home(request):
    return render(request,'home.html')
def login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')

    if username=='tom' and password=='123456':
        request.session['IS_LOGINED']=True
        return redirect('protected')
    return redirect('home')
def protected(request):
    is_logined = request.session.get('IS_LOGINED',False)
    if is_logined:
        return render(request,'protected.html')
    redirect('home')
def hello(request):
    context = {
        'num':1000,
        'student': ['尤家和','路德维','两家先','赵明刚'],
        'dict': {'email':'you@163.com','phone':'13676240551'},
        'class': 'nsd1806',
    }
    return render(request,'hello.html',context)
