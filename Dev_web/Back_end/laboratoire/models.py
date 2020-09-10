from django.db import models

# Create your models here.

class NewLab(models.Model):
    title = models.CharField(max_length = 120)
    image = models.CharField(max_length = 120)
    subject = models.CharField(max_length = 120)
    level = models.CharField(max_length = 120)
    #level = models.DecimalField(decimal_places = 2, max_digits = 3)
    duration = models.TextField()
    description = models.TextField()
    flag = models.CharField(max_length = 120)

    def __str__(self):
        return self.title