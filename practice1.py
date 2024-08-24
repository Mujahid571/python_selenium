import time

from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')  # Optional: Add any additional options you need
driver = webdriver.Chrome(options=options)
driver.get("https://practicetestautomation.com/practice/")
driver.maximize_window()
time.sleep(3)
myclick=driver.find_element(By.LINK_TEXT,"Test Login Page")
myclick.click()
time.sleep(2)
myuser = driver.find_element(By.ID,"username")
myuser.send_keys("student")
time.sleep(3)
mypass = driver.find_element(By.ID,"password")
mypass.send_keys("Password123")
time.sleep(3)
mybtn = driver.find_element(By.ID,"submit")
mybtn.click()
time.sleep(4)