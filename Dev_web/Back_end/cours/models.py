from django.db import models
from datetime import date
from django.urls import reverse
from django.conf.urls.static import static
from django.conf import settings
from django_bleach.models import BleachField
from django.contrib.auth.models import User

import os

class Subject(models.Model):
    name = models.CharField(max_length=200, help_text='Veuillez renseigner un sujet (exemple : SQL, HTML, Bash)')
    
    def __str__(self):
        return self.name

class Cours(models.Model):
    title = models.CharField(max_length = 120)
    image = models.FilePathField(path= 'static/images', null=True, default="none")
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, help_text='Choisir un sujet pour ce cours', blank=True, null=True) 
    level = models.CharField(max_length = 120, null=True, help_text = " Veuillez renseigner un niveau de difficulté (Débutant, Moyen, Intermédiare, Avancée)")
    description = models.TextField()
    content = BleachField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now = True)

    

    def get_absolute_url(self):
        return reverse("cours:cours_detail",args=[str(self.id)]) 

    def __str__(self):
        return self.title
