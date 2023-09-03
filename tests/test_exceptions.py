from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pytest import mark

pytestmark = mark.exceptions
TARGET_URL = "https://practicetestautomation.com/practice-test-exceptions/"

def test_no_such_element_exception(driver):  
    driver.get(TARGET_URL)

    # Click Add button
    add_button_element = driver.find_element(by=By.ID, value="add_btn")
    add_button_element.click()
    
    wait = WebDriverWait(driver, timeout=6)

    # assert wait.until(lambda d: driver.find_element(by=By.XPATH, value="//div[@id='row2']/input")).is_displayed(), "Input row 2 is not visible"
    input_field_2 = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@id='row2']/input")))
    assert input_field_2.is_displayed(), "Input row 2 is not present"

@mark.debug
def test_element_not_interactable_exception(driver):
    driver.get(TARGET_URL)
    test_text = "test"
    expected_confirmation_message = "Row 2 was saved"
    input_field_2_locator = (By.XPATH, "//div[@id='row2']/input")
    add_button_1_locator = (By.XPATH, "//div[@id='row1']/button[@id='add_btn']")
    save_button_2_locator = (By.XPATH, "//div[@id='row2']/button[@id='save_btn']")
    confirmation_locator = (By.ID, "confirmation")

    add_button_element = driver.find_element(*add_button_1_locator)
    add_button_element.click()

    wait = WebDriverWait(driver, timeout=6)
    input_field_2 = wait.until(lambda d: driver.find_element(*input_field_2_locator))
    input_field_2.send_keys(test_text)

    driver.find_element(*save_button_2_locator).click()

    confirmation_text = wait.until(lambda d: driver.find_element(*confirmation_locator).text)
    assert confirmation_text == expected_confirmation_message, f"Text of the confirmation popup ({confirmation_text}) doesn't match the expected one ({expected_confirmation_message})"