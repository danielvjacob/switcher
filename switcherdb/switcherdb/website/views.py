from ast import AsyncFunctionDef
from django.shortcuts import render
from .models import User
from .models import Service
from .models import Billing_info
from .forms import UserForm
from .forms import BillingForm

#executed when loading home page
def home(request):
    all_users = User.objects.all
    return render(request, 'home.html', {'all':all_users})

#executed when loading registration page
def join(request):
    if request.method == "POST":
        form = UserForm(request.POST or None)
        if form.is_valid():
            form.save()
        return home(request)
    else:
        return render(request, 'join.html', {})

#executed when loading input billing info page 
def inputBilling(request):
    if request.method == "POST":
        form = BillingForm(request.POST or None)
        if form.is_valid():
            form.save()
        return render(request, 'billing.html', {})
    else:
        return render(request, 'billing.html', {})

