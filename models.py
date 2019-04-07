from django.db import models
from datetime import timedelta

Programming_Languages = (('Python', 'Python'), ('Java', 'Java'), ('C++', 'C++'), ('C', 'C'), ('C#', 'C#'),
                         ('JavaScript', 'JavaScript'), ('PHP', 'PHP'), ('Prolog', 'Prolog'), ('MySQL', 'MySQL'),
                         ('TensorFlow', 'TensorFlow'))

Programming_Types = (('declarative','declarative'),('procedural','procedural'))
class Quiz(models.Model):
    title = models.CharField(max_length=20, default="",blank=False)
    programming_language = models.CharField(max_length=30, choices=Programming_Languages, default='Python', blank=False)
    Programming_Type = models.CharField(max_length=10, choices=Programming_Types, default='procedural', blank=False)
    skill_type = models.TextField(default='', blank=False)
    # Id is automatically created no need to create it
    no_of_questions = models.IntegerField(blank=False, default=3)
    # each question worth 1 score point
    expected_duration = models.DurationField(default=timedelta(minutes=15))
    Score_Point = models.IntegerField(blank=False, default=10)
    def __str__(self):
        return self.title

    class meta:
        verbose_name_plural = "quizzes"

Answers = (('a','a'),('b','b'),('c','c'),('d','d'),('e','e'))
class Question(models.Model):
    question = models.CharField(max_length=2000, default='')
    Answer = models.CharField(choices=Answers,blank=False, default='a',max_length=2)
    quiz_id=models.IntegerField(blank=False, default=0)
    a = models.CharField(max_length=2000, default='')
    b = models.CharField(max_length=2000, default='')
    c = models.CharField(max_length=2000, default='')
    d = models.CharField(max_length=2000, default='')
    e = models.CharField(max_length=2000, default='')
    def __str__(self):
        return self.question