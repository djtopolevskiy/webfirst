from django.http import HttpResponse
from django.shortcuts import render
from .models import Product

def index(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'myapp/index.html', context)
def indexItem(request, my_id):
    product = Product.objects.get(id=my_id)
    context = {
        'product': product
    }
    return render(request, 'myapp/indexitem.html', context)
    

def about(request):
    return HttpResponse("About page")

def contact(request):
    return render(request, 'myapp/contact.html')
