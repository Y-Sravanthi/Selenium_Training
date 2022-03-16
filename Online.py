from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(r"C:\Users\Sravanthi\Desktop\Selenium_Training\chromedriver.exe")
try:
    driver.get("http://automationpractice.com/index.php")
    driver.maximize_window()
    driver.execute_script("window.scrollTo(0,750);")

    driver1=driver.find_element(By.XPATH,"//*[@id='center_column']/ul/li/div/div[2]/h5/a")
    actions=ActionChains(driver)
    actions.move_to_element(driver1).perform()
    driver2=driver.find_element(By.XPATH,"//*[@id='center_column']/ul/li/div/div[2]/div[2]/a[1]").click()
    #actions.click(driver2)
    actions.perform()
    driver.find_element(By.XPATH,"//*[@id='layer_cart']/div[1]/div[2]/div[4]/a").click()
except Exception():
    print("Fail in something")
finally:
    driver.close()

#driver.implicitly_wait(30)

#driver.find_element(By.XPATH,"//*[@i//*[@id='center_column']/ul/li[7]/div/div[2]/h5/a").click()
#driver.find_element(By.XPATH,"//*[@id='subcategories']/ul/li[1]/h5/a").click()