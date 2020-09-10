from django.db import models
from datetime import date
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from cours.models import Cours
from laboratoire.models import NewLab
import os


class Subject(models.Model):
    name = models.CharField(max_length=200, help_text='Veuillez renseigner un sujet (exemple : SQL, HTML, Bash)') 
    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics', height_field=None, width_field=None, max_length=None, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    last_modified = models.DateTimeField(auto_now = True)
    cours = models.ManyToManyField(Cours,blank=True)
    lab = models.ManyToManyField(NewLab, blank=True)
    

    
    def get_absolute_url(self):
        return reverse("account:profile") 

    def __str__(self):
        return f'{self.user.username} Profile'

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()