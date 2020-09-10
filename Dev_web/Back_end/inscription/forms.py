from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class NewUser(UserCreationForm): 
    username = forms.CharField(
        max_length=120, 
        label='', 
        widget=forms.TextInput(attrs={
            'placeholder':'Identifiant', 
            'name':'username', 
            'value' : ''}))

    email = forms.EmailField(
        label='', 
        widget=forms.TextInput(attrs={
            'placeholder':'Adresse email', 
            'name':'email', 
            'value' : ''}))  

    password1 = forms.CharField(
        label='', 
        required = True, 
        widget=forms.PasswordInput(
            attrs={
                'name' : 'password1',
                'placeholder': 'Mot de passe'
            }))

    password2 = forms.CharField(
        label='', 
        required = True, 
        widget=forms.PasswordInput(
            attrs={
                'name' : 'password2',
                'placeholder': 'Corfirmez votre mot de passe'
            }))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_username(self, *args, **kwargs):
        data = self.cleaned_data['username']
        if data:
            try : 
                data = int(data)
            except: 
                pass   
                return data
            else:
                raise forms.ValidationError("Your username can't contain only integers or special characters") 
        return data
