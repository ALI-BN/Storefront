from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

accounts = [
    {
        'name': 'Ahm',
        'serialNum': '1012',
        'date': 'june 10',
        'email': 'AHM222@gamil.com'
    },
    {
        'name': 'Ali',
        'serialNum': '1011',
        'date': 'july 18',
        'email': 'Ali112x@gamil.com'
    }
]


def say_hello(request):
    return render(request, 'storefront/hello.html')


def about(req):
    content = {
        'acc': accounts,
        'title': 'about page'
    }
    return render(req, 'storefront/about.html', content)
