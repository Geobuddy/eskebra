from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'), #set path to home
    path('newsletter', views.email, name='email'), #set path to home
    # path('wishlist', views.wishlist, name='wishlist'), #set path to home
]
