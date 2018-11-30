from django.db import models
from . import views

class Question(models):
    questions_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField()

    def __str__(self):
        return '<问题: %s>' % self.questions_text

class Choice(models):
    Choice_text = models.CharField(max_length=200)
    vote = models.IntegerField()
    questions = models.ForeignKey(Question,on_delete=models.CASCADE)

    def __str__(self):
        return '<%s: %s>' % (self.questions,self.Choice_text)