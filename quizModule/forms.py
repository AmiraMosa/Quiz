from .models import *
from django.forms import ModelForm,ValidationError
class CreateQuizForm (ModelForm):
    class Meta:
        model = Quiz
        fields = '__all__'
    def clean_title(self):
        title = self.cleaned_data['title']
        if 'joe' not in title:
            raise ValidationError('Keda maysa74 w 3eb ya basha, put kelmt joe in the title')
        return title
#How to change validation done by is_valid() ??