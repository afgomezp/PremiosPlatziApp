from django.urls import path
from . import views

app_name = "polls"
urlpatterns = [
    #ex: /polls/
    path("", views.IndexView.as_view(), name="index"),

    #ex details: /polls/5
    path("<int:pk>/felipe", views.DetailView.as_view(), name="detail"),

    #ex results: /polls/5/results/
    path("<int:pk>/results/", views.ResultView.as_view(), name="results"),

    #ex vote: /polls/5/vote
    path("<int:question_id>/vote/", views.vote, name="vote")
]
