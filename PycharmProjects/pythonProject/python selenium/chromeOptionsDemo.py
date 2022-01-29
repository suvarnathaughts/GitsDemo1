from selenium import webdriver
from selenium.webdriver.chrome.service import Service
s = Service("C:\\chromedriver\\chromedriver.exe")
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("headless")
chrome_options.add_argument("--ignore-certificate-errors")

driver = webdriver.Chrome(service=s, options=chrome_options)
driver.get("http://rahulshettyacademy.com/angularpractice/")
print(driver.title)
