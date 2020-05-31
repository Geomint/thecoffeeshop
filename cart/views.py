from django.shortcuts import render, redirect, reverse

# Create your views here.


def cart_contents_view(request):
    """
    View that renders the cart page
    """
    return render(request, "cart.html")


def add_to_cart_view(request, id):
    """
    View that allows user to add items to cart
    """
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})
    if id in cart:
        cart[id] = int(cart[id]) + quantity
    else:
        cart[id] = cart.get(id, quantity)
    request.session['cart'] = cart
    return redirect(reverse('cart'))


def adjust_cart_view(request, id):
    """
    View that allows the user to alter the quantity of items in cart
    """
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})
    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)

    request.session['cart'] = cart
    return redirect(reverse('cart'))
