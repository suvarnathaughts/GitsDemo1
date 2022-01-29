from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

s = Service("C:\\chromedriver\\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("http://rahulshettyacademy.com/angularpractice/")
driver.find_element_by_css_selector("a[href*= 'shop']").click()
products = driver.find_elements_by_xpath("//div[@class= 'card h-100']/div/h4/a")
for product in products:
    if product.text == "Blackberry":
        driver.find_element_by_xpath("//div[@class= 'card h-100']/div/button").click()

driver.find_element_by_css_selector("a[class*='btn-primary']").click()
driver.find_element_by_xpath("//button[@class= 'btn btn-success']").click()
driver.find_element_by_id("country").send_keys("ind")
wait = WebDriverWait(driver, 7)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
driver.find_element_by_link_text("India").click()
driver.find_element_by_xpath("//div[@class = 'checkbox checkbox-primary']").click()
driver.find_element_by_css_selector("input[type = 'submit']").click()
#print(driver.find_element_by_class_name("alert-success").text)
successText = driver.find_element_by_class_name("alert-success").text
assert "Success! Thank you!" in successText
# how to take screenshot using selenium python
driver.get_screenshot_as_file("screen.png")










