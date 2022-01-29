from selenium import webdriver
from selenium.webdriver.chrome.service import Service

s = Service("C:\\chromedriver\\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.get("http://rahulshettyacademy.com/")
print(driver.title)
print(driver.current_url) # it shows the same website means it is not hacked
driver.get("http://rahulshettyacademy.com/AutomationPractice")
driver.minimize_window()
driver.back()# to comeback on our previous url http://rahulshettyacademy.com/"
driver.refresh() # it same like we reload the page again
driver.close() # it is to close the browser that invoke inthis only current window will close



