from django.views.generic import DetailView
from django.shortcuts import render, get_object_or_404, reverse
from .models import Product

# Create your views here.
def view_all_products(request):
    """
    renders all products on all-products page
    """
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})
