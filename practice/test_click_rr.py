import time

import pyautogui


class TestRungRinh:

    def test_rungrinh_icon(self, browser):
            time.sleep(5)
            coords = pyautogui.locateOnScreen('rungrinh_icon.png')
            pyautogui.click(coords)
            time.sleep(5)