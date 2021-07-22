from django.db import models

# Create your models here.

# Crating a data base for sttoring the url link to shortten
class Url(models.Model):
    link = models.CharField(max_length=1000)
    uuid = models.CharField(max_length=10)