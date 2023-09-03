from selenium.webdriver.common.by import By
from pytest import mark
import re

pytestmark = mark.login

@mark.positive
class TestPositiveCases:
    def test_login_page(self, driver):
        target_url = "http://192.168.56.1:8080/wowsite/my-account/"
        username = "test"
        password = "TEST"

        driver.get(target_url)

        username_locator = driver.find_element(value="username")
        username_locator.send_keys(username)

        password_locator = driver.find_element(value="password")
        password_locator.send_keys(password)

        submit_button_locator = driver.find_element(by=By.NAME, value="login")
        submit_button_locator.click()

        navigation_locator = driver.find_element(by=By.CLASS_NAME, value="woocommerce-MyAccount-navigation")
        assert navigation_locator.is_displayed(), "Navigation element is not visible"

        logout_locator = driver.find_element(by=By.PARTIAL_LINK_TEXT, value="Log out")
        assert logout_locator.is_displayed(), "Logout link text is not visible"


@mark.negative
class TestNegativeCases:
    @mark.parametrize("username, password, expected_error_message",
                      [("wrong_test", "TEST", "is not registered on this site"),
                      ("test", "WRONG_TEST", "password.*is incorrect")],
                      ids=['wrong-user', 'wrong-pass'])
    def test_login_page(self, driver, username, password, expected_error_message):
        target_url = "http://192.168.56.1:8080/wowsite/my-account/"

        driver.get(target_url)

        username_locator = driver.find_element(value="username")
        username_locator.send_keys(username)

        password_locator = driver.find_element(value="password")
        password_locator.send_keys(password)

        submit_button_locator = driver.find_element(by=By.NAME, value="login")
        submit_button_locator.click()

        error_message_locator = driver.find_element(by=By.XPATH, value="//*[@class='woocommerce-error']/li")
        assert error_message_locator.is_displayed(), "Error message is not visible"

        error_message_text = error_message_locator.text
        assert re.search(expected_error_message, error_message_text), f"Error message '{error_message_text}' doesn't contain '{expected_error_message}'"
