from django.contrib import admin
from django.urls import path, include
from .views import *

app_name = 'movie'
urlpatterns = [
    path('movie/create/', MovieCreateView.as_view()),
    path('all/', MoviesListView.as_view()),
    path('movie/detail/<int:pk>/', MoviesDetailView.as_view()),
]
