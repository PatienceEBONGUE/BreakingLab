# Generated by Django 3.0.6 on 2020-05-17 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laboratoire', '0004_auto_20200517_1749'),
    ]

    operations = [
        migrations.AddField(
            model_name='newlab',
            name='description',
            field=models.TextField(default='To be descipted later'),
            preserve_default=False,
        ),
    ]
