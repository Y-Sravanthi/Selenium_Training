from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(r"C:\Users\Sravanthi\Desktop\Selenium_Training\chromedriver.exe")
driver.get("https://jt-dev.azurewebsites.net/#/SignUp")
driver.find_element(By.XPATH,"//*[@id='language']/div[1]/span/span[2]/span").send_keys("English")
driver.find_element(By.XPATH,"//*[@id='name']").send_keys("Sravanthi")

#time.sleep(10)
#driver.close()


