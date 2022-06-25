from django.contrib import admin
from django.urls import path , include 
from . import views

app_name = 'blog'

urlpatterns = [
   path('login/',views.LoginView.as_view(),name='login'),
   path('logout/',views.LogoutView.as_view(),name='logout'),
   path('signup/',views.SignupView.as_view(),name='signup'),
   path('getpost/',views.CreatPostView.as_view(),name='getpost'),
   path('',views.HomeView.as_view(),name='showpost'),
   path("detail/<int:id>/", views.detailPost.as_view(), name='detial'),
   path('like/<int:id>/', views.likeView.as_view(), name='like'),
   path("profile/<int:id>/",views.ProfileView.as_view(),name='profile'),
   path("editpost/<int:id>/", views.EditPostView.as_view(), name='editpost'),
   path("edituser/<int:id>/", views.edit_user, name='edituser'),

 ]



