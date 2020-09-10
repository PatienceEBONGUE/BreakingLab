# Generated by Django 3.0.6 on 2020-06-25 20:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_bleach.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cours',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('image', models.FilePathField(default='none', null=True, path='static/images')),
                ('level', models.CharField(help_text=' Veuillez renseigner un niveau de difficulté (Débutant, Moyen, Intermédiare, Avancée)', max_length=120, null=True)),
                ('description', models.TextField()),
                ('content', django_bleach.models.BleachField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Veuillez renseigner un sujet (exemple : SQL, HTML, Bash)', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Inscrit_Cours',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registered_on', models.DateTimeField(auto_now_add=True)),
                ('cours', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cours.Cours')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]