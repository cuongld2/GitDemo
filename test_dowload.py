# http://testrail.coccoc.com/index.php?/cases/view/54219
# Open 1 new tab, access any page having downloadable files (media, docs, zip,…etc)
# Click on Savior icon in browser toolbar to download some media file
# Expected Result
# The download file must be displayed in Download-shelf at the bottom of browser

import time
from lib2to3.pgen2 import driver

import pyautogui as pyautogui
from selenium import webdriver


class TestSaviorIcon:
    def test_savior_icon(self, browser):
        #driver = webdriver.Chrome()
        time.sleep(5)
        driver.get('https://zingtv.vn/video/Cong-Chua-Hat-Cat-Tap-11/IWZE8IUB.html')
        savior = pyautogui.locateOnScreen('savior_icon.png')
        pyautogui.click(savior)
        time.sleep(6)
