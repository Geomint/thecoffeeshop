from django.shortcuts import render, get_object_or_404, reverse
from .models import Product

# Create your views here.


def view_all_products(request):
    """
    renders all products on all-products page
    """
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})


def view_product_detail(request, id):
    product = get_object_or_404(Product, pk=id)
    return render(request, 'product_detail.html', {'product': product})
