from django import forms
from django.forms import widgets
from .models import Element
from django.contrib.auth import get_user_model

class ElementSearchForm(forms.ModelForm):
    class Meta:
        model = Element
        fields = ['name', ]
        widgets = {
            'name':forms.TextInput(attrs={'id':'myInput','type':'text', 'name':'query','class':'form-control','placeholder':'Name of Element/Compound'}),
        }