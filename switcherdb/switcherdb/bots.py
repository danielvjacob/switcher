from fnmatch import fnmatchcase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://www.peacocktv.com/freesignup")

time.sleep(1)

email_key = "abc@gmail.com"
email = driver.find_element(By.XPATH, '//*[@id="email"]')
email.send_keys(email_key)

password_key = "jsoekknbnewi19348"
password = driver.find_element(By.XPATH, '//*[@id="password"]')
password.send_keys(password_key)

gender = "Man"
select = driver.find_element(By.XPATH, '//*[@id="gender"]')
Select(select).select_by_visible_text(gender)

time.sleep(1)
driver.quit()

#fname = "John"
#lname = "Doe"
#birth_year = 
#zipcode = "74137"