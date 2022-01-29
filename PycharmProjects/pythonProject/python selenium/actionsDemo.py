from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
s= Service("C:\\chromedriver\\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# for mouse hover first create object for ActionChains class
action = ActionChains(driver)
menu = driver.find_element_by_id("mousehover")
action.move_to_element(menu).perform()
# now we want to select Top and click on it, we can do it by driver or by action
#childmenu = driver.find_element_by_link_text("Top")
childmenu = driver.find_element_by_link_text("Reload")
action.move_to_element(childmenu).click().perform()
