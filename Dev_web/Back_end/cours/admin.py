from django.contrib import admin

# Register your models here.

from .models import Cours, Subject

admin.site.register(Cours)
admin.site.register(Subject)