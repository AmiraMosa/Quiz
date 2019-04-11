from django.db import models
from datetime import timedelta
from django.contrib.auth.models import User
from .models import  * #3amlt import le nafs lsf7a 34an kolo y4ofny

Programming_Languages = (('Python', 'Python'), ('Java', 'Java'), ('C++', 'C++'), ('C', 'C'), ('C#', 'C#'),
                         ('JavaScript', 'JavaScript'), ('PHP', 'PHP'), ('Prolog', 'Prolog'), ('MySQL', 'MySQL'),
                         ('TensorFlow', 'TensorFlow'))

Programming_Types = (('declarative', 'declarative'), ('procedural', 'procedural'))


class Quiz(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    #unique msh hy5ly kza 7ad ynf3 yst3ml nfs al esm da
    title = models.CharField(max_length=20, default="", blank=False,unique=True)
    programming_language = models.CharField(max_length=30, choices=Programming_Languages, default='Python', blank=False)
    Programming_Type = models.CharField(max_length=1000, choices=Programming_Types, default='procedural', blank=False)
    skill_type = models.TextField(default='', blank=False)
    no_of_questions = models.IntegerField(blank=False, default=0,editable=False)
    expected_duration = models.DurationField(default=timedelta(minutes=15))
    #editable is false, means we can't change it thru the admin, but it can be altered thru the __INIT__
    score = models.IntegerField(null=True, default=0,editable=False )
    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "quizzes"

    # In Django, a model field pertains to a column in the database.
    # On the other hand, a model attribute pertains to a method or property that is added to a model.
    @property
    def quest(self):
        return self.question_set.all()

    def __init__(self, *args, **kwargs):
        super(Quiz, self).__init__(*args, **kwargs)
        try:
            self.score =  len(self.quest) * 5
            self.no_of_questions = len(self.quest)
        except:
            pass



Answers = (('a', 'a'), ('b', 'b'), ('c', 'c'), ('d', 'd'), ('e', 'e'))


class Question(models.Model):
    question = models.CharField(max_length=2000, default='')
    Answer = models.CharField(choices=Answers, blank=False, default='a', max_length=2)
    # what if question related to many fields
    quiz_id = models.ManyToManyField(Quiz)
    a = models.CharField(max_length=200, default='', blank=True)
    b = models.CharField(max_length=200, default='', blank=True)
    c = models.CharField(max_length=200, default='', blank=True)
    d = models.CharField(max_length=200, default='', blank=True)
    e = models.CharField(max_length=200, default='', blank=True)

    def __str__(self):
        return self.question


# how to return all choices of a question when I ask for a GET quiz
# add edit (put) apis
# add button to add questions from specific quiz, so you will pass the id of the current quiz
# how to make password not visible , done in CRUD video
# make api to return all questions of specific quiz using its ID
# GET ALL Details or specific quiz
class Solved(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    score = models.IntegerField(default=0)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return "User" + str(self.user_id) + " --> Quiz" + str(self.quiz_id)
