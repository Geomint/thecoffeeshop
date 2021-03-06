from django import forms
from django.contrib.auth.models import User
from products.models import Product
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError


class RegisterNewUserForm(UserCreationForm):
    """
    This is the form to register a new user into the database
    """
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if User.objects.filter(email=email).exclude(username=username):
            raise forms.ValidationError(u'Email address must be unique')
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if not password1 or not password2:
            raise ValidationError("Confirm password")

        if password1 != password2:
            raise ValidationError("Passwords must match")
        return password2


class LoginUserForm(forms.Form):
    """
    Form to allow user to login to their account
    """
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UpdateUserDetailsForm(forms.ModelForm):
    """
    Form to allow user to update details
    """
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

