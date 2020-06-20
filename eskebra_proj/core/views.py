from django.shortcuts import render, get_object_or_404, redirect
from .models import Ads, User
from .forms import AddEmail, Vendor
import datetime
from django.db.models import Q
from django.contrib import messages


#Create a function to check wether parms are valid 
def is_valid_param(param):
        return param != ' ' and param is not None

def filter(request):
        ads = Ads.objects.order_by('-created_date').all()
        search_query = request.GET.get('search')        
        category_contains_query = request.GET.getlist('category')
        vendor_contains_query = request.GET.getlist('vendor_name')

        if  is_valid_param(search_query):
                or_lookup= (Q(name__icontains=search_query) |
                Q(vendor_name__iexact=search_query))
                ads = ads.filter(or_lookup)
                if not ads:
                        ads =['Not found']

        if vendor_contains_query:
                ads = ads.filter(Q(vendor_name__in=vendor_contains_query))

        if category_contains_query:
                ads = ads.filter(Q(category__in=category_contains_query))
        
        elif vendor_contains_query and category_contains_query:
                ads = ads.filter(Q(category__in=category_contains_query), Q(vendor_name__in=vendor_contains_query))

        return ads

# Create your views here.
def index(request):
        EmailForm = AddEmail()
        myform = Vendor(request.GET)
        ads = filter(request)
        new_adds = Ads.objects.filter(created_date__date=datetime.datetime.now()).order_by('-created_date')

        data = {'myads': ads,
                'form': EmailForm,
                'myform': myform,
                'new_adds': new_adds}

        return render(request, 'home.html', data)

# def wishlist(request):
#         EmailForm = AddEmail()
#         myform = Vendor(request.GET)
#         ads = filter(request)
#         new_adds = Ads.objects.filter(created_date__date=datetime.datetime.now()).order_by('-created_date')

#         data = {'myads': ads,
#                 'form': EmailForm,
#                 'myform': myform,
#                 'new_adds': new_adds}

#         return render(request, 'wishlist.html', data)

# POST Methods

def email(request):
        if request.method == 'POST':
                form = AddEmail(request.POST)
                if form.is_valid():
                        form.save()
                return redirect('/')