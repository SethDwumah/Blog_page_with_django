from django.shortcuts import render, redirect
from .models import Post
from .forms import SignUpForm
from django.contrib.auth import login, authenticate

# Create your views here.
def index(request):
    post = Post.objects.all()
    return render(request,'Blog/index.html',{"post":post})

def blog_list(request):
    return render(request,'Blog/blog_list.html')

def register(request):
    if request.method =='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            login(request, user)
            return redirect('block-list')
    else:
        form = SignUpForm()
    return render(request,'Blog/register.html',{'form':form})
        