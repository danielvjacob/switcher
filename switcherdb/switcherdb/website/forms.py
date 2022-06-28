from pyexpat import model
from django import forms
from .models import User
from multipage_form.forms import MultipageForm, ChildForm



#creating user form to be used in views.py
# class UserForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['username', 'password']


# #creating billing form to be used in views.py
# class BillingForm(forms.ModelForm):
#     class Meta:
#         #change from billing_info to user
#         model = User
#         fields = ['credit_num', 'expiration', 'cvc', 'card_type']


class UserForm(MultipageForm):
    model = User
    starting_form = "Stage1Form"

    class Stage1Form(ChildForm):
        next_form_class = "Stage2Form"

        class Meta:
            fields = ['username', 'password']
    class Stage2Form(ChildForm):
        class Meta:
            fields = ['credit_num', 'expiration', 'cvc', 'card_type']