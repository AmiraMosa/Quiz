import unittest
from django.shortcuts import render, redirect, get_object_or_404

from django.http import HttpRequest, request
from django.template import RequestContext
from django.template.loader import render_to_string
from django.test import Client
from django.urls import path

from views import showQuizDetails, ModelForm
from models import Quiz
import json

from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User


class test_view(TestCase):


    def test_delete_quiz_satus(self):
        self.client = Client()
        response = self.client.get("/showquizzes/delete/{'id':1}")
        self.assertEqual(response.status_code, 404)



    def test_showquizzes_satus(self):
        self.client=Client()
        response =self.client.get("/showquizzes/")
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, 'AllQuizzes.html')


    def test_results_satus(self):
        self.client=Client()
        response =self.client.get("/results/")
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, 'results.html')

    def test_addquiz_satus(self):
        self.client=Client()
        response =self.client.get("/addquiz/")
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, 'createquizz.html')


    def test_quiz_getall_satus(self):
        self.client=Client()
        response =self.client.get("/quiz/getall/")
        self.assertEqual(response.status_code,200)





    def test_quiz_postAPI_satus(self):
        self.client=Client()
        response =self.client.get("/quiz/post/")
        self.assertEqual(response.status_code,200)



    def test_quiz_deleteAPI_satus(self):
        self.client=Client()
        response =self.client.get("/quiz/delete/")
        self.assertEqual(response.status_code,200)



    def test_quiz_editAPI_satus(self):
        self.client=Client()
        response =self.client.get("/quiz/edit/")
        self.assertEqual(response.status_code,200)

    def test_template(self):
        self.client = Client()
        response = self.client.get("/showquizzes/")
        self.assertTemplateUsed(response, 'AllQuizzes.html')









