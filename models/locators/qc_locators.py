from selenium.webdriver.common.by import By


class LoginLocators:
    EMAIL_LOCATOR = (By.NAME, 'email')
    PASSWORD_LOCATOR = (By.NAME, 'password')
    LOGIN_BUTTON_LOCATOR = (By.XPATH, '//button[contains(text(),"ng nh")]')
    HOMEPAGE_LOCATOR = (By.XPATH, '//a[@class="hoverable"][contains(text(),"n d")]')