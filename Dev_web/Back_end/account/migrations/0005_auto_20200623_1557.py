# Generated by Django 3.0.6 on 2020-06-23 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20200623_1507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='profile_pics'),
        ),
    ]
