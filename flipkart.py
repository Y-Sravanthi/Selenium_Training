from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Firefox(executable_path="C:\\Users\\Sravanthi\\Desktop\\Selenium_Training\\geckodriver.exe")
driver.get("https://www.flipkart.com")
driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div/div/div[2]/div/form/div[1]/input").send_keys("8247048507")
driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div/div/div[2]/div/form/div[2]/input").send_keys("Sravanthi@2903")
driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div/div/div[2]/div/form/div[4]/button").click()
driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div/div/div[3]/a/div[1]/div/img").click()

driver=driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div/div/div[3]/a/div[1]/div/img")
driver.execute_script("window.scrollTo(0,750);")
actions=ActionChains(driver)
actions.move_to_element(driver)
driver.find_element(By.XPATH,"/html/body/div/div/div[3]/div[6]/div/div[1]/a/div").click()

driver.implicitly_wait(70)
driver.close()
