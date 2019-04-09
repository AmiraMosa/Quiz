from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Solved)
class QuestionsInline(admin.TabularInline):
    model = Question
    fields = ('title', 'created_by')
    readonly_fields = ('Score_Point',)
