from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=250)
    author =models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='Blog_post')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
   
    

    class meta:
        ordering = ['publish']
        indexes =[
            models.Index(fields=['-publish'])
        ]
    def __str__(self):
        return self.title

