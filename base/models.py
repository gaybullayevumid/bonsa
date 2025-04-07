from django.db import models

# Create your models here.

class Home(models.Model):
    title_1 = models.CharField(max_length=255)
    title_2 = models.CharField(max_length=255)
    about = models.TextField()
