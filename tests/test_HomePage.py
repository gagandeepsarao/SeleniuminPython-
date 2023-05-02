from selenium.webdriver.support.select import Select
from selenium import webdriver
import pytest

from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):
    def test_formSubmission(self, getData):

        homePage = HomePage(self.driver)
        homePage.getName().send_keys(getData["firstname"])
        homePage.getEmail().send_keys(getData["Email"])
        homePage.getCheckBox().click()
        self.selectOptionByText(homePage.getGender(), getData["Gender"])
        homePage.submitForm().click()

        alertText = homePage.getSuccessMessage().text

        assert ("Success" in alertText)
        self.driver.refresh()


    @pytest.fixture(params= HomePageData.test_HomePage_data)
    def getData(self,request):
            return request.param




