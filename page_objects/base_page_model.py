from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


class BasePageModel:
    DEFAULT_WAIT_TIMEOUT = 5

    def __init__(self, driver) -> None:
        self._driver = driver

    def open(self):
        self._driver.get(self._url)

    def _find(self, locator, timeout=DEFAULT_WAIT_TIMEOUT) -> WebElement:
        return self._wait(timeout=timeout).until(lambda d: self._driver.find_element(*locator))
    
    def _wait(self, timeout=DEFAULT_WAIT_TIMEOUT) -> WebDriverWait:
        return WebDriverWait(self._driver, timeout=timeout)
    
    def _enter_text(self, locator, text, timeout=DEFAULT_WAIT_TIMEOUT) -> None:
        self._find(locator, timeout=timeout).send_keys(text)

    def _click(self, locator, timeout=DEFAULT_WAIT_TIMEOUT) -> None:
        self._find(locator, timeout=timeout).click()

    def _get_text(self, locator, timeout=DEFAULT_WAIT_TIMEOUT) -> str:
        return self._find(locator, timeout=timeout).text

    def _is_displayed(self, locator, timeout=DEFAULT_WAIT_TIMEOUT) -> bool:
        try:
            return self._find(locator, timeout=timeout).is_displayed()
        except NoSuchElementException:
            return False