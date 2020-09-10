from django.urls import path, re_path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

app_name = 'account'
urlpatterns = [

    path('', profile, name='profile'),
    path('<int:cours_id>', update_profile, name='update_profile')
]   