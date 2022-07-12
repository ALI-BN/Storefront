from django.shortcuts import render
from .models import product
# Create your views here.


def productPg(req):
    content = {
        'acc': product.objects.get(id=req.product.id),
    }
    return render(req, 'storefront/product.html', content)
