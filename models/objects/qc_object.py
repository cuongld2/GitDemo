from models.elements.qc_elements import LoginPageElements


class LoginObject:
    login_page_element = LoginPageElements()

    def user_login_with_username_password(self, driver, email, password):
        email_field = self.login_page_element.find_email_field(driver)
        email_field.click()
        email_field.send_keys(email)

        password_field = self.login_page_element.find_password_field(driver)
        password_field.click()
        password_field.send_keys(password)

        login_button = self.login_page_element.find_login_button(driver)
        login_button.click()