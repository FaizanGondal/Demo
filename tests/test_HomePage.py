from selenium import webdriver
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.select import Select

from TestData.HomePageData import HomePageData
from pageObject.HomePage import HomePage
from utilities.BaseClass import BaseClass
import pytest


class TestHomePage(BaseClass):
        # adding lines for git testing
    def test_formSubmission(self, getData):
        logs = self.getLogger()
        homepage = HomePage(self.driver)
        logs.info("first name is " + getData["FirstName"])
        homepage.getName().send_keys(getData["FirstName"])
        # driver.find_element_by_name("name").send_keys("AbC")
        homepage.getPasswordLocator().send_keys(getData["LastName"])
        # driver.find_element_by_id("exampleInputPassword1").send_keys("1223")
        self.driver.find_element_by_id("exampleCheck1").click()
        self.driver.find_element_by_xpath("//input[@type='submit']").click()
        print(self.driver.find_element_by_class_name("alert-success").text)

        # Select class for drop downs
        dropdown = Select(self.driver.find_element_by_id("exampleFormControlSelect1"))
        dropdown.select_by_visible_text(getData["Gender"])
        # dropdown.select_by_index(0)
        ## value is fetched if value is given as an attribute in the html tag
        # dropdown.select_by_value()
        self.driver.find_element_by_xpath("//input[@value='Submit']").click()

        alertText = self.driver.find_element_by_xpath("//div[@class='alert alert-success alert-dismissible']").text
        assert ("Success" in alertText)
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.getTestData("testcase2"))  # each tuple will be treated as one test case
    def getData(self, request):
        return request.param
