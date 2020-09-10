from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required

from .models import *

def contact(request):
    return render(request, 'Pages/contact.html')

def test(request):
    context = {}
    return render(request, 'Pages/test.html', context)