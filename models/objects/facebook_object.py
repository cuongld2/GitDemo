from selenium.webdriver.support.select import Select

from models.elements.facebook_elements import StartPageElements


class StartPageObject:
    start_page_elems = StartPageElements()

    def choose_date_birthday(self, driver, index):
        select_date = Select(self.start_page_elems.find_birthday_date_drop_down_elem(driver))
        return select_date.select_by_index(index)

    def choose_female_sex(self, driver):
        self.start_page_elems.find_female_sex_radio_button(driver).click()



