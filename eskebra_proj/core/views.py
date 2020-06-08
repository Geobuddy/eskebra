from django.shortcuts import render, get_object_or_404, redirect
from .models import Ads, User
from .forms import AddEmail, Vendor
import datetime


#Create a function to check wether parms are valid 
def is_valid_param(param):
        return param != '' and param is not None

def filter(request):
        ads = Ads.objects.order_by('-created_date').all()
        title_contains_query = request.GET.get('title_contains')        
        category_contains_query= request.GET.get('category')

        # vendor_contains_query = request.GET.get('theForm')

        if is_valid_param(title_contains_query):
                ads = ads.filter(name__icontains=title_contains_query)
        
        if is_valid_param(category_contains_query):
                ads = ads.filter(category__icontains=category_contains_query)

        # if is_valid_param(vendor_contains_query):
        #         ads = ads.filter(vendor_name__icontains=vendor_contains_query)
       
        return ads

# Create your views here.
def index(request):
        ads = filter(request)
        EmailForm = AddEmail()
        myform = Vendor()
        today = datetime.datetime.now()
        
        data = {'myads': ads,
                'form': EmailForm,
                'myform': myform,
                'time': today}

        return render(request, 'home.html', data)


def post(request):
        if request.method == 'POST':
                form = AddEmail(request.POST)
                if form.is_valid():
                        form.save()
                return redirect('/')

# def store(request):
#         ads = filter(request)
#         EmailForm = AddEmail()
#         myform = Vendor()
#         today = datetime.datetime.now()
        
#         data = {'myads': ads,
#                 'form': EmailForm,
#                 'myform': myform,
#                 'time': today}

#         return render(request, 'store.html', data)

# def category(request):
#         ads = filter(request)
#         EmailForm = AddEmail()
#         myform = Vendor()
#         today = datetime.datetime.now()
        
#         data = {'myads': ads,
#                 'form': EmailForm,
#                 'myform': myform,
#                 'time': today}

#         return render(request, 'category.html', data)

# def sub_store(request):
#         ads = filter(request)
#         EmailForm = AddEmail()
#         myform = Vendor()
#         today = datetime.datetime.now()
        
#         data = {'myads': ads,
#                 'form': EmailForm,
#                 'myform': myform,
#                 'time': today}

#         return render(request, 'sub_store.html', data)

# def sub_category(request):
#         ads = filter(request)
#         EmailForm = AddEmail()
#         myform = Vendor()
#         today = datetime.datetime.now()
        
#         data = {'myads': ads,
#                 'form': EmailForm,
#                 'myform': myform,
#                 'time': today}

#         return render(request, 'sub_category.html', data)
