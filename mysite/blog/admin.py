from django.contrib import admin
from .models import *

admin.site.register(MyPost)
admin.site.register(MyUser)
admin.site.register(Comment)
admin.site.register(Like)