import driver as driver
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
account_menu = driver.find_element(By.ID,"menu-item-50").click()
reg_email = driver.find_element(By.ID,"reg_email")
reg_email.send_keys("Smit@bk.ru")
reg_password = driver.find_element(By.ID,"reg_password")
reg_password.send_keys("Smit.007q")
register = driver.find_element(By.CSS_SELECTOR,"[name=register]").click()
driver.quit()

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
account_menu = driver.find_element(By.ID,"menu-item-50").click()
email_address = driver.find_element(By.ID,"username")
email_address.send_keys("Smit@bk.ru")
password = driver.find_element(By.ID,"password")
password.send_keys("Smit.007qq")
login = driver.find_element(By.CSS_SELECTOR,"[name=login]").click()
if len(driver.find_elements(By.PARTIAL_LINK_TEXT,'Logout')) > 0:
    print("Элемент Logout, присутствует на странице ")
else:
    print("Элемента Logout на странице нет")
driver.quit()
