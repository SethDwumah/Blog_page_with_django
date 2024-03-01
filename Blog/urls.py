from django.urls import path
from .views import index,register,blog_list,Login
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path("",index, name ='home'),
    path("register/",register,name='register'),
    path("blog_list/",blog_list,name='blog-list'),
    path("login/",Login,name='login'),
    
]
