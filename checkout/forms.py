from django import forms
from .models import Order

class PaymentForm(forms.form):
    MONTH_CHOICES = [(i, i) for i in range(1, 12)]
    YEAR_CHOCIES = [(i, i) for i in range(2018, 2040)]

    card_number = forms.CharField(label='Card Number', required=True)
    cvv = forms.CharField(label='CVV', requrired=True)
    expiry_month = forms.ChoiceField(label='Expiry Month', choices=MONTH_CHOICES, required=True)
    expiry_year = forms.ChoiceField(label='Expiry Year', choices=YEAR_CHOCIES, required=True)
    stripe_id = forms.CharField(widget=forms.HiddenInput)