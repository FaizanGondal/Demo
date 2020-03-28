import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseClass:
    def verifyLinkPresence(self, text):
        wait = WebDriverWait(self.driver, 7)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, text)))

    def getLogger(self):
        loggername = inspect.stack()[1][3]  ## in order to enter the name of file not of where it is called
        logger = logging.getLogger(loggername)
        fileHandler = logging.FileHandler('logfile.log')
        logger.addHandler(fileHandler)  ## filehandler object into it

        formatter = logging.Formatter(
            "%(asctime)s :%(levelname)s : %(name)s :%(message)s ")  # % is given to wrapp and evaluate the variable on runtime

        fileHandler.setFormatter(formatter)

        logger.setLevel(logging.DEBUG)  ## set level from where the logs will print the messages.
        return logger
