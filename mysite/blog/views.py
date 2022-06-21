
from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth import authenticate, login , logout
# from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from blog.models import MyPost,Comment ,Like
from .forms import PostGetForm ,CreatUser ,AuthForm,CommentForm 



# Create your views here.
def login_views(request):
    if request.method == 'POST':
        form = AuthForm(request.POST)
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
    
    context={
        'posts':posts,
        
            }
    
    return render(request,'base.html',context)


@login_required   
def get_post(request):
    if request.method =='POST':
        
        form = PostGetForm(request.POST)
        if form.is_valid():
            # forms=form.cleaned_data
            form.instance.author = request.user
            print(form)
            MyPost.objects.create
            form.save()
            return redirect('/')
    else:
        form = PostGetForm()
    context={'form':form}
    return render(request,'creatpost.html',context)


def detail_post(request,id):
    
    posts= MyPost.objects.filter(pk=id)
    comments=Comment.objects.filter(post_id=id)
    post = MyPost.objects.get(id=id)
    
    if request.method=="POST":
        comment_form=CommentForm(request.POST)
        if comment_form.is_valid():
           body=comment_form.cleaned_data.get('body')
           
       
           comment_form.save(commit=False)
    
        
           Comment.objects.create(post=post, commenter=request.user, body=body )
        
    else:
        comment_form = CommentForm()
        
        
    if request.user==post.author:
        edit=''
    else:
        edit= None
        
    return render(request, 'detail.html', {'posts': posts,'edit':edit,'comment':comment_form ,'comments':comments })
    
@login_required
def like(request,id):
    if request.method == "POST":
        
            #make sure user can't like the post more than once. 
            user = User.objects.get(username=request.user)
            #find whatever post is associated with like
            post = MyPost.objects.get(pk=id)
            if Like.objects.filter(user=user).filter(post=post).exists():
               Like.objects.get(user=user,post=post).delete()
               post.user_likes.remove(user)
               post.likes -= 1
               post.save()
               redirect('/detail/')
               
            else:
                
                
                newLike = Like(user=user, post=post)
                
                newLike.alreadyLiked = True
                post.likes += 1
                #adds user to Post 
                post.user_likes.add(user)
                post.save()
                newLike.save()
                redirect('/detail/')
            
            return render(request,'detail.html')
        
        
def profile(requset,id):
    user = User.objects.filter(pk=id)
    posts=MyPost.objects.filter(author=id)    
    likes=Like.objects.filter(user=id)
    # for like in likes:
    #     postliked=like.post
    
    if requset.user.id==id:
        edit='edit'
    else:
        edit=False
    print('qqqqqqqqqqqq',edit)
    
    return render(requset,'profile.html',{'user':user,'likes':likes,'edit':edit,'posts':posts})


@login_required
def edit_post(request,id):
    
    post=MyPost.objects.get(pk=id)
    if request.user==post.author:
        
        if request.method =='POST':
            form=PostGetForm(request.POST,instance=post)
            if form.is_valid():
                form.save()
                return redirect('/')
        else:
            form=PostGetForm(instance=post)
    else:
        return redirect('/')         
        
    return render(request,'editpost.html',{'form':form})



@login_required
def edit_user(request,id):
    user=User.objects.get(id=id)
    if request.user==user:
        if request.method =='POST':
            
            form=CreatUser(request.POST,instance=user)
            if form.is_valid():
                form.save()
                return redirect('/')
        
        else:
            form=CreatUser(instance=user)
    else:
        return redirect('/')    
    
    return render(request,'edituser.html',{'form':form})