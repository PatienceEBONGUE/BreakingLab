from django import forms
#from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.models import User
from .models import NewLab

class Lab_form(forms.ModelForm): 
    title = forms.CharField(
        max_length=120, 
        label='', 
        widget=forms.TextInput(attrs={
            'placeholder':'Titre', 
            'name':'title', 
            'value' : ''}))

    image = forms.CharField(
    max_length=120, 
    label='', 
    widget=forms.TextInput(attrs={
        'placeholder':'Image', 
        'name':'title', 
        'value' : ''}))

    subject = forms.CharField(
        label='', 
        widget=forms.TextInput(attrs={
            'placeholder':'Sujet', 
            'name':'subject', 
            'value' : ''}))  

    level = forms.CharField(
        label='', 
        required = True, 
        widget=forms.TextInput(
            attrs={
            'placeholder':'Difficulté', 
            'name':'level', 
            'value' : ''
        })) 
            

    duration = forms.CharField(
        label='', 
        required = True, 
        widget=forms.TextInput(
            attrs={
                'name' : 'duration',
                'placeholder': 'Durée',
                'value' : ''
            }))

    description = forms.CharField(
        label='', 
        required = True, 
        widget=forms.TextInput(
            attrs={
                'name' : 'description',
                'placeholder': 'Description',
                'value' : '',
            }))
    
    class Meta:
        model = NewLab
        fields = ['title', 'image', 'subject', 'level', 'duration','description']

    # def clean_title(self, *args, **kwargs):
    #     title = self.cleaned_data.get("field")
            
    #     #return data
        



