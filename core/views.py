from django.shortcuts import render

from store.models import Product

def frontpage(request):
    products = Product.objects.all()[0:6]
    context = {
        'products': products
    }
    return render(request, 'core/frontpage.html',context )

def about(request):
    return render(request, 'core/about.html')