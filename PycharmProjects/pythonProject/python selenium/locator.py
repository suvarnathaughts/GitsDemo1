from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


s = Service("C:\\chromedriver\\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("http://rahulshettyacademy.com/angularpractice/")
form_textfield = driver.find_element(By.NAME, 'Name')
form_textfield.send_keys("rahul")

