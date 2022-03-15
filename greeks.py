from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://demoqa.com/selectable")
list1=driver.find_element(By.XPATH,"//*[@id='verticalListContainer']/li[1]")
list2=driver.find_element(By.XPATH,"//*[@id='verticalListContainer']/li[2]")
list3=driver.find_element(By.XPATH,"//*[@id='verticalListContainer']/li[3]")
list4=driver.find_element(By.XPATH,"//*[@id='verticalListContainer']/li[4]")
actions=ActionChains(driver)
actions.click(list1)
actions.click(list2)
actions.click(list3)
actions.click(list4)
actions.perform()

