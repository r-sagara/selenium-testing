from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from pytest import mark

pytestmark = mark.exceptions


def test_no_such_element_exception(ExceptionsPage):  
    ExceptionsPage.add_second_row()
    ExceptionsPage.verify_row_presence(2)


def test_element_not_interactable_exception(ExceptionsPage):
    test_text = "test"
    expected_confirmation_message = "Row 2 was saved"
    ExceptionsPage.add_second_row()
    ExceptionsPage.verify_row_presence(2)
    ExceptionsPage.fill_row_with_text(2, test_text)
    ExceptionsPage.verify_confirmation_text(expected_confirmation_message)
    

def test_invalid_element_state_exception(ExceptionsPage):
    test_text = "test"
    expected_confirmation_message = "Row 1 was saved"
    ExceptionsPage.activate_row_edit(1)
    ExceptionsPage.clear_row(1)
    ExceptionsPage.fill_row_with_text(1, test_text)
    ExceptionsPage.verify_confirmation_text(expected_confirmation_message)


def test_stale_element_reference_exception(ExceptionsPage):
    ExceptionsPage.add_second_row()
    ExceptionsPage.verify_no_instructions()


def test_timeout_exception(ExceptionsPage):
    ExceptionsPage.add_second_row()
    ExceptionsPage.verify_row_presence(2)