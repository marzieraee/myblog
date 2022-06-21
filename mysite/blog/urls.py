from django.contrib import admin
from django.urls import path , include 
from . import views

app_name = 'blog'

urlpatterns = [
   path('login/',views.login_views,name='login'),
   path('logout/',views.logout_views,name='logout'),
   path('signup/',views.signup_views,name='signup'),
   path('getpost/',views.get_post,name='getpost'),
   path('',views.show_post,name='showpost'),
   path("detail/<int:id>/", views.detail_post, name='detial'),
   path('like/<int:id>/', views.like, name='like'),
   path("profile/<int:id>/",views.profile,name='profile'),
   path("editpost/<int:id>/", views.edit_post, name='editpost'),
   path("edituser/<int:id>/", views.edit_user, name='edituser'),

 ]



