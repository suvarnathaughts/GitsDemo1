from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select

s = Service("C:\\chromedriver\\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
driver.find_element_by_css_selector("input[name = 'name']").send_keys("Rahul")
driver.find_element_by_name("email").send_keys("shetty")
driver.find_element_by_id("exampleCheck1").click()
dropdown = Select(driver.find_element_by_id("exampleFormControlSelect1"))
dropdown.select_by_visible_text("Male")
driver.find_element_by_xpath("//input[@type = 'submit']").click()
message = driver.find_element_by_class_name("alert-success").text
assert ("success" in message)
