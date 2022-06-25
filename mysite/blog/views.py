
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth import authenticate, login , logout
# from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views import View

from blog.models import MyPost,Comment ,Like
from .forms import PostGetForm ,CreatUser ,AuthForm,CommentForm 


# comments are functioal one
# Create your views here.
class LoginView(View):
    form_class= AuthForm
    template_name ='login.html'
    def get(self,request):
        form=self.form_class()
        return render(request,self.template_name,{'form':form})
    def post(self,request):
        form=self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                login(request, user)
                return redirect('blog:showpost')
            else:
                print('user not found')
            
        return render(request,self.template_name,{'form':form})

        

# def login_views(request):
#     if request.method == 'POST':
#         form = AuthForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             user = authenticate(request, username=cd['username'], password=cd['password'])
#             if user is not None:
#                 login(request, user)
#                 return redirect('blog:showpost')
#             else:
#                 print('user not found')
#     else:
#         form = AuthForm()

#     context = {'form':form}
#     return render(request,'login.html',context)
    

        
class LogoutView(View):
    template_name='base.html'
    def get(self,request):
        logout(request)
        return render(request,self.template_name)
    



# @login_required
# def logout_views(request):
#     logout(request)
#     return redirect ('/')



class SignupView(View):
    form_class= CreatUser
    template_name ='signup.html'
    def get(self,request):
        form=self.form_class()
        return render(request,self.template_name,{'form':form})  
    def post(self,request):
        form=self.form_class(request.POST)
        if form.is_valid():
           cd=form.cleaned_data
           new_user=User.objects.create_user(username=cd['username'],password=cd['password'],email=cd['email'])
           login(request,new_user)
           return redirect('blog:showpost')
        else:
            print('user not found')
            
        return render(request,self.template_name,{'form':form})
 
    
    
    
    
    
# def signup_views(request):
#     if request.method == 'POST':
#         form = CreatUser(request.POST)
#         if form.is_valid():
#            cd=form.cleaned_data
#            new_user=User.objects.create_user(username=cd['username'],password=cd['password'],email=cd['email'])
#            login(request,new_user)
#            return redirect('/')
#     else:
#         form = CreatUser()
    
#     context = {'form':form}
#     return render(request,'signup.html',context)
    



class HomeView(View):
    template_name='base.html'
    
    def get(self,request):
        posts_list=MyPost.objects.all() 
        
        paginator = Paginator(posts_list, 1) # Show 3 contacts per page.

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context={
        'posts':posts_list,
        'page_obj':page_obj
         }
        
        
                 
        return render(request,self.template_name,context)
    
    
      
# def show_post(request):
#     posts=MyPost.objects.all()
    
#     context={
#         'posts':posts,
        
#             }
    
#     return render(request,'base.html',context)


class CreatPostView(View):
    form_class= PostGetForm
    template_name ='creatpost.html'
    def get(self,request):
        form=self.form_class()
        return render(request,self.template_name,{'form':form})  
    def post(self,request):
        form=self.form_class(request.POST)
        if form.is_valid():
           if form.is_valid():
            # forms=form.cleaned_data
            form.instance.author = request.user
            print(form)
            MyPost.objects.create
            form.save()
           return redirect('blog:showpost')
        
            
        return render(request,self.template_name,{'form':form})
 





# @login_required   
# def get_post(request):
#     if request.method =='POST':
        
#         form = PostGetForm(request.POST)
#         if form.is_valid():
#             # forms=form.cleaned_data
#             form.instance.author = request.user
#             print(form)
#             MyPost.objects.create
#             form.save()
#             return redirect('/')
#     else:
#         form = PostGetForm()
#     context={'form':form}
#     return render(request,'creatpost.html',context)


class detailPost(View):

    form_class= CommentForm
    template_name='detail.html'
        
    def get(self, request,*args, **kwargs):
        posts= MyPost.objects.filter(pk=kwargs.get('id'))
        post = MyPost.objects.get(pk=kwargs.get('id'))
        comments=Comment.objects.filter(post_id=kwargs.get('id'))
        form=self.form_class()
        if request.user == post.author:
            edit=True
        else:
            edit= False
        context={
            'edit':edit,
            'posts': posts,
            'comments':comments,
            'comment':form}
        return render(request,self.template_name,context)
    
    def post(self, request,*args, **kwargs):
        
        post = MyPost.objects.filter(id=kwargs.get('id'))
        
        form=self.form_class(request.POST)
        
        if form.is_valid():
            body=form.cleaned_data.get('body')
            form.save(commit=False)
            
            Comment.objects.create(post=post, commenter=request.user ,body=body )
            if request.user==post.author:
                
                edit=''
            else:
                edit= False
        else:
            print('not valid')
            
        context={
            
            
            'comment':form ,
            'post':post,
            'edit':edit,
            }
                
        return render(request,self.template_name,context)


# def detail_post(request,id):
    
    # posts= MyPost.objects.filter(pk=id)
#     comments=Comment.objects.filter(post_id=id)
#     post = MyPost.objects.get(id=id)
    
#     if request.method=="POST":
#         comment_form=CommentForm(request.POST)
        # if comment_form.is_valid():
        #    body=comment_form.cleaned_data.get('body')
           
       
        #    comment_form.save(commit=False)
    
        
        #    Comment.objects.create(post=post, commenter=request.user, body=body )
        
#     else:
#         comment_form = CommentForm()
        
        
    # if request.user==post.author:
    #     edit=''
    # else:
    #     edit= None
        
#     return render(request, 'detail.html', )
    
    
    
class likeView(View):
    
    template_name='detail.html'
    
    def post(self,request,*args, **kwargs):
        user = User.objects.get(username=request.user)
        post = MyPost.objects.get(pk=kwargs.get('id'))
        newLike = Like(user=user, post=post)
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
        
        return render(request,self.template_name)
    
    
    
# @login_required
# def like(request,id):
#     if request.method == "POST":
        
#             #make sure user can't like the post more than once. 
#             user = User.objects.get(username=request.user)
#             #find whatever post is associated with like
#             post = MyPost.objects.get(pk=id)
#             if Like.objects.filter(user=user).filter(post=post).exists():
#                Like.objects.get(user=user,post=post).delete()
#                post.user_likes.remove(user)
#                post.likes -= 1
#                post.save()
#                redirect('/detail/')
               
#             else:
                
                
#                 newLike = Like(user=user, post=post)
                
#                 newLike.alreadyLiked = True
#                 post.likes += 1
#                 #adds user to Post 
#                 post.user_likes.add(user)
#                 post.save()
#                 newLike.save()
#                 redirect('/detail/')
            
#             return render(request,'detail.html')
        
       
       
class ProfileView(View):
    form_class= CommentForm
    template_name='profile.html'
    def  get(self, request,*args, **kwargs):
        user = User.objects.filter(pk=kwargs.get('id'))
        posts=MyPost.objects.filter(author=kwargs.get('id'))    
        likes=Like.objects.filter(user=kwargs.get('id'))    
        if request.user.id==kwargs.get('id'):
            edit='edit'
        else:
            edit=False
            
        context={'user':user,'likes':likes,'edit':edit,'posts':posts}
        return render(request,self.template_name,context)
    
       
       
        
# def profile(requset,id):
#     user = User.objects.filter(pk=id)
#     posts=MyPost.objects.filter(author=id)    
#     likes=Like.objects.filter(user=id)    
#     if requset.user.id==id:
#         edit='edit'
#     else:
#         edit=False
#     print('qqqqqqqqqqqq',edit)
    
#     return render(requset,'profile.html',{'user':user,'likes':likes,'edit':edit,'posts':posts})



class EditPostView(View):
    form_class= PostGetForm
    template_name ='editpost.html'

    
    def get(self, request,*args, **kwargs):
        
        post=MyPost.objects.get(pk=kwargs.get('id'))
        if request.user==post.author:  
            form=self.form_class(instance=post)
        
        return render(request,self.template_name,{'form':form}) 
    
    def post(self, request,*args, **kwargs):
        post=get_object_or_404(MyPost, pk=kwargs.get('id'))
        if request.user == post.author:  
            form=PostGetForm(request.POST,instance=post)
            if form.is_valid():
                form.save()
                return redirect('/')
        else :
            return redirect('/')    
        return render(request,self.template_name,{'form':form}) 
        
     


    
    # def post(self,request):
    #     form=self.form_class(request.POST)
    #     if form.is_valid():
    #        if form.is_valid():
    #         # forms=form.cleaned_data
    #         form.instance.author = request.user
    #         print(form)
    #         MyPost.objects.create
    #         form.save()
    #        return redirect('blog:showpost')
        
            
    #     return render(request,self.template_name,{'form':form})




# @login_required
# def edit_post(request,id):
    
#     post=MyPost.objects.get(pk=id)
#     if request.user==post.author:
        
#         if request.method =='POST':
#             form=PostGetForm(request.POST,instance=post)
#             if form.is_valid():
#                 form.save()
#                 return redirect('/')
#         else:
#             form=PostGetForm(instance=post)
#     else:
#         return redirect('/')         
        
#     return render(request,'editpost.html',{'form':form})

class EditUserView(View):
    form_class= CreatUser
    template_name ='edituser.html'

    def post(self, request,*args, **kwargs):
        user=User.objects.get(pk=kwargs.get('id'))
        if request.user==user:
            form=self.form_class(request.POST,instance=user)
            if form.is_valid():
                form.save(commit=False)
                return redirect('/')
        else:
            return redirect('/')    
        return render(request,self.template_name,{'form':form}) 
        
    def get(self, request,*args, **kwargs):
        user=User.objects.get(pk=kwargs.get('id'))
        if request.user==user:  
            form=self.form_class(instance=user)
        return render(request,self.template_name,{'form':form})  







# @login_required


# def edit_user(request,id):
#     user=User.objects.get(id=id)
#     if request.user==user:
#         if request.method =='POST':
            
#             form=CreatUser(request.POST,instance=user)
#             if form.is_valid():
#                 form.save()
#                 return redirect('/')
        
#         else:
#             form=CreatUser(instance=user)
#     else:
#         return redirect('/')    
    
#     return render(request,'edituser.html',{'form':form})