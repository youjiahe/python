from django.db import models
from datetime import datetime
# Create your models here.
class Article(models.Model):
    title=models.CharField(max_length=200)
    pub_date=models.DateTimeField(default=datetime.now())
    text=models.TextField()

    def __str__(self):
        return self.title