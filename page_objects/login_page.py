from selenium.webdriver.common.by import By
from page_objects.base_page_model import BasePageModel
import re


class LoginPageModel(BasePageModel):
    _url = "http://192.168.56.1:8080/wowsite/my-account/"
    __username_field = (By.ID, "username")
    __password_field = (By.ID, "password")
    __submit_button = (By.NAME, "login")
    __error_message = (By.XPATH, "//*[@class='woocommerce-error']/li")

    def do_login(self, username, password):
        self._enter_text(self.__username_field, username)
        self._enter_text(self.__password_field, password)
        self._click(self.__submit_button)

    def verify_error_message(self, expected_message):
        error_message_text = self._get_text(self.__error_message, timeout=3)
        assert re.search(expected_message, error_message_text), f"Error message '{error_message_text}' doesn't contain '{expected_message}'"

