import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
list_a = []
list_b = []
s = Service("C:\\chromedriver\\chromedriver.exe")
driver = webdriver.Chrome(service = s)
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/")
driver.find_element_by_css_selector("input.search-keyword").send_keys("ber")
# here after typing ber it take 2 or 3 sec to dispaly result so we use python time sleep
time.sleep(4)
count = len(driver.find_elements_by_xpath("//div[@class = 'products']/div"))
assert count == 3

veggies = driver.find_elements_by_xpath("//div[@class = 'products']/div/h4")
for veg in veggies:
    list_a.append(veg.text)
print(list_a)

time.sleep(3)

buttons = driver.find_elements_by_xpath("//div[@class = 'product-action']/button")
for button in buttons:
    button.click()

driver.find_element_by_css_selector("img[alt = 'Cart']").click()
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/header[1]/div[1]/div[3]/div[2]/div[2]/button[1]").click()

vegetables = driver.find_elements_by_css_selector("p.product-name")
for vegetable in vegetables:
    if vegetable.text != '':
        list_b.append(vegetable.text)
print(list_b)
assert list_a == list_b

driver.find_element_by_class_name("promocode").send_keys("rahulshettyacademy")
driver.find_element_by_class_name("promoBtn").click()
print(driver.find_element_by_css_selector("span.promoInfo").text)