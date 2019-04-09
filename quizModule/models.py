from django.db import models
from datetime import timedelta
from django.contrib.auth.models import User

Programming_Languages = (('Python', 'Python'), ('Java', 'Java'), ('C++', 'C++'), ('C', 'C'), ('C#', 'C#'),
                         ('JavaScript', 'JavaScript'), ('PHP', 'PHP'), ('Prolog', 'Prolog'), ('MySQL', 'MySQL'),
                         ('TensorFlow', 'TensorFlow'))

Programming_Types = (('declarative', 'declarative'), ('procedural', 'procedural'))


class Quiz(models.Model):
    created_by = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    title = models.CharField(max_length=20, default="", blank=False)
    programming_language = models.CharField(max_length=30, choices=Programming_Languages, default='Python', blank=False)
    Programming_Type = models.CharField(max_length=1000, choices=Programming_Types, default='procedural', blank=False)
    skill_type = models.TextField(default='', blank=False)
    no_of_questions = models.IntegerField(blank=False, default=3)
    expected_duration = models.DurationField(default=timedelta(minutes=15))
    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "quizzes"

    @property
    def quest(self):
        return self.question_set.all()

    @property
    def Score_Point(self):
        return len(self.quest)*5
Answers = (('a', 'a'), ('b', 'b'), ('c', 'c'), ('d', 'd'), ('e', 'e'))


class Question(models.Model):
    question = models.CharField(max_length=2000, default='')
    Answer = models.CharField(choices=Answers, blank=False, default='a', max_length=2)
    #what if question related to many fields
    quiz_id = models.ManyToManyField(Quiz)
    a = models.CharField(max_length=200, default='', blank=True)
    b = models.CharField(max_length=200, default='', blank=True)
    c = models.CharField(max_length=200, default='', blank=True)
    d = models.CharField(max_length=200, default='', blank=True)
    e = models.CharField(max_length=200, default='', blank=True)

    def __str__(self):
        return self.question



#how to make the table have unique fields such that there can't be no 1--->1 many times
#how to return all choices of a question when I ask for a GET quiz

class Solved(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    score = models.IntegerField(default=0)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return "User"+str(self.user_id )+" --> Quiz"+str(self.quiz_id )


