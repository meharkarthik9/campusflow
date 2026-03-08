from django.urls import path
from .views import hello_new

urlpatterns = [
    path('newhello/', hello_new),
]
