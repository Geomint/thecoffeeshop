from django.shortcuts import render

# Create your views here.


def index(request):
    """
    Returns the index.html home page
    """
    page_title = 'Home Page'
    return render(request, "index.html", {'page_title': page_title})
