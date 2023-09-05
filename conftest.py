from selenium import webdriver
from page_objects.exceptions_page import ExceptionsPageModel
from page_objects.login_page import LoginPageModel
from page_objects.account_page import AccountPageModel
import pytest


BROWSER_DRIVERS = {
    "chrome": webdriver.Chrome,
    "edge": webdriver.Edge
}

def pytest_addoption(parser):
    parser.addoption(
        "--browser", 
        action="store",
        default="chrome",
        help="Run tests with specified browser",
        choices=tuple(BROWSER_DRIVERS.keys())
    )

@pytest.fixture(scope='function', params=list(BROWSER_DRIVERS.keys()))
def driver(request):
    # driver_option = request.config.getoption("--browser")
    _driver = BROWSER_DRIVERS[request.param]()
    yield _driver
    _driver.quit()

@pytest.fixture
def LoginPage(driver):
    page = LoginPageModel(driver)
    yield page

@pytest.fixture
def AccountPage(driver):
    page = AccountPageModel(driver)
    yield page

def ExceptionsPage(driver):
    page = ExceptionsPageModel(driver)
    yield page