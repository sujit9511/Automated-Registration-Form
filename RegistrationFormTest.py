from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver=webdriver.Edge('../msedgedriver.exe')


try:
    driver.get('https://sujit9511.github.io/Registration-Form/')
    driver.maximize_window()
    time.sleep(2)
    fname=driver.find_element(By.NAME,'firstName')
    time.sleep(3)
    fname.send_keys("AutoName2")
    time.sleep(2)
    lname=driver.find_element(By.ID,'lname')
    time.sleep(2)
    lname.send_keys("AutoSurname2")
    time.sleep(2)
    email=driver.find_element(By.XPATH,'//*[@id="email"]')
    time.sleep(3)
    email.send_keys("autoemail2@gmail.com")
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR,'#female').click()
    time.sleep(3)
    dropdownpath=driver.find_element(By.ID,'dropdown')
    time.sleep(3)
    select=Select(dropdownpath)
    time.sleep(2)
    select.select_by_index(2)
    time.sleep(4)
    driver.find_element(By.XPATH,'/html/body/div/div/div/form/button').click()
    time.sleep(10)


except:
    print('Error')
