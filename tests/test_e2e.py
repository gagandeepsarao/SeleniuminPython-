import pytest
from selenium import webdriver
import time


from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pageObjects.CheckoutPage import CheckoutPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        checkOutPage = homepage.shopItems()
        cards = checkOutPage.getCardTitles()
        log.info("Getting all the card titles")
        i = -1
        for card in cards:
            i = i + 1
            cardText = card.text
            log.info(cardText)
            if cardText == "Blackberry":
                checkOutPage.getCardFooter()[i].click()

        self.driver.find_element(By.CSS_SELECTOR,"a[class*='btn-primary']").click()

        confirmPage = checkOutPage.checkOutItems()
        log.info("Entering country name as ind")
        self.driver.find_element(By.ID,"country").send_keys("ind")
        time.sleep(5)
        self.verifyLinkPresence("Ind")


        self.driver.find_element(By.LINK_TEXT,"India").click()
        self.driver.find_element(By.XPATH,"//div[@class='checkbox checkbox-primary']").click()
        self.driver.find_element(By.CSS_SELECTOR,"[type='submit']").click()
        textMatch = self.driver.find_element(By.CSS_SELECTOR,"[class*='alert-success']").text
        log.info("Text received from application is "+textMatch)

        assert ("Success! Thank you!" in textMatch)
