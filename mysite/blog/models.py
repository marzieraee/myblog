from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class MyPost(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE,null=True,related_name='related_name')
    user_likes = models.ManyToManyField(User,related_name='userlike',blank=True)
    title=models.CharField(max_length=200)
    image = models.ImageField(upload_to='media/img',default='defult.jpg', blank=True, null=True)
    contet=models.TextField(null=True)
    created_date=models.DateTimeField(auto_now_add=True)
    likes = models.PositiveIntegerField(default=0)    
          
    def __str__(self):
        return self.title
     
    
class MyUser(models.Model):
    username=models.ForeignKey(User,on_delete=models.CASCADE)
    email=models.EmailField()
    
    
class Comment(models.Model):
    post = models.ForeignKey(MyPost,on_delete=models.CASCADE,related_name='comments')
    commenter = models.ForeignKey(User,on_delete=models.CASCADE,related_name='comments')
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)


class Like(models.Model):
        user = models.ForeignKey(User,on_delete=models.CASCADE ,related_name='likeuser')
        post = models.ForeignKey(MyPost,on_delete=models.CASCADE ,related_name='likepost')
        already_likes = models.PositiveIntegerField(default=False)
        created_on = models.DateTimeField(auto_now_add=True)

