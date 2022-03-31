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


driver.find_element(By.XPATH,"//*[@id='twotabsearchtextbox']").send_keys("samsung mobiles new")
driver.find_element(By.XPATH,"//*[@id='nav-search-submit-button']").click()
driver.execute_script("window.scrollTo(0,730);")
driver1=driver.find_element(By.XPATH,"//*[@id='search']/div[1]/div[1]/div/span[3]/div[2]/div[4]/div/div/div/div/div/div[2]/div/div/div[1]/h2/a").click()
act=ActionChains(driver1)
act.move_to_element().click()
act.perform()
driver.implicitly_wait(50)

driver.close()
print("Test launched successfully")



#actions=ActionChains(driver1)
#actions.move_to_element(driver1).perform()
#driver.find_element(By.XPATH,"//*[@id='add-to-cart-button']").click()
#actions.perform()
#driver.implicitly_wait(50)
