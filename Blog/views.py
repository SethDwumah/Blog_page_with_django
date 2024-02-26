from django.shortcuts import render
from .models import Post
from django.contrib.auth import authenticate

# Create your views here.
def index(request):
    post = Post.objects.all()
    return render(request,'Blog/index.html',{"post":post})

