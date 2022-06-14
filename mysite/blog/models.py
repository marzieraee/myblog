from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class MyPost(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    title=models.CharField(max_length=200)
    image = models.ImageField(upload_to='media/img',default='defult.jpg', blank=True, null=True)
    like=models.BooleanField(default=False)
    contet=models.TextField(null=True)
    created_date=models.DateTimeField(auto_now_add=True)
    
    
    # class Meta:
    #     verbose_name = ('MyModels')
    #     verbose_name_plural = ('MyModels')
          
    def __str__(self):
        return self.title
     
    
class MyUser(models.Model):
    username=models.ForeignKey(User,on_delete=models.CASCADE)
    email=models.EmailField()
    likes = models.PositiveIntegerField(default=0)
    