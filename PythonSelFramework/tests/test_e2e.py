import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from PageObjects.CheckoutPage import CheckoutPage
from PageObjects.ConfirmPage import ConfirmPage
from PageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        checkoutpage = homepage.shopItems()
        log.info("getting all the card titles")
        products = checkoutpage.getTitles()
        for product in products:
            if product.text == "Blackberry":
                checkoutpage.getAddTocart().click()

        checkoutpage.getcheckoutbutton().click()
        confirmpage = checkoutpage.getcheckout()
        confirmpage.getCountry().send_keys("ind")
        log.info("entering country name as ind ")
        self.verifyLinkPresence("India")
        confirmpage.getcountryname().click()
        confirmpage.getCheckbox().click()
        confirmpage.getSubmitbutton().click()
        successText = confirmpage.getAlert().text
        log.info("text recieved from application" +successText)
        assert "Success! Thank you!" in successText  # we want fail test to get html report screenshot
