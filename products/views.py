from django.shortcuts import render
from .models import Product

# Create your views here.
def view_all_products(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})