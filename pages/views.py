from django.shortcuts import render

# Create your views here.


def index(request):
    """
    Returns the index.html home page
    """
    page_title = 'Home Page'
    return render(request, "index.html", {'page_title': page_title})


def about_view(request):
    """
    Returns the index.html home page
    """
    page_title = 'About Us'
    return render(request, "about_us.html", {'page_title': page_title})


