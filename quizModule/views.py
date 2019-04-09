from django.shortcuts import render,redirect
from .models import *
from .serializers import QuizSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
from .forms import *

def showQuizez(request):
    AllQuiz = Quiz.objects.all()
    return render(request, 'AllQuizzes.html', {'Objects': AllQuiz})


class QuizList(APIView):
    """
    API endpoint that allows Quizzes to be viewed or edited.
    """

    def get(self, request):
        AllQuizzes = Quiz.objects.all()
        seralizer = QuizSerializer(AllQuizzes, many=True)
        return Response(seralizer.data)

    def post(self):
        pass

def showQuizDetails(request, id):
    if request.method == "GET":
        try:
            quiz = Quiz.objects.get(id=id)
        except:
            return HttpResponse('No such ID is available')
        return render(request, 'QuizDetails.html', {'quiz': quiz})
    elif request.method == "POST":
        # obj = Solved.objects.create()
        # post will contains the data I submitted, such as the radio buttons
        # obj.quiz_id = request.POST['Q1']
        questions = Quiz.objects.get(id=id).question_set.all()
        score = 0
        data = request.POST
        for i,q in enumerate(questions):
            if q.Answer == data['Q'+str(i)]:
                score+=1

        s = Solved.objects.create(score=score,quiz_id=id,user_id=request.user.id)
        s.save()
        #here I have to change it to return again to the get method
        return showQuizez(request)

def getResults(request):
    objects = Solved.objects.all()
    list = []
    res = []
    for obj in objects:
        if [obj.user_id,obj.quiz_id] not in list:
            list.append([obj.user_id,obj.quiz_id])
            res.append(obj)
    return render(request,'results.html',{'objects':res})

def addQuiz(request):
    form = CreateQuizForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/showquizzes/')
    return render(request, 'createquizz.html', {'form': form})
