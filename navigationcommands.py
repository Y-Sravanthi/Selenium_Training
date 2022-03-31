from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(r"C:\Users\Sravanthi\Desktop\Selenium_Training\chromedriver.exe")

driver.get("https://demo.guru99.com/test/newtours/")
print(driver.title)

driver.get("https://petstore.octoperf.com/actions/Catalog.action")
print(driver.title)

driver.back()
print(driver.title)

driver.forward()
print(driver.title)
driver.implicitly_wait(10)
driver.close()
print("Successfully performed navigation commands!!!")

