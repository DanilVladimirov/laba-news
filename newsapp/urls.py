from django.contrib import admin
from django.urls import path
from newsapp.views import index, create_news

urlpatterns = [
    path('', index, name='get_news'),
    path('create-news', create_news, name='create_news')
]
