"""Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from django.conf import settings
from home.views import *
from laboratoire.views import *
from connexion.views import *
from inscription.views import *
from account.views import *
from cours.views import *
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

urlpatterns = [
    re_path(r'^$', home, name='home'),
    re_path(r'^home/$', home, name='home'),
    re_path(r'^laboratoire/$', laboratoire, name='laboratoire'),
    re_path(r'^laboratoire/ajouter$', ajouter_laboratoire, name='ajouter_laboratoire'),
    re_path(r'^laboratoire/stopContainer$', stopContainer, name='stopContainer'),
    re_path(r'^contact/$', views.contact, name='contact'),
    re_path(r'^connexion/$', connexion_form, name='connexion'),
    re_path(r'^deconnexion/$', deconnexion, name='deconnexion'),
    re_path(r'^inscription/$', inscription_form, name='inscription'),
    re_path(r'^test/$', views.test, name='test'),
    path(r'run-sh/slug:<image>', container, name='run_sh'),
    path(r'laboratoire/laboratoire-home/slug:<laboratoire>', laboratoire_home, name='laboratoire_home'),
    path('admin/', admin.site.urls),
    path('cours/', include('cours.urls')),
    path('compte/', include('account.urls')),
    re_path(r'^cours/$', cours, name='cours'),
    re_path(r'^compte/$', profile, name='profile'),


] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)