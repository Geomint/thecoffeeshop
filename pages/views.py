from django.shortcuts import render, redirect
from products.models import Product
from django.core.mail import send_mail
from django.contrib import messages
from .forms import ContactForm

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
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            name = contact_form.cleaned_data['name']
            message = contact_form.cleaned_data['message']
            from_email = contact_form.cleaned_data['email']
            send_mail(name, message, from_email, [
                      'george.pyott@googlemail.com'], fail_silently=False)
            messages.success(
                request, "Your message has been sent, we will be in touch soon.")
            return redirect('contact')
    else:
        contact_form = ContactForm()

    page_title = 'Contact Us'
    return render(request, "contact_us.html", {'page_title': page_title, 'contact_form': contact_form})

def thankyou_page_view(request):
    """
    Returns the thankyou.html page
    """
    page_title = 'Thank You Page'
    return render(request, "thankyou.html", {'page_title': page_title})