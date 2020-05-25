from django.shortcuts import get_object_or_404
from products.models import Product


def cart_session(request):
    """
    Context for the cart for the user in session
    """

    cart = request.session.get('cart', {})
    cart_items = []
    total = 0
    product_total = 0
    for id, quantity in cart.items():
        product = get_object_or_404(Product, pk=id)
        total += quantity * product.price
        product_total += quantity
        cart_items.append({'id': id, 'quantity': quantity, 'product': product})
    return {'cart_items': cart_items, 'total': total, 'product_total': product_total}
