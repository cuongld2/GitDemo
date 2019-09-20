from selenium.webdriver.common.by import By


class LoginLocators:
    EMAIL_LOCATOR = (By.NAME, 'email')
    PASSWORD_LOCATOR = (By.NAME, 'pass')
    LOGIN_BUTTON_LOCATOR = (By.XPATH, '/html/body/div[1]/div[2]/div/div/div/div/div[2]/form/table/tbody/tr[2]/td[3]/label/input')