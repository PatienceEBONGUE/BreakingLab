# Generated by Django 3.0.6 on 2020-06-24 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laboratoire', '0009_newlab_flag'),
        ('account', '0008_profile_lab'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='cours',
            field=models.ManyToManyField(blank=True, null=True, to='cours.Cours'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='lab',
            field=models.ManyToManyField(blank=True, null=True, to='laboratoire.NewLab'),
        ),
    ]
