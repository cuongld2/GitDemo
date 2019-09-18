from selenium.webdriver.common.by import By


class LoginStagingLocator:
    EMAIL_LOCATOR = (By.NAME, 'email')
    PASSWORD_LOCATOR = (By.NAME, 'password')
    LOGIN_BUTTON_LOCATOR = (By.XPATH, '//button[@type="submit"]')
    HEADER_LINK_LOCATOR = (By.ID, 'header-link-email')

