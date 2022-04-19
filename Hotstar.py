from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(r"C:\Users\Sravanthi\Desktop\Selenium_Training\chromedriver.exe")
driver.get("https://google.com")
driver.maximize_window()
print(driver.title)
driver.find_element(By.XPATH,"//*[@id='inputWrapper']").send_keys("naveenautomationlabs")
driver.implicitly_wait(20)

driver.quit()
