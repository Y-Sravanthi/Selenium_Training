from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(r"C:\Users\Sravanthi\Desktop\Selenium_Training\chromedriver.exe")
driver.get("https://amazon.com")
driver.maximize_window()

driver.find_element(By.XPATH,"//*[@id='nav-link-accountList']/span/span").click()
driver.find_element(By.XPATH,"//*[@id='ap_email']").send_keys("8247048507")
driver.find_element(By.XPATH,"//*[@id='continue']").click()
driver.find_element(By.XPATH,"//*[@id='ap_password']").send_keys("Sravanthi@2903")
driver.find_element(By.XPATH,"//*[@id='signInSubmit']").click()
driver.find_element(By.XPATH,"//*[@id='nav-xshop']/a[1]").click()
driver.execute_script("window.scrollTo(0,900);")
driver1=driver.find_element(By.XPATH,"//*[@id='slot-15']/div/div/div[2]/div[3]/div/div[5]/div/div/a[3]/div").click()
actions=ActionChains(driver1)
actions.move_to_element(driver1).perform()
driver.find_element(By.XPATH,"//*[@id='add-to-cart-button']").click()
actions.perform()
driver.implicitly_wait(50)
