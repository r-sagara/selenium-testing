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
        choices=(*BROWSER_DRIVERS.keys(), "all")
    )

def pytest_generate_tests(metafunc):
    fixture_name = 'driver'
    if fixture_name in metafunc.fixturenames:
        driver_option = metafunc.config.getoption("--browser")
        parameters = [*BROWSER_DRIVERS.keys()] if driver_option == "all" else [driver_option]
        metafunc.parametrize(fixture_name, parameters, scope="function", indirect=True)

@pytest.fixture(scope='function')
def driver(request):
    _driver = BROWSER_DRIVERS[request.param]()
    yield _driver
    _driver.quit()

@pytest.fixture
def LoginPage(driver):
    page = LoginPageModel(driver)
    page.open()
    yield page

@pytest.fixture
def AccountPage(driver):
    page = AccountPageModel(driver)
    yield page

@pytest.fixture
def ExceptionsPage(driver):
    page = ExceptionsPageModel(driver)
    page.open()
    yield page