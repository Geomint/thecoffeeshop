from django.shortcuts import render
from products.models import Product

# Create your views here.

def search_view(request):
    """
    Returns a view with a list of filtered products based on search query
    """
    products = Product.objects.filter(name__icontains=request.GET['q'])
    return render(request, "products.html", {"products": products})