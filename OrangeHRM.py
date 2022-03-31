

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(r"C:\Users\Sravanthi\Desktop\Selenium_Training\chromedriver.exe")

driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()

driver.find_element(By.XPATH,"//*[@id='txtUsername']").send_keys("Admin")
driver.find_element(By.XPATH,"//*[@id='txtPassword']").send_keys("admin123")
driver.find_element(By.XPATH,"//*[@id='btnLogin']").click()

admin=driver.find_element(By.XPATH,"//*[@id='menu_admin_viewAdminModule']")
usermgmt=driver.find_element(By.XPATH, "//*[@id='menu_admin_UserManagement']")
user=driver.find_element(By.XPATH,"//*[@id='menu_admin_viewSystemUsers']")

actions=ActionChains(driver)

actions.move_to_element(admin).move_to_element(usermgmt).move_to_element(user).click().perform()
driver.implicitly_wait(60)
driver.close()
#driver.quit()
print("Actionschains functionality performed")