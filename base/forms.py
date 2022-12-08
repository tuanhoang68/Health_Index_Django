from django import forms
from django.forms import ModelForm

from .models import Input

class Form(ModelForm):
    
    class Meta:
        model = Input
        fields = '__all__'



    