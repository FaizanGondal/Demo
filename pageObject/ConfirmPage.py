from selenium.webdriver.common.by import By


class Confirmpage:
    def __init__(self, driver):
        self.driver = driver

    delieveryText = (By.ID, "country")
    # self.driver.find_element_by_id("country").send_keys("Pakistan")

    findDropDown = (By.LINK_TEXT, "Pakistan")
    # self.driver.find_element_by_link_text("Pakistan").click()

    Successbtn = (By.XPATH, "//input[@class='btn btn-success btn-lg']")
    # self.driver.find_element_by_xpath("//input[@class='btn btn-success btn-lg']").click()

    successAlertbtn = (By.CLASS_NAME, "alert-success")

    # final = (self.driver.find_element_by_class_name("alert-success").text)

    def getDelieveryTextBox(self):
        return self.driver.find_element(*Confirmpage.delieveryText)

    def pressDropDown(self):
        return self.driver.find_element(*Confirmpage.findDropDown)

    def pressSuccess(self):
        return self.driver.find_element(*Confirmpage.Successbtn)

    def successAlert(self):
        return self.driver.find_element(*Confirmpage.successAlertbtn)

    def takeScreenShot(self):
        self.driver.get_screenshot_as_file("screen.png")
