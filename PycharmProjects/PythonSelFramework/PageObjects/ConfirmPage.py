from selenium.webdriver.common.by import By


class ConfirmPage:
    def __init__(self, driver):
        self.driver = driver

    country = (By.ID, "country")
    countryName = (By.LINK_TEXT, "India")
    checkbox = (By.XPATH, "//div[@class = 'checkbox checkbox-primary']")
    submitButton = (By.CSS_SELECTOR, "input[type = 'submit']")
    alert = (By.CLASS_NAME, "alert-success")

    def getCountry(self):
        return self.driver.find_element(*ConfirmPage.country)

    def getcountryname(self):
        return self.driver.find_element(*ConfirmPage.countryName)

    def getCheckbox(self):
        return self.driver.find_element(*ConfirmPage.checkbox)

    def getSubmitbutton(self):
        return self.driver.find_element(*ConfirmPage.submitButton)

    def getAlert(self):
        return self.driver.find_element(*ConfirmPage.alert)



