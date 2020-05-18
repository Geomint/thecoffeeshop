from django.shortcuts import render

# Create your views here.

def index(request):
    """
    Returns the index.html home page
    """
    return render(request, "index.html")
