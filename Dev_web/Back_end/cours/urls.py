from django.urls import path, re_path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

app_name = 'cours'
urlpatterns = [

    path('', cours, name='cours'),
    path('<int:id>/', cours_detail, name='cours_detail'),
    path('<int:id>/supprimer/', supprime_cours, name='supprime_cours'),
    path('<int:id>/modifier/', edit_cours, name='edit_cours'),
    re_path(r'^ajouter$', ajouter_cours, name='ajouter_cours')
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
