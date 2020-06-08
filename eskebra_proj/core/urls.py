from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'), #set path to home
    # path('stores', views.store, name='store'), #set path to home
    # path('categories', views.category, name='category'), #set path to home
    # path('store', views.store, name='store'), #set path to home
    # path('categories', views.category, name='category'), #set path to home
    path('content', views.post, name='content'), #set path to home
]
