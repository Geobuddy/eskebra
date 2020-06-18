from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'), #set path to home
    path('newsletter', views.post, name='email'), #set path to home
]
