from django.db import models
from . import views
from datetime import timedelta
from django.utils import timezone
# Create your models here.
class Questions(models.Model):
    question_text=models.CharField(max_length=200)
    pub_date = models.DateTimeField()

    def __str__(self):
        return '<问题： %s>' % self.question_text

    def was_pub_curentlly(self,days=7):
        return self.pub_date > timezone.now() - timedelta(days=days)

class Choice(models.Model):
    choice_text = models.CharField(max_length=200)
    vote = models.IntegerField()
    question = models.ForeignKey(Questions,on_delete=models.CASCADE)

    def __str__(self):
        return '<%s: %s>' % (self.question,self.choice_text)

