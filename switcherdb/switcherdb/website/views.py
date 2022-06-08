from django.shortcuts import render
from .models import User
from .models import Service
from .models import Billing_info


def home(request):
    all_users = User.objects.all
    return render(request, 'home.html', {'all':all_users})


