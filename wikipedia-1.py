import time

from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')  # Optional: Add any additional options you need
driver = webdriver.Chrome(options=options)
driver.get('https://www.wikipedia.org/')
driver.maximize_window()
time.sleep(5)
option_tag = driver.find_elements(By.TAG_NAME,'option')
for i in option_tag:
    print("text is ",i.text, " the language is ",i.get_attribute("lang"))
print(len(option_tag))