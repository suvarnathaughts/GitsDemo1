import document as document
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
s = Service("C:\\chromedriver\\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("http://rahulshettyacademy.com/angularpractice/")
driver.find_element_by_name("name").send_keys("hello")
print(driver.find_element_by_name("name").text)
# here nothing will print
#for that we have two methods using selenium:get_attribute method, using java script driver.execute_script

print(driver.find_element_by_name("name").get_attribute("value"))

print(driver.execute_script('return document.getElementsByName("name")[0].value'))

# in same page we want to click on shop button
shopButton = driver.find_element_by_css_selector("a[href*= 'shop']")
driver.execute_script("arguments[0].click();", shopButton)
# if we want scroll down shop page it is not possible by selenium but possible with jse
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
