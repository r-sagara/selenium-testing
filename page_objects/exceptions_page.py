from selenium.webdriver.common.by import By
from page_objects.base_page_model import BasePageModel


class ExceptionsPageModel(BasePageModel):
    _url = "https://practicetestautomation.com/practice-test-exceptions/"
    __input_locator_template = (By.XPATH, "//div[@id='row{}']/input")
    __add_button_locator_template = (By.XPATH, "//div[@id='row{}']/button[@id='add_btn']")
    __save_button_locator_template = (By.XPATH, "//div[@id='row{}']/button[@id='save_btn']")
    __edit_button_locator_template = (By.XPATH, "//div[@id='row{}']/button[@id='edit_btn']")
    __confirmation_locator = (By.ID, "confirmation")
    __instructions_locator = (By.ID, "instructions")

    def add_second_row(self):
        self._click(self._get_locator_by_count(self.__add_button_locator_template, 1))

    def _get_locator_by_count(self, locator_template, count):
        return (locator_template[0], locator_template[1].format(count))
    
    def fill_row_with_text(self, count, text):
        self._enter_text(self._get_locator_by_count(self.__input_locator_template, count), text)
        self._click(self._get_locator_by_count(self.__save_button_locator_template, count))

    def activate_row_edit(self, count):
        self._click(self._get_locator_by_count(self.__edit_button_locator_template, count))

    def clear_row(self, count):
        row_locator = self._get_locator_by_count(self.__input_locator_template, count)
        self._wait_to_be_enabled(row_locator)
        self._clear(row_locator)

    def verify_row_presence(self, count):
        timeout = 6
        assert self._wait_for_visibility(self._get_locator_by_count(self.__input_locator_template, count), timeout=timeout,
                                         custom_msg=f"Row {count} is not present in a given timeout {timeout}")

    def verify_confirmation_text(self, expected_text):
        actual_text = self._get_text(self.__confirmation_locator)
        assert actual_text == expected_text, f"Text of the confirmation popup ({actual_text}) doesn't match the expected one ({expected_text})"

    def verify_no_instructions(self):
        assert self._wait_for_invisibility(self.__instructions_locator, custom_msg="Instructions element is still displayed")