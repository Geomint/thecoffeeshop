from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import RegisterNewUserForm

# Create your views here.


def register_account_view(request):
    """
    A view that registers a new account into the database
    """
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = RegisterNewUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, "You have successfully created an account, log-in now!")
            return redirect('login')
    else:
        form = RegisterNewUserForm()
    return render(request, 'register.html', context={"form": form})
