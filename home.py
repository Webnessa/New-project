import driver as driver
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
driver.execute_script("window.scrollBy(0, 600);")
book_selenium = driver.find_element(By.PARTIAL_LINK_TEXT,"Selenium Ruby").click()
reviews = driver.find_element(By.CLASS_NAME,"reviews_tab").click()
star_5 = driver.find_element(By.CLASS_NAME,"star-5").click()
your_review = driver.find_element(By.ID,"comment")
your_review.send_keys("Nice book!")
name = driver.find_element(By.ID,"author")
name.send_keys("Smit")
email = driver.find_element(By.ID,"email")
email.send_keys("Smit@bk.ru")
submit = driver.find_element(By.ID,"submit").click()
driver.quit()