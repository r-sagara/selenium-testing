from selenium.webdriver.common.by import By
from page_objects.base_page_model import BasePageModel


class AccountPageModel(BasePageModel):
    _url = "http://192.168.56.1:8080/wowsite/my-account/"
    __navigation = (By.CLASS_NAME, "woocommerce-MyAccount-navigation")
    __logout_link = (By.PARTIAL_LINK_TEXT, "Log out")
    __hello_message = (By.CLASS_NAME, "woocommerce-MyAccount-content")
    __expected_hello_part = "Hello {}"

    def verify_login(self, username):
        assert self.is_navigation_bar_displayed(), f"Navigation bar is not displayed"
        assert self.is_logout_link_displayed(), f"Logout link is not displayed"

        hello_text = self._get_text(self.__hello_message)
        expected_text = self.__expected_hello_part.format(username)
        assert expected_text in hello_text, f"There is no '{expected_text}' in hello message '{hello_text}'"

    def is_navigation_bar_displayed(self):
        return bool(self._wait_for_visibility(self.__navigation))
    
    def is_logout_link_displayed(self):
        return bool(self._wait_for_visibility(self.__logout_link))