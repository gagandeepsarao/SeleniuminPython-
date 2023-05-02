from selenium.webdriver.common.by import By

from pageObjects import ConfirmPage


class CheckoutPage:
    def __init__(self,driver):
        self.driver = driver

    cardTitle = (By.CSS_SELECTOR,".card-title a")
    cardFooter = (By.CSS_SELECTOR, ".card-footer button")
    checkOut = (By.XPATH,"//button[@class='btn btn-success']")



    def getCardTitles(self):
        return self.driver.find_elements(*CheckoutPage.cardTitle)

    def getCardFooter(self):
        return self.driver.find_elements(*CheckoutPage.cardFooter)

    def checkOutItems(self):
        self.driver.find_element(*CheckoutPage.checkOut).click
        confirmPage = ConfirmPage(self.driver)
        return confirmPage

    #        self.driver.find_element(By.ID,"country").send_keys("ind")






