# Generated by Django 3.0.6 on 2020-06-24 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_auto_20200623_1633'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='cours',
            field=models.ManyToManyField(to='cours.Cours'),
        ),
    ]
