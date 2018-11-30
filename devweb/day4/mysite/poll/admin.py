from django.contrib import admin
from .models import Questions,Choice
# Register your models here.
#admin.site.register(Questions)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question_text','pub_date']
    list_filter = ['pub_date']
    search_fields = ['question_text']
    date_hierarchy = 'pub_date'
    ordering = ['-pub_date']
admin.site.register(Questions,QuestionAdmin)
admin.site.register(Choice)