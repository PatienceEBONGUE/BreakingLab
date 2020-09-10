from django import forms
from .models import *
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django_bleach.forms import BleachField
import datetime

class CreateCourseForm(forms.ModelForm):
    title = forms.CharField(
        max_length=120, 
        label='', 
        widget=forms.TextInput(attrs={
            'placeholder':'Titre', 
            'name':'title', 
            'value' : ''}))
   
    subject = forms.ModelChoiceField(
        label='Sujet',
        queryset=Subject.objects.all()
    )



    level = forms.CharField(
        label='', 
        required = True, 
        widget=forms.TextInput(
            attrs={
            'placeholder':'Difficulté', 
            'name':'level', 
            'value' : ''
        })) 
            

    description = forms.CharField(
        label='Description', 
        required = True, 
        widget=forms.Textarea(
            attrs={
                'name' : 'description',
                'placeholder': 'Description',
                "rows" : 5, 
                "cols" : 42, 
                'value' : ''
            }))

    content = BleachField(
        label='', 
        required = True, 
        widget=forms.Textarea(
            attrs={
                'name' : 'content',
                'placeholder': '',
                'value' : '',
                "rows" : 10, 
                "cols" : 42 
            }))

    def clean_title(self) :
        data = self.cleaned_data['title']
        return data 
    def clean_subject(self) :
        data = self.cleaned_data['subject']
        return data 
    def clean_level(self) :
        data = self.cleaned_data['level']
        return data 
    def clean_content(self) :
        data = self.cleaned_data['content']
        return data 
    def clean_description(self) :
        data = self.cleaned_data['description']
        return data 
    
    def clean_last_date(self) :
        data = self.cleaned_data['last_modified']
        return data 
    
    class Meta:
        model = Cours
        fields = '__all__'



class EditCourseForm(forms.ModelForm):
    title = forms.CharField(
        max_length=120, 
        label='Titre', 
        widget=forms.TextInput(attrs={
            'placeholder':'Titre', 
            'name':'title', 
            'value' : ''}))

    subject = forms.ModelChoiceField(
        label='Sujet',
        queryset=Subject.objects.all()
    )

    level = forms.CharField(
        label='Difficulté', 
        required = True, 
        widget=forms.TextInput(
            attrs={
            'placeholder':'Difficulté', 
            'name':'level', 
            'value' : ''
        })) 
            

  
    description = forms.CharField(
        label='Description', 
        required = True, 
        widget=forms.Textarea(
            attrs={
                'name' : 'description',
                'placeholder': 'Description',
                "rows" : 5, 
                "cols" : 42, 
                'value' : ''
            }))
    
    
    content = BleachField(
        label='', 
        required = True, 
        widget=forms.Textarea(
            attrs={
                'name' : 'content',
                'placeholder': '',
                'value' : '',
                "rows" : 10, 
                "cols" : 42 
            }))

    def clean_title(self) :
        data = self.cleaned_data['title']
        return data 
    def clean_subject(self) :
        data = self.cleaned_data['subject']
        return data 
    def clean_level(self) :
        data = self.cleaned_data['level']
        return data 
    def clean_content(self) :
        data = self.cleaned_data['content']
        return data 
    def clean_description(self) :
        data = self.cleaned_data['description']
        return data 
    
    def clean_last_date(self) :
        data = self.cleaned_data['last_modified']
        return data 
    
    class Meta:
        model = Cours
        fields = '__all__'