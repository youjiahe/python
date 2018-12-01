from django.shortcuts import render,HttpResponse,redirect
from .models import Questions
def index(request):
    questions = Questions.objects.order_by('pub_date')
    return render(request,'index.html',{'questions':questions})
# Create your views here.
def detail(request,question_id):
    question = Questions.objects.get(id=question_id)
    return render(request,'detail.html',{'question':question})
def result(request,question_id):
    question = Questions.objects.get(id=question_id)
    return render(request,'result.html',{'question':question})
def results(request):
    questions = Questions.objects.order_by('pub_date')
    return render(request,'results.html',{'questions':questions})
def vote(request,question_id):
    questions = Questions.objects.get(id=question_id)
    choice_id = request.POST.get('choice_id')
    choice = questions.choice_set.get(id=choice_id)
    choice.vote += 1
    choice.save()

    return redirect(request,'vote.html',{'questions': questions})