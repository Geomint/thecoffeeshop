from django.shortcuts import render, redirect, reverse

# Create your views here.

def cart_contents_view(request):
    """
    View that renders the cart page
    """
    return render(request, "cart.html")

def add_to_cart_view(request, id):
    """
    view that allows user to add items to cart
    """
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})
    cart[id] = cart.get(id, quantity)
    request.session['cart'] = cart
    return redirect (reverse('home'))