from selenium.webdriver.common.by import By

from pageObject.ConfirmPage import Confirmpage


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    cardTitle = (By.XPATH, "//div[@class= 'card h-100']")
    # products = self.driver.find_elements_by_xpath("//div[@class= 'card h-100']")

    cardFooter = (By.XPATH, "div/button")
    # product.find_element_by_xpath("div/button").click()

    cardCartbtn = (By.CSS_SELECTOR, "a[class*='btn-primary']")
    # self.driver.find_element_by_css_selector("a[class*='btn-primary']").click()

    cardSuccessbtn = (By.XPATH, "//button[@class='btn btn-success']")

    # self.driver.find_element_by_xpath("//button[@class='btn btn-success']").click()

    def getCardTitles(self):
        return self.driver.find_elements(*CheckoutPage.cardTitle)

    # return self.driver.find_elements_by_xpath("//div[@class= 'card h-100']")

    def getCardFooter(self):
        return self.driver.find_element(*CheckoutPage.cardFooter)

    def getToCart(self):
        return self.driver.find_element(*CheckoutPage.cardCartbtn)

    def pressSuccess(self):
        self.driver.find_element(*CheckoutPage.cardSuccessbtn).click()
        final_page = Confirmpage(self.driver)
        return final_page
