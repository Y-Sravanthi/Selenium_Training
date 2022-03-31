import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(r"C:\Users\Sravanthi\Desktop\Selenium_Training\chromedriver.exe")

driver.get("https://petstore.octoperf.com/actions/Catalog.action")
driver.maximize_window()

print(driver.title)
print(driver.current_url)

fish=driver.find_element(By.XPATH,"//*[@id='SidebarContent']/a[1]").click()
#driver.find_element(By.XPATH,"//*[@id='BackLink']/a").click()
#dogs=driver.find_element(By.XPATH,"//*[@id='SidebarContent']/a[2]").click()
driver.find_element(By.XPATH,"//*[@id='Catalog']/table/tbody/tr[2]/td[1]/a").click()
driver.find_element(By.XPATH,"//*[@id='Catalog']/table/tbody/tr[2]/td[1]/a").click()
driver.find_element(By.XPATH,"//*[@id='Catalog']/table/tbody/tr[7]/td/a").click()
driver.find_element(By.XPATH,"//*[@id='Cart']/form/table/tbody/tr[2]/td[5]/input").send_keys()
driver.find_element(By.XPATH,"//*[@id='Cart']/a").click()
time.sleep(30)
driver.close()
