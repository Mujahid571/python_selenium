import time

from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.FirefoxOptions()
options.add_argument('--ignore-certificate-errors')  # Optional: Add any additional options you need
driver = webdriver.Firefox(options=options)
driver.get('https://www.saucedemo.com/')
driver.maximize_window()
