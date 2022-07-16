from ast import AsyncFunctionDef
from django.shortcuts import render
from .models import User
from .models import Service
from .forms import UserForm
import subprocess
#imports for bots
from fnmatch import fnmatchcase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# from .forms import BillingForm


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

def bots(request):
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    # driver.get("https://www.peacocktv.com/freesignup")
    # time.sleep(1)


    for e in Service.objects.all():
        driver.get("https://www.peacocktv.com/freesignup")
        time.sleep(1)
        email_key = e.user.username

        email = driver.find_element(By.XPATH, '//*[@id="email"]')
        email.send_keys(email_key)

        password_key = e.user.password
        password = driver.find_element(By.XPATH, '//*[@id="password"]')
        password.send_keys(password_key)

        gender = "Man"
        select = driver.find_element(By.XPATH, '//*[@id="gender"]')
        Select(select).select_by_visible_text(gender)

        time.sleep(3)
        #driver.quit()
    
    driver.quit()

    # cmd = 'python bots.py'
    # p = subprocess.Popen(cmd, shell=True)
    return home(request)

# #executed when loading input billing info page 
# def inputBilling(request):
#     if request.method == "POST":
#         form = BillingForm(request.POST or None)
#         if form.is_valid():
#             form.save()
#         return render(request, 'billing.html', {})
#     else:
#         return render(request, 'billing.html', {})

