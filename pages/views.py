from django.shortcuts import render
from products.models import Product

# Create your views here.


def index(request):
    """
    Returns the index.html home page
    """
    products = Product.objects.all()
    page_title = 'Home Page'
    return render(request, "index.html", {'page_title': page_title, "products": products})


def about_view(request):
    """
    Returns the about_us.html page
    """
    page_title = 'About Us'
    return render(request, "about_us.html", {'page_title': page_title})

def contact_us_view(request):
    """
    Returns the contact_us.html page and allows user to post contact forms
    """
    page_title = 'Contact Us'
    return render(request, "contact_us.html", {'page_title': page_title})
