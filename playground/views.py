from django.shortcuts import render
from django.http import HttpResponse
from .models import store
from products.models import product
# Create your views here.


# for get and post method ((routing))
def say_hello(request):
    content = {
        'products': product.objects.all(),
        'stores': store.objects.all(),
    }
    return render(request, 'storefront/hello.html', content)


def about(req):
    content = {
        'acc': store.objects.all(),
        'title': 'about page'
    }
    return render(req, 'storefront/about.html', content)
