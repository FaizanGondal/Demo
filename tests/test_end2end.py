from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
import time
from selenium.webdriver.support.wait import WebDriverWait
import pytest

from pageObject.CheckoutPage import CheckoutPage
from pageObject.ConfirmPage import Confirmpage
from pageObject.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):
    def test_end2end(self):
        logs = self.getLogger()
        homepage = HomePage(self.driver)
        # self.driver.find_element_by_link_text("Shop").click()
        checkflag = homepage.shopItem()
        # products = self.driver.find_elements_by_xpath("//div[@class= 'card h-100']")
        # checkflag = CheckoutPage(self.driver)
        products = checkflag.getCardTitles()
        logs.info("getting all the cart items")
        # //div[@class= 'card h-100']/div/h4/a
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        for product in products:
            productname = product.find_element_by_xpath("div/h4/a").text
            logs.info(productname)
            if productname == "Blackberry":
                # traverse again for the search of cart button
                # there is no need to give index if the path is unique
                time.sleep(2)
                self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
                # checkflag.getCardFooter().click()
                # you cannot handle sending xpath of child but you can handle here by fetching the all buttons
                # then put index on them and click the index you want to click
                # you have to send complete path every time.
                product.find_element_by_xpath("div/button").click()

        # self.driver.find_element_by_css_selector("a[class*='btn-primary']").click()
        self.driver.execute_script("window.scrollTo(0,0);")
        checkflag.getToCart().click()
        # self.driver.find_element_by_css_selector("a[class*='btn-primary']").click()
        time.sleep(2)

        # self.driver.find_element_by_xpath("//button[@class='btn btn-success']").click()
        final_page = checkflag.pressSuccess()

        # self.driver.find_element_by_id("country").send_keys("Pakistan")
        # final_page = Confirmpage(self.driver)
        final_page.getDelieveryTextBox().send_keys("Pakistan")
        logs.info("Entering Country name as pak")

        self.verifyLinkPresence("Pakistan")
        # self.driver.find_element_by_link_text("Pakistan").click()
        final_page.pressDropDown().click()

        # self.driver.find_element_by_xpath("//input[@class='btn btn-success btn-lg']").click()
        final_page.pressSuccess().click()

        # final = (self.driver.find_element_by_class_name("alert-success").text)
        final = (final_page.successAlert().text)
        logs.info("Text recieved  from application is "+ final)
        assert "Success!asdasdas    " in final

        # self.driver.get_screenshot_as_file("screen.png")
        final_page.takeScreenShot()
