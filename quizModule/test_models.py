#from django.test import TestCase
import unittest
from .models import Quiz
from datetime import timedelta
from django.db import models
from django.contrib.auth.models import User


class test_models(unittest.TestCase):

  #  def setUp(self):
   #     Quiz.objects.create(title="joe", programming_language="python")

    def test_title(self):
        quiz = Quiz(title="joe")
        self.assertEqual(str(quiz), quiz.title)

    def test_programming_language(self):
        quiz =Quiz()
        quiz.title="joe"
        self.assertEqual(quiz.programming_language,"Python")

#####probleeeeeeeeem
    def test_created_by(self):
       quiz = Quiz()
       quiz.title = "joe"
       self.assertEqual(User.__name__, "User")

    def test_Programming_Type(self):
        quiz = Quiz()
        quiz.title="joe"
        self.assertEqual(quiz.Programming_Type, "procedural")


    def test_skill_type(self):
         quiz = Quiz()
         quiz.title="joe"
         self.assertEqual(quiz.skill_type,"")
