import time

import pyautogui as pyautogui
import pytest
from selenium import webdriver


class TestSideBar:

    @pytest.fixture(scope='module')
    def set_up_browser(self):
        driver = webdriver.Chrome()
        yield driver
        driver.quit()

    def test_facebook_icon(self, set_up_browser):
        time.sleep(2)
        coords = pyautogui.locateOnScreen('facebook_icon.PNG')
        pyautogui.click(coords)
