import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')  # Optional: Add any additional options you need
driver = webdriver.Chrome(options=options)
driver.get("https://the-internet.herokuapp.com/hovers")
driver.maximize_window()

hover = driver.find_element(By.XPATH,'//*[@id="content"]/div/div[3]/img')
actions = ActionChains(driver)
actions.move_to_element(hover).perform()
time.sleep(3)
driver.find_element(By.XPATH,'//*[@id="content"]/div/div[3]/div/a').click()
time.sleep(3)
