import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(r"C:\Users\Sravanthi\Desktop\Selenium_Training\chromedriver.exe")

driver.get("https://google.com")
print(driver.title)
driver.find_element(By.NAME,"q").send_keys("Naveenautomationlabs")
optionlist=driver.find_element(By.CSS_SELECTOR,"")
print(len(optionlist))

for ele in optionlist:
    print(ele)

time.sleep(10)
#driver.quit()

