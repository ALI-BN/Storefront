from django.shortcuts import render
from django.http import HttpResponse
from .models import store
# Create your views here.


# for get and post method ((routing))
def say_hello(request):
    return render(request, 'storefront/hello.html')


def about(req):
    content = {
        'acc': store.objects.all(),
        'title': 'about page'
    }
    return render(req, 'storefront/about.html', content)
