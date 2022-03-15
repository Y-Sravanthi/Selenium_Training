from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(r"C:\Users\Sravanthi\Desktop\Selenium_Training\chromedriver.exe")
driver.get("https://hotstar.com")
driver.find_element(By.XPATH,"//*[@id='searchField']").send_keys("Sports")
#driver.find_element(By.XPATH,"//*[@id='app']/div/div/div[1]/div[1]/div/div[2]/div/div[4]/div[2]/div[1]/article").click()
driver.implicitly_wait(10)
driver.close()
#driver.find_element(By.XPATH,"//*[@id='app']/div/div/div[1]/div[1]/div/div[2]/div/div[4]/div[2]/div[1]/article/a").click()
