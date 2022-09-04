import datetime

from django.test import TestCase
from django.utils import timezone
from .models import Question

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


