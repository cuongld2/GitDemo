from selenium.webdriver.common.by import By


class LoginPageLocators:
    EMAIL_FIELD = (By.NAME, 'email')
    PASSWORD_FIELD = (By.NAME, 'password')
    LOGIN_BUTTON = (By.XPATH, '//button[@data-track_event-label="Login page"][text()="Đăng nhập"]')
    LOGIN_MESSAGE = (By.XPATH, '//*[@id="client-login"]/form/div[1]')
    ERROR_MESSAGE = (By.CLASS_NAME, 'form-errors clearfix')

