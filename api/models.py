from django.db import models


# Create your models here.

class Post(models.Model):
    name = models.CharField(max_length=255)
    des = models.CharField(max_length=500)
    username = models.CharField(max_length=255)
    image = models.ImageField(upload_to="image/")


# testi Amin
