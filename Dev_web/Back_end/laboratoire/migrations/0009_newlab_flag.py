# Generated by Django 3.0.5 on 2020-06-23 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laboratoire', '0008_auto_20200530_1927'),
    ]

    operations = [
        migrations.AddField(
            model_name='newlab',
            name='flag',
            field=models.CharField(default=0, max_length=120),
            preserve_default=False,
        ),
    ]
