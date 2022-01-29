from selenium import webdriver
from selenium.webdriver.chrome.service import Service
s = Service("C:\\chromedriver\\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("http://rahulshettyacademy.com/")
