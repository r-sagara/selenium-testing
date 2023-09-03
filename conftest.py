from selenium import webdriver
import pytest

BROWSER_DRIVERS = {
    "chrome": webdriver.Chrome,
    #"edge": webdriver.Edge
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
    # _driver.implicitly_wait(1)
    yield _driver
    _driver.quit()