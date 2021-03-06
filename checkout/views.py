from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import OrderForm, PaymentForm
from .models import OrderItem
from django.conf import settings
from django.utils import timezone
from products.models import Product
import stripe

# Create your views here.
stripe.api_key = settings.STRIPE_SECRET

@login_required()
def checkout_view(request):
    """
    renders checkout page
    """
    if request.method == "POST":
        order_form = OrderForm(request.POST)
        payment_form = PaymentForm(request.POST)

        if order_form.is_valid() and payment_form.is_valid():
            order = order_form.save(commit=False)
            order.user = request.user
            order.date = timezone.now()
            order.save()

            cart = request.session.get('cart', {})
            total = 0
            for id, quantity in cart.items():
                product = get_object_or_404(Product, pk=id)
                total += quantity * product.price
                order_item = OrderItem(
                    order=order,
                    product=product,
                    quantity=quantity,
                )
                order_item.save()
            try:
                customer = stripe.Charge.create(
                    amount=int(total * 100),
                    currency="GBP",
                    description=request.user.email,
                    card=payment_form.cleaned_data['stripe_id']
                )
            except stripe.error.CardError:
                messages.error(request, "Your card was declined.")
            
            if customer.paid:
                request.session['cart'] = {}
                return redirect(reverse('thankyou'))
            else:
                messages.error(request, "Unable to process your payment")
        else:
            print(payment_form.errors)
            messages.error(request, "We were unable to take payment with those card details")
    else:
        order_form = OrderForm()
        payment_form = PaymentForm()

    return render(request, "checkout.html", {"order_form": order_form, "payment_form": payment_form, "publishable": settings.STRIPE_PUBLISHABLE})
