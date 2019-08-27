from selenium.webdriver.common.by import By


class LoginLocators:
    EMAIL_LOCATOR = (By.ID, 'name')
    PASSWORD_LOCATOR = (By.ID, 'password')
    LOGIN_BUTTON_LOCATOR = (By.ID, 'button_primary')


# 2 blank lines after each class


class HomePageLocators:
    BROWSER_MOBILE_LOCATOR = (By.XPATH, '//a[@href="index.php?/projects/overview/1"]')
    TEST_RUN_LOCATOR = (By.XPATH, '//a[@href="index.php?/runs/view/1"]')

class AddResultLocators:
    ADD_RESULT_LOCATOR = (By.ID, 'addResult')
    ADD_RESULT_SM_LOCATOR = (By.ID, 'addResult')

   # BROWSER_WINDOW_LOCATOR = (By.XPATH, '//a[@href="index.php?/projects/overview/2"]')