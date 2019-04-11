from django.shortcuts import render, redirect,get_object_or_404
from .serializers import QuizSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import *
from .forms import *
from rest_framework import generics


def showQuizez(request):
    AllQuiz = Quiz.objects.all()
    return render(request, 'AllQuizzes.html', {'Objects': AllQuiz})


def addQuiz(request):
    initial = {'skill_type': 'Any Default skill type'}
    # We defined initial values in the view cuz it depends on the view, so we can't build it in the forms itself
    form = CreateQuizForm(request.POST or None, initial=initial)
    if form.is_valid():
        form.save()
        # below is another method to save the data, you can use it if you used forms.Form not forms.FormModel
        # Quiz.objects.create(**form.cleaned_data)
        return redirect('/showquizzes/')
    return render(request, 'createquizz.html', {'form': form})


def updateQuiz(request, id):
    q = Quiz.objects.get(id=id)
    form = CreateQuizForm(request.POST or None, instance=q)
    if form.is_valid():
        form.save()
        print(form.cleaned_data)
        return redirect('/showquizzes/')
    else:
        print(form.errors)
    return render(request, 'editequizz.html', {'form': form})

def deleteQuiz(request,id):
    q = get_object_or_404(Quiz,id=id).delete()
    return redirect('/showquizzes/')
def showQuizDetails(request, id):
    if request.method == "GET":
        try:
            quiz = Quiz.objects.get(id=id)
        except:
            return HttpResponse("<h1> No such ID is available </h1>")
        return render(request, 'QuizDetails.html', {'quiz': quiz})
    elif request.method == "POST":
        # obj = Solved.objects.create()
        # post will contains the data I submitted, such as the radio buttons
        # obj.quiz_id = request.POST['Q1']
        questions = Quiz.objects.get(id=id).question_set.all()
        score = 0
        data = request.POST
        for i, q in enumerate(questions):
            if q.Answer == data['Q' + str(i)]:
                score += 1

        s = Solved.objects.create(score=score, quiz_id=id, user_id=request.user.id)
        s.save()
        # here I have to change it to return again to the get method
        return showQuizez(request)


def getResults(request):
    objects = Solved.objects.all()
    list = []
    res = []
    for obj in objects:
        if [obj.user_id, obj.quiz_id] not in list:
            list.append([obj.user_id, obj.quiz_id])
            res.append(obj)

    return render(request, 'results.html', {'objects': res})


class QuizAPI(APIView):
    """
    API endpoint that allows Quizzes to be viewed or edited.
    """

    def get(self, request):
        AllQuizzes = Quiz.objects.all()
        # the many param informs the serializer that it will be serializing more than a single Quiz.
        seralizer = QuizSerializer(AllQuizzes, many=True)
        return Response(seralizer.data)

    def post(self, request):

        data = request.data

        # in this way we have to pass all of the data, wlw 7ad naes yb2a 5las kda
        serializer = QuizSerializer(data=data['quiz'])

        # serializer = QuizSerializer(data={'title':data['title'],'skill_type':data['skill_type'],'created_by':data['created_by']})
        if serializer.is_valid(raise_exception=True):
            q = serializer.save()

        return Response({"success": "Article '{}' created successfully".format(data['quiz']['title'])})

    def put(self):
        pass

    # id will be sent as param in the url
    # http://localhost:8000/deletequiz/14
    def delete(self, request, id):
        try:
            # This should be called from only PostMan with a Delete Request
            to_be_deleted = Quiz.objects.get(id=id)
            to_be_deleted.delete()
            return Response({"successfully deleted"}, status=204)
        except:
            return Response({"No such available quiz"})


class GetQuizzes(generics.ListAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
