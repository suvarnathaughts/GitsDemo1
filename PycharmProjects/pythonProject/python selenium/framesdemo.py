import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
s = Service("C://chromedriver//chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://the-internet.herokuapp.com/iframe")
driver.switch_to.frame("mce_0_ifr")
time.sleep(3)
driver.find_element_by_css_selector("#tinymce").clear()
driver.find_element_by_css_selector("#tinymce").send_keys("i am able to automate")
# if we want to grab the text An iFrame containing the TinyMCE WYSIWYG Editor which is not in frame
# then switch back to default content
driver.switch_to.default_content()
print(driver.find_element_by_tag_name("h3").text)