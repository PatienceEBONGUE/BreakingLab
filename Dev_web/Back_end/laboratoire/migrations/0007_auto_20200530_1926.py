# Generated by Django 3.0.6 on 2020-05-30 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laboratoire', '0006_newlab_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newlab',
            name='level',
            field=models.CharField(max_length=120),
        ),
    ]