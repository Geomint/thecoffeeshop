from django import forms
from .models import Order


class PaymentForm(forms.Form):
    """
    Form to allow user to enter in card details to make payment
    """
    MONTH_CHOICES = [(i, i) for i in range(1, 12)]
    YEAR_CHOICES = [(i, i) for i in range(2018, 2040)]

    card_number = forms.IntegerField(
        label='Credit card number', required=False)
    cvv = forms.IntegerField(label='Security code (CVV)', required=False)
    expiry_month = forms.ChoiceField(
        label='Month', choices=MONTH_CHOICES, required=False)
    expiry_year = forms.ChoiceField(
        label='Year', choices=YEAR_CHOICES, required=False)
    stripe_id = forms.CharField(widget=forms.HiddenInput)


class OrderForm(forms.ModelForm):
    """
    This is the order form to allow user to enter details
    """
    address_line_2 = forms.CharField(required=False)
    phone_number = forms.IntegerField()

    class Meta:
        model = Order
        fields = [
            'full_name',
            'phone_number',
            'country',
            'postcode',
            'city',
            'address_line_1',
            'address_line_2',
        ]
