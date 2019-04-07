from django.shortcuts import render
from .models import Quiz
from .serializers import QuizSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
def createQuiz(request):
   # obj = Quiz.objects.create(Title="sdf",Body="asd",dataNow=datetime.now())

    return render(request, 'QuizAdded.html',{} )
    # return HttpResponse('5alas ana t3bt')

def showQuizez(request):
    AllQuiz = Quiz.objects.all()
    return render(request,'QuizHomePage.html',{'Objects':AllQuiz})


from rest_framework import viewsets


class QuizList(APIView):
    """
    API endpoint that allows Quizzes to be viewed or edited.
    """
    def get(self,request):
        AllQuizzes = Quiz.objects.all()
        seralizer = QuizSerializer(AllQuizzes,many=True)
        return Response(seralizer.data)
    def post(self):
        pass

