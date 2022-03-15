import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(r"C:\Users\Sravanthi\Desktop\Selenium_Training\chromedriver.exe")
driver.get("https://www.google.com")
driver.maximize_window()
driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input").send_keys("whatsappweb")

driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]").click()
driver.find_element(By.XPATH,"//*[@id='rso']/div[1]/div/div/div/div/div/div/div[1]/a").click()

time.sleep(300)
driver.find_element(By.XPATH,"//*[@id='pane-side']/div[2]/div/div/div[11]/div/div/div[2]/div[1]/div[1]/span").click()
driver.find_element(By.XPATH,"//*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]").send_keys("Python Testing")
driver.close()
