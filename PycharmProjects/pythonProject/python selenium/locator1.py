import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select

s = Service("C:\\chromedriver\\chromedriver.exe")
driver = webdriver.Chrome(service = s)
#driver.get("https://rahulshettyacademy.com/angularpractice/")
# driver.find_element_by_name("name").send_keys("rahul")   # to find web element using Name locator
#driver.find_element_by_id("exampleCheck1").click()       # to find web element using id locator
#driver.find_element_by_name("email").send_keys("shetty")   # here we use Name locator for email box
#driver.find_element_by_css_selector("input[name = 'name']").send_keys("suvarna")  #here we use css selector for name box
#driver.find_element_by_xpath("//input[@type = 'submit']").click()
#print(driver.find_element_by_class_name("alert-success").text)
#dropdown = Select(driver.find_element_by_id("exampleFormControlSelect1"))
# first method to select from dropdown is by visible text
#dropdown.select_by_visible_text("female")    it shows exception error
#dropdown.select_by_index(1)
#dropdown.select_by_visible_text("Male")
#if we want to check wether "success" is present or not without giving  print(driver.find_element_by_class_name("alert-success").text)
#here we need to use assert  method
#message = driver.find_element_by_class_name("alert-success").text
#assert "success" in message
# here process is finished with exit code 0 means success is present
# now how to handle autosuggestive dropdown
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.find_element_by_id("autosuggest").send_keys("Ind")
time.sleep(2)
countries = driver.find_elements_by_css_selector("li[class='ui-menu-item'] a")
len(countries)
for country in countries:
    if country.text == "India":
        country.click()
        break
# now to validate that correct option is selected without reloading and print
assert driver.find_element_by_id("autosuggest").get_attribute('value') == "India"







