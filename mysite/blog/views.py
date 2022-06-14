
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login , logout
# from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from blog.models import MyPost
from .forms import PostGetForm ,CreatUser ,AuthForm



# Create your views here.
def login_views(request):
    if request.method == 'POST':
        form = AuthForm(request.POST)
        print(form)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            print(user)
            if user is not None:
                login(request, user)
                return redirect('blog:showpost')
            else:
                print('user not found')
    else:
        form = AuthForm()

    context = {'form':form}
    return render(request,'login.html',context)
    

        
  
@login_required
def logout_views(request):
    logout(request)
    return redirect ('/')


def signup_views(request):
    if request.method == 'POST':
        form = CreatUser(request.POST)
        if form.is_valid():
           cd=form.cleaned_data
           new_user=User.objects.create_user(username=cd['username'],password=cd['password'],email=cd['email'])
           login(request,new_user)
           return redirect('/')
    else:
        form = CreatUser()
    
    context = {'form':form}
    return render(request,'signup.html',context)
    
    
def show_post(request):
    posts=MyPost.objects.all()

    context={'posts':posts}
    
    return render(request,'base.html',context)


@login_required   
def get_post(request):
    if request.method =='POST':
        
        form = PostGetForm(request.POST)
        
        if form.is_valid():
            MyPost.objects.create
            form.save()
            return redirect ('/')
    else:
        form = PostGetForm()
    context={'form':form}
    return render(request,'creatpost.html',context)




