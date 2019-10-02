from selenium.webdriver.common.by import By


class SettingsPageLocators:
    # ADD_LINK_BUTTON = (By.CLASS_NAME, 'js-addLink addButton headerButton')
    # ADD_TORRENT_BUTTON = (By.CLASS_NAME, 'js-addTorrent torrentButton headerButton')
    # CLEAR_ALL_BUTTON = (By.CLASS_NAME, 'js-clearAll clearButton headerButton')
    ADD_LINK_BUTTON = (By.XPATH, '//*[@id="root"]/div/header/div/button[1]')
    ADD_TORRENT_BUTTON = (By.XPATH, '//*[@id="root"]/div/header/div/button[2]')
    CLEAR_ALL_BUTTON = (By.XPATH, '//*[@id="root"]/div/header/div/button[5]')
