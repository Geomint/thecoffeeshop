from django import forms
from .models import Order


class PaymentForm(forms.Form):
    """
    Form to allow user to enter in card details to make payment
    """
    MONTH_CHOICES = [(i, i) for i in range(1, 12)]
    YEAR_CHOCIES = [(i, i) for i in range(2018, 2040)]

    card_name = forms.CharField(label='Card Name', required=True)
    card_number = forms.CharField(label='Card Number', required=True)
    cvv = forms.CharField(label='CVV', required=True)
    expiry_month = forms.ChoiceField(
        label='Expiry Month', choices=MONTH_CHOICES, required=True)
    expiry_year = forms.ChoiceField(
        label='Expiry Year', choices=YEAR_CHOCIES, required=True)
    stripe_id = forms.CharField(widget=forms.HiddenInput)


class OrderForm(forms.ModelForm):
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
