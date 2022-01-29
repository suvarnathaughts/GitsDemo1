from selenium.webdriver.common.by import By

from PageObjects.ConfirmPage import ConfirmPage


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
    CardTitles = (By.XPATH, "//div[@class= 'card h-100']/div/h4/a")
    AddToCart = (By.XPATH, "//div[@class= 'card h-100']/div/button")
    checkoutButton = (By.CSS_SELECTOR, "a[class*='btn-primary']")
    Checkout = (By.XPATH, "//button[@class= 'btn btn-success']")

    def getTitles(self):
        return self.driver.find_elements(*CheckoutPage.CardTitles)

    def getAddTocart(self):
        return self.driver.find_element(*CheckoutPage.AddToCart)

    def getcheckoutbutton(self):
        return self.driver.find_element(*CheckoutPage.checkoutButton)

    def getcheckout(self):
        self.driver.find_element(*CheckoutPage.Checkout).click()
        confirmpage = ConfirmPage(self.driver)
        return confirmpage



