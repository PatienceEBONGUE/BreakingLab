# Generated by Django 3.0.6 on 2020-06-24 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laboratoire', '0009_newlab_flag'),
        ('account', '0007_profile_cours'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='lab',
            field=models.ManyToManyField(to='laboratoire.NewLab'),
        ),
    ]
