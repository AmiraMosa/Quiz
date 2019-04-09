from .models import *
from django.forms import ModelForm
class CreateQuizForm (ModelForm):
    class Meta:
        model = Quiz
        fields = '__all__'


