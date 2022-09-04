import datetime
from urllib import response

from django.test import TestCase
from django.utils import timezone
from .models import Question
from django.urls.base import reverse

# Create your tests here.

class QuestionModelTest(TestCase):

    def setUp(self):
        self.question = Question(question_text = '¿Quién es el mejor course director de platzi?')

    def test_was_published_recently_with_future_question(self):
        time = timezone.now() + datetime.timedelta(days=30)
        self.question.pub_date = time
        self.assertIs(self.question.was_published_recently(), False)

    def test_was_published_recently_with_past_question(self):
        time = timezone.now() - datetime.timedelta(days=1, minutes=1)
        self.question.pub_date = time
        self.assertIs(self.question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59)
        self.question.pub_date = time
        self.assertIs(self.question.was_published_recently(), True)
    
def create_question(question_text, days):
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)

class QuestionIndexViewtest(TestCase):
        
    def test_no_question(self):
        response= self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context["latest_question_list"], [])
    
    def test_no_future_question_displayed(self):
        response= self.client.get(reverse('polls:index'))
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(question_text='Qué es lo que más te gusta de platzi', pub_date=time)
        self.assertNotIn(future_question, response.context["latest_question_list"])
    
    def test_future_question(self):
        create_question("soy pregunta del futuo", days=30)
        response= self.client.get(reverse('polls:index'))
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context["latest_question_list"], [])
    
    def test_past_question(self):
        question = create_question("soy pregunta del pasado", days=-30)
        response= self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(response.context["latest_question_list"], [question])
