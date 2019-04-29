"""Test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from quizModule import views
urlpatterns = [
    path('admin/', admin.site.urls,name='Admin'), #Go to admin settings
    path('showquizzes/', views.showQuizez,name='All'), #get list of all quizzes
    path('', views.showQuizez), #Home Page, get list of all quizzes
    path('showquizzes/details/<int:id>', views.showQuizDetails,name='QuizDetails'), #get details of specific quiz and its questions
    path('showquizzes/edit/<int:id>', views.updateQuiz,name='EditQuiz'),  # get details of specific quiz and its questions
    path('showquizzes/delete/<int:id>', views.deleteQuiz, name='DeleteQuiz'),
    # get details of specific quiz and its questions

    path('details/<int:id>', views.showQuizDetails, name='QuizDetails'),
    path('edit/<int:id>', views.updateQuiz, name='EditQuiz'),
    path('delete/<int:id>', views.deleteQuiz, name='DeleteQuiz'),

    path('results/', views.getResults,name='Results'), #get result of all solved quizzes till now
    path('addquiz/', views.addQuiz,name='CreateQuiz'),
    path('quiz/getall/', views.QuizAPI.as_view(), name='GetAllQuizAPI'), # DONE
    path('quiz/get/', views.getQuizDetails.as_view(), name='GetSpecificQuiz'),
    path('quiz/getQuestion/', views.QuestionAPI.as_view(), name='getQuestionsAPI'),
    path('quiz/post/', views.QuizAPI.as_view(), name='PostQuiz'),
    path('quiz/deleteall', views.QuizAPI.as_view(), name='DeleteAllQuizApi'),
    path('quiz/delete/', views.QuizAPI.as_view(), name='DeleteQuizAPI'),  # This is an API no front-end HTML file required
    path('quiz/edit/', views.QuizAPI.as_view(), name='EditQuizAPI'),

]
