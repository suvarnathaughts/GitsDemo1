from selenium import webdriver
from selenium.webdriver.chrome.service import Service
s= Service("C:\\chromedriver\\chromedriver.exe")
driver = webdriver.Chrome(service = s)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
Checkboxes = driver.find_elements_by_xpath("//input[@type = 'checkbox']")
print(len(Checkboxes))
#for Checkbox in Checkboxes:
    #Checkbox.click()
    #assert Checkbox.is_selected()    #  it will click all checkboxex whatever the no. is

# now if you want to select only one option for e.g option2 , then we can use id, name and then click but
#there is generic method but in this we can use condition
#in option2 html properties we have value = option2
#if we grab value attribute we can check option2 is present or not and click method
for Checkbox in Checkboxes:
    if Checkbox.get_attribute("value") == "option1":
        Checkbox.click()
        assert Checkbox.is_selected()

# for radio buttons
#radiobuttons = driver.find_elements_by_name("radioButton")
#radiobuttons[2].click()           #[2] is index because it is list
#assert radiobuttons[2].is_selected()

# new topic "is_displayed" from lecture no.64
assert driver.find_element_by_id("displayed-text").is_displayed()
# we want go on hide button and click
driver.find_element_by_id("hide-textbox").click()
assert not driver.find_element_by_id("displayed-text").is_displayed()






