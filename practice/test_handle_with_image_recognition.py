import time

import pyautogui as pyautogui
import pytest
from selenium import webdriver


class TestSideBar:

    @pytest.fixture(scope='module')
    def set_up_browser(self):
        driver = webdriver.Chrome()
        yield driver
        time.sleep(4)

    def test_facebook_icon(self, set_up_browser):
        time.sleep(5)
        coords = pyautogui.locateOnScreen('facebook_icon.PNG')
        pyautogui.click(coords)

