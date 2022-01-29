import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select

from PageObjects.HomePage import HomePage
from TestData.test_HomePage_data import HomePageData
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formsubmission(self, getData):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        log.info("first name is" + getData["firstname"])
        homepage.getName().send_keys(getData["firstname"])
        homepage.getEmail().send_keys(getData["lastname"])
        homepage.getCheckbox().click()
        dropdown = Select(homepage.getGender())
        dropdown.select_by_visible_text(getData["gender"])
        homepage.getSubmitForm().click()
        message = homepage.getSuccessMessage().text
        assert ("success" in message)
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.getTestData("Testcase2"))
    def getData(self, request):
        return request.param
