from django.shortcuts import render

# Create your views here.

def cart_contents_view(request):
    """
    View that renders the cart page
    """
    return render(request, "cart.html")