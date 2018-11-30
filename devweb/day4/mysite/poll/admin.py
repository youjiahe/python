from django.contrib import admin
from .models import Questions,Choice
# Register your models here.
#admin.site.register(Questions)
class QuestionAdmin(admin.ModelAdmin):
    pass
admin.site.register(Questions,QuestionAdmin)
admin.site.register(Choice)