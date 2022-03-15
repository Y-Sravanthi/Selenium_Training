from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(r"C:\Users\Sravanthi\Desktop\Selenium_Training\chromedriver.exe")
driver.get("https://www.phptravels.net/login")
driver.maximize_window()
driver.find_element(By.XPATH,"//*[@id='fadein']/div[1]/div/div[2]/div[2]/div/form/div[1]/div/span").send_keys("user@phptravels.com")
driver.find_element(By.XPATH,"//*[@id='fadein']/div[1]/div/div[2]/div[2]/div/form/div[2]/div[1]/input").send_keys("demouser")
driver.find_element(By.XPATH,"//*[@id='fadein']/div[1]/div/div[2]/div[2]/div/form/div[3]/button").click()