from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Product, Category

cart = []

def home(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    return render(request, 'shop/home.html', {'products': products, 'categories': categories})

def add_to_cart(request, id):
    product = Product.objects.get(id=id)
    cart.append(product)
    return redirect('cart')

def cart_view(request):
    total = sum([item.price for item in cart])
    return render(request, 'shop/cart.html', {'cart': cart, 'total': total})

