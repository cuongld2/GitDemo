from selenium.webdriver.common.by import By


class LoginLocators:
    EMAIL_LOCATOR = (By.ID, 'name')
    PASSWORD_LOCATOR = (By.ID, 'password')
    LOGIN_BUTTON_LOCATOR = (By.XPATH, '//button[@type="submit"]')


