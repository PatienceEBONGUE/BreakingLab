from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext

# Create your views here.
def deconnexion(request):
    logout(request)
    return redirect('connexion')

def connexion_form(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Votre identifiant ou votre mot de passe est incorrect.' )
    return render(request, 'Pages/connexion.html', {})