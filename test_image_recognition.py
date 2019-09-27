import time

import pyautogui as pyautogui
from selenium import webdriver


class Testimagereconition:
    def test_image_recognition(self):
        driver = webdriver.Chrome()
        url = "http://coccoc.com"
        driver.get(url)
        recog = pyautogui.locateOnScreen('facebook_icon.png')
        pyautogui.click(recog)
        time.sleep(5)
        driver.quit()




