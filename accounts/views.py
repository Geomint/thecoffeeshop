from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import RegisterNewUserForm, LoginUserForm

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
    return render(request, 'profile_page.html', {"profile": user})