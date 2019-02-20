from django.urls import path
from .views import (index, about, contacts)


app_name = 'mainapp'

urlpatterns = [
    path('contacts/', contacts, name='contacts'),
    path('about/', about, name='about'),
    path('', index, name='main'),
]