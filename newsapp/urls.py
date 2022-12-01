from django.urls import path
from newsapp.views import index, create_news, register, log_in, settings

urlpatterns = [
    path('', index, name='get_news'),
    path('create-news', create_news, name='create_news'),
    path('register', register, name='register'),
    path('log-in', log_in, name='log_in'),
    path('settings', settings, name='settings')
]
