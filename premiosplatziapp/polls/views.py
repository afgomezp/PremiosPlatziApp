from secrets import choice
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Question, Choice

# Create your views here.

from django.http import HttpResponse

def index(request):
    latest_question_list = Question.objects.all()

    return render(request, "polls/index.html", {
        "latest_question_list":latest_question_list
    } )



def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {
        "question": question
    })

def results(request, question_id):
    return HttpResponse (f'estas viendo los resultados a la pregunta número: {question_id}')

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    
    except (KeyError, Choice.DoesNotExist):
        return render(request, "polls/detail.html", {
            "question":question,
            "error_message": "no elegiste una respuesta"
        })
    
    else:
        selected_choice.votes +=1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question_id,)))