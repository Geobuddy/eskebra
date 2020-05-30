from django.shortcuts import render, get_object_or_404, redirect
from .models import Ads, User
from .forms import AddEmail



# Create your views here.
def index(request):
        ads = Ads.objects
        stores = ads.values('vendor_name').distinct('vendor_name').order_by('vendor_name')
        form = AddEmail()
        data = {'myads': ads,
                'stores': stores,
                'categories': Ads.CATEGORIES,
                'form': form}

        return render(request, 'home.html', data)


def post(request):
        if request.method == 'POST':
                form = AddEmail(request.POST)
                if form.is_valid():
                        form.save()
                return redirect('/')