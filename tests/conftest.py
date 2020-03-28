import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
import time

from selenium.webdriver.support.wait import WebDriverWait

driver = None


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="firefox"
    )


@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == "firefox":
        firefox_options = webdriver.FirefoxOptions()
        firefox_options.add_argument("start-maximized")
        driver = webdriver.Firefox(executable_path="D:\\OneDrive\\geckodriver-v0.26.0-win64\\geckodriver.exe",
                                   options=firefox_options)
    elif browser_name == "Chrome":
        driver = webdriver.Chrome(executable_path="D:\\OneDrive\\chromedriver_win32(1)\\chromedriver.exe")

    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()  ## to tear down the driver at the end
    ## return driver return the driver like this is not a good practice so employ the request object for this job


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
    Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
    :param item:
    :return:
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            filename = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(filename)
            if filename:
                html = '<div><img src="%s" alt="screenshot" style= "width:304px;height:228px" ' \
                       ' onclick="window.open(this.src)" align="right" /></div>' % filename
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)
