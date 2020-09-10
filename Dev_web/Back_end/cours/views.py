from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import CreateCourseForm, EditCourseForm
from .models import Cours, Subject
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse

import datetime

# Create your views here.


def cours(request):
    queryset = Cours.objects.all().order_by('-created_on')
    context = {
        "object_list" : queryset
    }
    return render(request, 'Pages/cours.html', context)

def cours_detail(request, id):
    obj = get_object_or_404(Cours, id=id)
    context = {
        "object" : obj
    }
    return render(request, 'Pages/cours_detail.html',context)


@login_required(login_url='connexion')
def supprime_cours(request, id):

    obj = get_object_or_404(Cours, id=id)
    if request.method == 'POST':
        obj.delete()
        return redirect('cours:cours')
    context = {
        "object" : obj
    }
    return render(request, 'Pages/supprime_cours.html',context)


@login_required(login_url='connexion')
def ajouter_cours(request):
    form = CreateCourseForm()

    if request.method == 'POST':
        form = CreateCourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cours:cours')

    context = {'form': form}
    return render(request, 'Pages/ajouter_cours.html', context)

@login_required(login_url='connexion')
def edit_cours(request, id): 
    instance = Cours.objects.get(id=id)    
    form = EditCourseForm()
    form.fields['title'].initial = Cours.objects.get(id=id).title 
    form.fields['subject'].initial = Cours.objects.get(id=id).subject
    form.fields['image'].initial = Cours.objects.get(id=id).image
    form.fields['level'].initial = Cours.objects.get(id=id).level 
    form.fields['description'].initial = Cours.objects.get(id=id).description
    form.fields['content'].initial = Cours.objects.get(id=id).content 

    
    if request.method == 'POST':
        form = EditCourseForm(request.POST, instance=instance)
        if form.is_valid():
            cours = Cours (
                title = form.cleaned_data['title'], 
                subject = form.cleaned_data['subject'], 
                level = form.cleaned_data['level'],
                description = form.cleaned_data['description'], 
                content = form.cleaned_data['content'] 
            )
            form.save()
            return redirect(reverse('cours:cours_detail', kwargs={"id": id}))

    context = {'form': form}
    return render(request, 'Pages/ajouter_cours.html', context)