from django.db import models
from datetime import timezone


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=250)
    author =models.CharField(max_length=200)
    body = models.TextField()
    published_date = models.DateTimeField()


    def __str__(self):
        return self.title

