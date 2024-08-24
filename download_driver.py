import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# Initialize the Chrome driver using WebDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())

# Open the website
driver.get("https://www.saucedemo.com/")

# Wait for 7 seconds
time.sleep(7)
