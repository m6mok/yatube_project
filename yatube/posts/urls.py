from django.contrib import admin
from django.urls import include, path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.index, name='main'),
    path('groups/<int:num>/', views.group_posts, name='group'),
]
