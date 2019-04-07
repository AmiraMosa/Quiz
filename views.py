from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
# Create your views here.
from .models import Quiz


def createQuiz(request):
   # obj = Quiz.objects.create(Title="sdf",Body="asd",dataNow=datetime.now())

    return render(request, 'QuizAdded.html',{} )
    # return HttpResponse('5alas ana t3bt')

def showQuizez(request):
    AllQuiz = Quiz.objects.all()
    return render(request,'QuizHomePage.html',{'Objects':AllQuiz})
