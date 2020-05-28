from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from checkout.models import Order, OrderItem
from .forms import RegisterNewUserForm, LoginUserForm, UpdateUserDetailsForm, UploadProductForm

# Create your views here.


def register_account_view(request):
    """
    A view that registers a new account into the database
    """
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        register_form = RegisterNewUserForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            username = register_form.cleaned_data.get('username')
            messages.success(
                request, "You have successfully created an account, log-in now!")
            return redirect('login')
    else:
        register_form = RegisterNewUserForm()
    return render(request, 'register.html', context={"register_form": register_form})


def login_account_view(request):
    """
    A view that logs the user into session
    """
    if request.user.is_authenticated:
        return redirect(reverse('index'))
    if request.method == 'POST':
        login_form = LoginUserForm(request.POST)
        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password'])
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully logged in!")
                return redirect(reverse('index'))
            else:
                login_form.add_error(
                    None, "Your username or password is incorrect.")
    else:
        login_form = LoginUserForm()
    return render(request, 'login.html', {'login_form': login_form})


@login_required
def account_profile_view(request):
    """
    A view that returns the logged-in users profile page
    """
    user = User.objects.get(email=request.user.email)
    if request.method == 'POST':
        update_form = UpdateUserDetailsForm(
            request.POST, instance=request.user)
        if update_form.is_valid():
            update_form.save()
            messages.success(
                request, 'You have successfully updated your account details.')
            return redirect('profile')
    else:
        update_form = UpdateUserDetailsForm(instance=request.user)

    orders = Order.objects.filter(user=request.user)

    all_orders = []

    for order in orders:
        order_fetch = OrderItem.objects.filter(order=order)
        order_items = []
        order_total = 0
        for order_item in order_fetch:
            order_items.append(order_item)
            order_total += int(order_item.product.price * order_item.quantity)
        all_orders.append({'order': order, 'order_items': order_items, "total": order_total})
    
    print(all_orders)

    return render(request, 'profile_page.html', {"profile": user, "update_form": update_form, "all_orders": all_orders})


@login_required
def upload_product_view(request):
    """
    A view that allows users flagged as staff or admin to upload products from profile page
    """
    user = User.objects.get(email=request.user.email)
    if request.method == 'POST':
        product_upload = UploadProductForm(request.POST, instance=request.user)
        if product_upload.is_valid():
            product_upload.save()
            messages.success(
                request, 'You have successfully uploaded this product.')
            return redirect('profile')
    else:
        product_upload = UploadProductForm(instance=request.user)

    return render(request, 'profile_page.html', {"profile": user, "product_upload": product_upload})
