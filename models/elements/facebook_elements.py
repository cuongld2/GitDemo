from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from models.locators.facebook_locators import StartPageLocators


class StartPageElements:

    @staticmethod
    def find_birthday_date_drop_down_elem(driver):
        wait = WebDriverWait(driver, 10)
        return wait.until(
            ec.presence_of_element_located(StartPageLocators.BIRTHDAY_DATE_DROPDOWN_LIST))

    @staticmethod
    def find_female_sex_radio_button(driver):
        wait = WebDriverWait(driver, 10)
        return wait.until(
            ec.element_to_be_clickable(StartPageLocators.SEX_FEMALE_RADIO_BUTTON))
