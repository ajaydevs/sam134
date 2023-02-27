from django.urls import path
from .import views

urlpatterns = [
    path('c_home/',views.home),
     path('profile/',views.user_profile),
   
]