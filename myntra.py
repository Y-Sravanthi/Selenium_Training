from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(r"C:\Users\Sravanthi\Desktop\Selenium_Training\chromedriver.exe")
driver.get("https://www.myntra.com")
driver.maximize_window()
driver.find_element(By.XPATH,"//*[@id='desktop-header-cnt']/div[2]/nav/div/div[2]/div").click()
