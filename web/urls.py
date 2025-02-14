from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('login/', views.login),
    path('logout/', views.logout),
    
    
    # Users Management
    path('users/', views.users),
    path('users/<int:user_id>/', views.users_show),
    path('users/create/', views.users_create),
    
    
    # Settings Management
    path('settings/', views.settings),
    path('settings/services/<int:service_id>/toggle/', views.service_toggle),
]