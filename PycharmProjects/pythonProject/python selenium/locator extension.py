from selenium import webdriver
from selenium.webdriver.chrome.service import Service
s = Service("C:\\chromedriver\\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://login.salesforce.com/")
#driver.find_element_by_id("username").send_keys("rahul")
#driver.find_element_by_id("username").clear()
  # how to generate css from id : syntax: tagname#id
#driver.find_element_by_css_selector("input#username").send_keys("rahul")
   # tagname is optional if we dont use it there will be no problem
#driver.find_element_by_css_selector("#username").clear()
   # how to generate css from class name syntax:tagname.classname
driver.find_element_by_css_selector("input.password").send_keys("lohit")
# use of link test locator
driver.find_element_by_link_text("Forgot Your Password?").click()
# generating xpath based on text syntax://tagname[text()='xxx']
#driver.find_element_by_xpath("//input[text()='Cancel']").click()    # it shows some error
driver.find_element_by_xpath("//input[@type= 'button']").click()    # now it is correct
#print(driver.find_element_by_xpath("//form[@name = 'login']/div[1]/label").text)
print(driver.find_element_by_css_selector("form[name= 'login'] label:nth-child(3)").text)






