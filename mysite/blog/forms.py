from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


from blog.models import MyPost ,Comment 



class PostGetForm(forms.ModelForm):
    
    class Meta:
        model = MyPost
        fields = ['title','image','contet']
        
 
 
class CreatUser(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    confirm_password=forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model=User
        fields=('username','email','password')

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise ValidationError(
                "password and confirm_password does not match"
            )
class AuthForm(forms.Form):
    username = forms.CharField(max_length=255)
    password = forms.CharField(max_length=255)

    
class CommentForm(forms.ModelForm):
        
    class Meta:
        model = Comment
        fields = ('body',)
        
        
# class LikeForm(forms.ModelForm):
#     class Meta:
        
#         model= Like
#         fields = ('likes',)
    
# class EditPostForm(forms.ModelForm):
#     class Meta:
#         model= MyPost
#         feilds = ('title','image','contet',)