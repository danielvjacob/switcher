from django import forms
from .models import User
from .models import Billing_info

#creating user form to be used in views.py
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

#creating billing form to be used in views.py
class BillingForm(forms.ModelForm):
    class Meta:
        model = Billing_info
        fields = ['user', 'credit_num', 'expiration', 'cvc', 'card_type']