from django.urls import re_path
from SearchApp import views

urlpatterns = [
    re_path(r'^videos$', views.VideosApi.as_view()),
    re_path(r'^search$', views.SearchApi),
]