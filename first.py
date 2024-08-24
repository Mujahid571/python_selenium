import time

from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')  # Optional: Add any additional options you need
driver = webdriver.Chrome(options=options)
driver.get('https://www.saucedemo.com/')
driver.maximize_window()

# This is Username section
user_name = driver.find_element(By.ID,"user-name")
user_name.send_keys("standard_user")

#This is Passwor section
mypassword = driver.find_element(By.ID,"password")
mypassword.send_keys("secret_sauce")
time.sleep(2)
# This is login section
mylogin = driver.find_element(By.ID,"login-button")
mylogin.click()
time.sleep(5)
driver.quit()