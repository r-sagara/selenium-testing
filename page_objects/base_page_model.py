from typing import Union
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

    def _find(self, locator, timeout=DEFAULT_WAIT_TIMEOUT) -> Union[WebElement, bool]:
        return self._wait_for_visibility(locator, timeout=timeout)
    
    def _wait_for_visibility(self, locator, timeout=DEFAULT_WAIT_TIMEOUT, custom_msg="") -> Union[WebElement, bool]:
        msg = custom_msg if custom_msg else f"Element visibility by locator ({locator}) is not waited in a given timeout ({timeout})"
        return self._wait(timeout=timeout).until(EC.visibility_of_element_located(locator), message=msg)

    def _wait_for_invisibility(self, locator, timeout=DEFAULT_WAIT_TIMEOUT, custom_msg="") -> Union[WebElement, bool]:
        msg = custom_msg if custom_msg else f"Element invisibility by locator ({locator}) is not waited in a given timeout ({timeout})"
        return self._wait(timeout=timeout).until(EC.invisibility_of_element_located(locator), message=msg)

    def _wait(self, timeout=DEFAULT_WAIT_TIMEOUT) -> WebDriverWait:
        return WebDriverWait(self._driver, timeout=timeout)
    
    def _enter_text(self, locator, text, timeout=DEFAULT_WAIT_TIMEOUT) -> None:
        self._find(locator, timeout=timeout).send_keys(text)

    def _click(self, locator, timeout=DEFAULT_WAIT_TIMEOUT) -> None:
        self._find(locator, timeout=timeout).click()

    def _get_text(self, locator, timeout=DEFAULT_WAIT_TIMEOUT) -> str:
        return self._find(locator, timeout=timeout).text
    
    def _wait_to_be_enabled(self, locator, timeout=DEFAULT_WAIT_TIMEOUT):
        self._wait(timeout=timeout).until(lambda d: self._find(locator).is_enabled())

    def _clear(self, locator, timeout=DEFAULT_WAIT_TIMEOUT):
        self._find(locator, timeout=timeout).clear()