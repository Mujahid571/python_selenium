import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')  # Optional: Add any additional options you need
driver = webdriver.Chrome(options=options)
driver.get("https://elementalselenium.com/")
driver.maximize_window()
# take a screenshort of whole page
#driver.save_screenshot("mypic.png")

# take screen short of specific parts
my_section = driver.find_element(By.XPATH,'//*[@id="__docusaurus"]/footer')
my_section.screenshot("copmany.png")
time.sleep(3)
driver.quit()