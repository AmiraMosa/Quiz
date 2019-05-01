#from django.test import TestCase
import unittest
from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import render, redirect, get_object_or_404
from serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import *
from .forms import *
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
       # quiz = Quiz.objects.
        quiz = Quiz(created_by_id=1)
        self.assertEqual(quiz.created_by_id,1)

    def test_Programming_Type(self):
        quiz = Quiz()
        quiz.title="joe"
        self.assertEqual(quiz.Programming_Type, "procedural")


    def test_skill_type(self):
         quiz = Quiz()
         quiz.title="joe"
         self.assertEqual(quiz.skill_type,"")
