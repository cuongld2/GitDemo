import time

import pyautogui as pyautogui


class TestSideBar:

    def test_facebook_icon(self, set_up_browser):
        time.sleep(2)
        coords = pyautogui.locateOnScreen('facebook_icon.PNG')
        pyautogui.click(coords)

