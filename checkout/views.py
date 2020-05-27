from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import OrderForm, PaymentForm
from .models import OrderItem
from django.conf import settings
from django.utils import timezone
from products.models import Product
import stripe

# Create your views here.

@login_required()
def checkout_view(request):
    """
    renders checkout page
    """
    return render(request, "checkout.html")