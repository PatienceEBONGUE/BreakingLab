from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Profile
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth.models import User
from cours.models import Subject, Cours

import datetime

# Create your views here.
@login_required
def profile(request):
    return render(request, 'Pages/profile.html')

@login_required
def update_profile(request, cours_id):
    user = User.objects.get(pk=request.user.id)
    user.profile.cours.add(cours_id)
    user.save()
    return redirect('cours:cours')