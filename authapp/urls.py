from django.contrib import admin
from django.urls import path
from .views import UserRegisterView,UserUpdateView,PasswordChangeView
# from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views
from .views import password_success,ShowProfilePageView,EditprofileView,MakeProfilePage


urlpatterns = [
    path('register/',UserRegisterView.as_view(),name = "register"),
    path('editprofile/',UserUpdateView.as_view(),name ="update_profile" ),
    # path('password/',auth_views.PasswordChangeView.as_view(template_name ='registration/change_password.html')),
     path('password/',PasswordChangeView.as_view(template_name ='registration/change_password.html')),
     path('password_update',password_success,name = "password_update"),
     path('<int:pk>/profile/',ShowProfilePageView.as_view(),name = "showprofile"),
     path('<int:pk>/edit_profile/',EditprofileView.as_view(),name = "editprofilepage"),
     path('createprofilepage/',MakeProfilePage.as_view(),name = 'createprofilepage')
]