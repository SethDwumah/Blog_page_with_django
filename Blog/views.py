from django.shortcuts import render, redirect
from .models import Post
from .forms import SignUpForm, LoginForm
from django.contrib.auth.models import auth
from django.contrib.auth import login, authenticate
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'Blog/index.html')

def blog_list(request):
    post = Post.objects.all()
    return render(request,'Blog/blog_list.html',{"post":post})

def register(request):
    if request.method =='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog-list')
    else:
        form = SignUpForm()
    return render(request,'Blog/register.html',{'form':form})



def Login(request):
    if request.method == 'POST':
        form = LoginForm(request,data=request.POST )
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username,password=password)
            if user is not None:
                auth.login(request, user)
            
                return redirect('blog-list')
    else:
        form = LoginForm()
    return render(request, 'Blog/login.html', {'form': form})


        