from selenium.webdriver.common.by import By


class LoginLocators:
    EMAIL_LOCATOR = (By.ID, 'name')
    PASSWORD_LOCATOR = (By.ID, 'password')
    LOGIN_BUTTON_LOCATOR = (By.XPATH, '//button[@type="submit"]')


# 2 blank lines after each class


class HomePageLocators:
    BROWSER_MOBILE_LOCATOR = (By.XPATH, '//a[@href="index.php?/projects/overview/3"]')
    BROWSER_WINDOW_LOCATOR = (By.XPATH, '//a[@href="index.php?/projects/overview/2"]')

    TEST_CASE_RESULT_LOCATOR = (By.XPATH, '//a[@href="#statusDropdown" and @rel="143312"][text() = "Not test"]')


