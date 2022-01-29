from selenium import webdriver
from selenium.webdriver.chrome.service import Service
s = Service("C://chromedriver//chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element_by_link_text("Click Here").click()
# here to get element from new window we have to switch to that window first
# we can switch with id, how to get child id,[1] is the index of child window ['paerentid','childid'] in handles stored
childWINDOW = driver.window_handles[1]
driver.switch_to.window(childWINDOW)
print(driver.find_element_by_tag_name("h3").text)
driver.close()
#if we want to come back on parent window then again switch to parent window having index[0]
driver.switch_to.window(driver.window_handles[0])
print(driver.find_element_by_tag_name("h3").text)
assert "Opening a new window" == driver.find_element_by_tag_name("h3").text

