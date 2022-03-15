from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
driver=webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.youtube.com")

driver.find_element(By.XPATH,"//*[@id='search-form']").send_keys("Songs")
#driver.find_element(By.XPATH,"//*[@id='search-icon-legacy']").click()

