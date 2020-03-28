from selenium.webdriver.common.by import By

from pageObject.CheckoutPage import CheckoutPage


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    shop = (By.LINK_TEXT, "Shop")
    name = (By.NAME, "name")
    password = (By.ID,"exampleInputPassword1")

    def shopItem(self):
        self.driver.find_element(*HomePage.shop).click()  # star is added to deserialize the shop object into the form written below, will be treat as tuple
        checkflag = CheckoutPage(self.driver)
        return checkflag
        # self.driver.find_element_by_link_text("Shop").click()

    def getName(self):
        return self.driver.find_element(*HomePage.name)


    def getPasswordLocator(self):
        return  self.driver.find_element(*HomePage.password)