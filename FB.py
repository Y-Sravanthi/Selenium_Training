from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(r"C:\Users\Sravanthi\Desktop\Selenium_Training\chromedriver.exe")
driver.get("https://www.facebook.com")
driver.find_element(By.XPATH,"//*[@id='email']").send_keys("vishnuaabb@gmail.com")
driver.find_element(By.XPATH,"//*[@id='pass']").send_keys("Visravs@290301")
driver.find_element(By.NAME,"login").click()

