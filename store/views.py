from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(rquest):
    return render(rquest,'store/home.html')


def product_page(rquest):
    return render(rquest,'store/product.html')


def cart_detile(rquest):
    return render(rquest,'store/cart.html')

def index(rquest):
    return render(rquest,'store/index.html')
