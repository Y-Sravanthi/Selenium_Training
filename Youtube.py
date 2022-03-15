from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(r"C:\Users\Sravanthi\Desktop\Selenium_Training\chromedriver.exe")
driver.get("https://youtube.com")
driver.find_element(By.XPATH,"//*[@id='text']").send_keys("Songs")

