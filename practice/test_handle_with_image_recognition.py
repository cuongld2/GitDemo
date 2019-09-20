import time

import pyautogui
import pytest
from utils_automation.setup import Browser


class TestRRIcon:
    def test_click_rr(self, browser):
        time.sleep(2)
        coords = pyautogui.locateOnScreen('rungrinh_icon.PNG')
        pyautogui.click(coords)
