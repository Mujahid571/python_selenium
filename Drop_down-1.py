import time

from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')  # Optional: Add any additional options you need
driver = webdriver.Chrome(options=options)
driver.get("https://www.saucedemo.com/")
driver.maximize_window()
time.sleep(3)

## username
username = driver.find_element(By.ID,"user-name")
username.send_keys("standard_user")
time.sleep(3)

# passward
passwd = driver.find_element(By.ID,"password")
passwd.send_keys("secret_sauce")
time.sleep(3)

# button
btn = driver.find_element(By.ID,"login-button")
btn.click()
time.sleep(3)

# DropDown
myselect = driver.find_element(By.CLASS_NAME,"product_sort_container")
myselect.send_keys("Price (high to low)")
time.sleep(5)

# sidebutton
mybtn = driver.find_element(By.ID,"react-burger-menu-btn")
mybtn.click()
time.sleep(3)
#aboutbutn
aboutbtn = driver.find_element(By.ID,"about_sidebar_link")
aboutbtn.click()
time.sleep(3)
driver.quit()