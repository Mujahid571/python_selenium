import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Set up Chrome options
options = Options()

# Initialize the Chrome driver with options
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
# Open the website
driver.get("https://www.saucedemo.com/")

# Wait for 7 seconds
time.sleep(7)
