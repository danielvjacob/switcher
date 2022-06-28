from django import forms
from .models import User


#creating user form to be used in views.py
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

#creating billing form to be used in views.py
class BillingForm(forms.ModelForm):
    class Meta:
        #change from billing_info to user
        model = User
        fields = ['credit_num', 'expiration', 'cvc', 'card_type']