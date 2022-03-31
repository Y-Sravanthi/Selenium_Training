import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(r"C:\Users\Sravanthi\Desktop\Selenium_Training\chromedriver.exe")

driver.get("http://demo.automationtesting.in/Windows.html")
driver.maximize_window()

print(driver.title)        # return tile of the page
print(driver.current_url)  # return url

driver.find_element(By.XPATH,"//*[@id='Tabbed']/a/button").click()
time.sleep(5)
#driver.close()

driver.quit()

