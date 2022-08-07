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
        if e.company == "Peacock":

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
        
        if e.company == "Hulu":

            driver.get("https://signup.hulu.com/account")
            time.sleep(2)
            
            #click defualt plan and select button
            driver.find_element(By.XPATH, '//*[@id="plan-1"]/div/div[2]/button').click()
            time.sleep(2)

            select_button2 = driver.find_element(By, 'BUTTON')
            select_button2.click()
            time.sleep(2)

            email_key = e.user.username
            email = driver.find_element(By.XPATH, '//*[@id="email"]')
            email.send_keys(email_key)

            password_key = e.user.password
            password = driver.find_element(By.XPATH, '//*[@id="password"]')
            password.send_keys(password_key)

            name_key = e.first_name + " " + e.user.last_name
            name = driver.find_element(By.XPATH, '//*[@id="firstName"]')
            name.send_keys(name_key)
            

            
            bday_Month_key = e.birthday_month
            month = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/main/div[2]/div/form/div[2]/div[4]/div[2]/div/div/div')
            Select(month).select_by_visible_text(bday_Month_key)

            bday_Day_key = e.birthday_day
            day = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/main/div[2]/div/form/div[2]/div[4]/div[3]/div/div/div')
            Select(day).select_by_visible_text(bday_Day_key)

            bday_Year_key = e.birthday_year
            year = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/main/div[2]/div/form/div[2]/div[4]/div[4]/div/div/div')
            Select(year).select_by_visible_text(bday_Year_key)


            if e.gender == "Man":
                gender = "Male"
            elif e.gender == "Woman":
                gender = "Female"
            else:
                gender = "Prefer not to say"
            select = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/main/div[2]/div/form/div[2]/div[5]/div[2]/div/div/div')
            Select(select).select_by_visible_text(gender)
        
        if e.company == 'Netflix':
            driver.get("https://www.netflix.com")
            time.sleep(2)

            email_key = e.user.username
            email = driver.find_element(By.XPATH, '//*[@id="id_email_hero_fuji"]')
            email.send_keys(email_key)
            time.sleep(1)

            #click from get started page to password page
            driver.find_element(By.XPATH, '//*[@id="appMountPoint"]/div/div/div/div/div/div[2]/div[1]/div[2]/form/div/div/button/span[1]').click()
            time.sleep(2)
            #click 'Next' from 'Finish setting up your account'
            driver.find_element(By.XPATH, '//*[@id="appMountPoint"]/div/div/div[2]/div/div[2]/button').click()
            time.sleep(2)

            password_key = e.user.password
            password = driver.find_element(By.XPATH, '//*[@id="id_password"]')
            password.send_keys(password_key)
            driver.find_element(By.XPATH, '//*[@id="appMountPoint"]/div/div/div[2]/div/form/div/div[2]/button').click()
            time.sleep(2)






            










        
    
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

