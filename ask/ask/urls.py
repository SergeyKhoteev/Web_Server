from django.contrib import admin
from django.urls import include, re_path
from . import views

urlpatterns = [
    re_path(r'[\w\.]*', views.test),
    re_path(r'signup\/[\w\.]*', views.test),
    re_path(r'question\/[\w\.]*', views.test),
    re_path(r'ask\/[\w\.]*', views.test),
    re_path(r'popular\/[\w\.]$*', views.test),
    re_path(r'new\/[\w\.]$*', views.test),
]
