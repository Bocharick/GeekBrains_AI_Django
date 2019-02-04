from django.urls import path
from .views import (index, about, contacts)


urlpatterns = [
    path('contacts/', contacts),
    path('about/', about),
    path('', index),
]