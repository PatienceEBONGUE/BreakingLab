#!/usr/bin/env python

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import Lab_form
from .models import NewLab
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from subprocess import Popen, PIPE

import json, time

# Create your views here.

@login_required(login_url='connexion')
def ajouter_laboratoire(request):
    form = Lab_form(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('laboratoire')
        # return render(request, 'Pages/add-lab.html')
    context = {
        'form' : form 
    }
    return render(request, 'Pages/add-lab.html', context)

@login_required(login_url='connexion')
def laboratoire(request):
    data = NewLab.objects.all()
    context = {'data' : data}
    return render(request, 'Pages/laboratoire.html', context)

@login_required(login_url='connexion')
def container(request, image):
    if request.method == 'POST':
        name = request.POST.get('name')

    process = Popen(['/home/rbilly/proj/proj-script.sh start %s %s' %(image ,request.user.username)], shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
    
    # %s %s' %(image, request.user.username)

    time.sleep(5)
    
    output = process.stdout.read()
    # errors = process.stderr.read()

    data = json.loads(output)
    port = data["port"]
    
    if image == "xss1" or image == "sqlmap1":
        page = "accueil.php"
    elif image == "access1":
        page = "accueil.php"
    elif image == "sql1":
        page = "index.php"
    else:
        page = "login.php"
    
    return redirect('http://breakinglab.billysworld.fr:%s/%s' %(port, page))
    
    #test = 'http://wwlan.billysworld.fr:%s/%s' %(port, page)
    
    # return HttpResponse("%s" %(test))

@login_required(login_url='connexion')
def stopContainer(request):

    process = Popen(['/home/rbilly/proj/proj-script.sh stop %s' %(request.user.username)], shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)

    return redirect('laboratoire')

@login_required(login_url='connexion')
def laboratoire_home(request, laboratoire):
    flag = NewLab.objects.get(image=laboratoire).flag
    description = NewLab.objects.get(image=laboratoire).description
    laboratoire_id = NewLab.objects.get(image=laboratoire).id
    titre = NewLab.objects.get(image=laboratoire).title
    if request.method == 'POST':
        flag_posted = request.POST.get('flag')
        if flag is not None:
            if flag_posted == flag :
                messages.info(request, 'Vous avez réussi !' )
                user = User.objects.get(pk=request.user.id)
                user.profile.lab.add(laboratoire_id)
                user.save()
            else:
                messages.info(request, 'Le code est incorrect.' )
    context = {'laboratoire': laboratoire, 'titre': titre, "description": description}
    return render(request, 'Pages/laboratoire-home.html', context)