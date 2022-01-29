from selenium import webdriver
from selenium.webdriver.chrome.service import Service
s = Service("C:\\chromedriver\\chromedriver.exe")
driver = webdriver.Chrome(service = s)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element_by_css_selector("#name").send_keys("Option3")
driver.find_element_by_id("confirmbtn").click()
alert = driver.switch_to.alert
print(alert.text)
alert.accept()