# how to handle alert
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
s = Service("C:\\chromedriver\\chromedriver.exe")
driver = webdriver.Chrome(service = s)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element_by_css_selector("#name").send_keys("Option3")    # this is the step to write in edit box
driver.find_element_by_id("alertbtn").click()     #this is the step to click on the alert button
alert = driver.switch_to.alert  #alert is adriver which handle java popups
print(alert.text)
alert.accept()



