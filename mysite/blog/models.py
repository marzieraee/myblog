from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class MyPost():
    title=models.CharField(max_length=200)
    image=models.ImageField((""), upload_to=None, height_field=None, width_field=None, max_length=None)
    like=models.BooleanField()
    comment=models.TextField()
    contet=models.TextField()
      
        
    
class MyUser():
    username=models.ForeignKey(User,on_delete=models.CASCADE)
    email=models.EmailField()
    likes = models.PositiveIntegerField(default=0)
    