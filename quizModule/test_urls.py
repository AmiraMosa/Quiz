from django.test import SimpleTestCase
from django.urls import reverse,resolve


from quizModule.views import showQuizez,getResults,addQuiz,QuizAPI


class terst_urls(SimpleTestCase):

    def test_showquizzes_url(self):
        url=reverse("All")
        self.assertEqual(resolve(url).func,showQuizez)


    def test_results_url(self):
        url=reverse("Results")
        self.assertEqual(resolve(url).func,getResults)

    def test_addquiz_url(self):
        url = reverse("CreateQuiz")
        self.assertEqual(resolve(url).func, addQuiz)

   
