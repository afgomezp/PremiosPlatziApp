from django.contrib import admin

# Register your models here.
#primero todo lo que se debe importar
from .models import Question, Choice
from django import forms
from django.forms.models import BaseInlineFormSet


class ChoiceImline(admin.StackedInline):
    model = Choice
    extra = 3


class Questionadmin(admin.ModelAdmin):
    fields=["pub_date", "question_text"]
    inlines=[ChoiceImline]
    list_display = ("question_text", "pub_date","was_published_recently")
    list_filter = ["pub_date"]
    search_fields = ["question_text"]


#para crear preguntas desde el administrador
admin.site.register(Question, Questionadmin)

