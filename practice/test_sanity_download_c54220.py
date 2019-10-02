''' Testcase C54220:
Step:
1. Open Browser
2. Open 1 new tab, access any page having downloadable files (media, docs, zip,…etc)
3. Click on icon "Open "Downloads" page" in browser toolbar at top right corner

Expect:
1. icon  "Open "Downloads" page" must be displayed in the top right corner of browser
2. During download progress, % file completed  in Download-shelf must be the same with % completed showing in icon "Open "Downloads" page" in browser toolbar
3. When click on the icon, 1 tab opens with download history list
'''

import time
import pyautogui as pyautogui


class Test_Sanity_Download:

    def test_sanity_download_c54220(self, browser):
        time.sleep(5)
        coords = pyautogui.locateOnScreen('download_page.png')
        pyautogui.click(coords)
        time.sleep(5)
        assert 'downloads' in browser.current_url

