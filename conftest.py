from selenium import webdriver as sele_webdriver


def browser():
    chrome_options = sele_webdriver.ChromeOptions()
    chrome_options.add_argument("--window-size=1920,1080")
    # chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--proxy-server='direct://'")
    chrome_options.add_argument("--proxy-bypass-list=*")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument("--allow-insecure-localhost")
    chrome_options.add_argument("--disable-infobars")
    # chrome_options.add_argument('--user-data-dir=' + os.environ['user-dir-path'])
    chrome_options.add_argument(
        '--user-data-dir=' + "C:\\Users\\DuongPH_PC\\AppData\\Local\\CocCoc\\Browser\\User Data")
    driver = sele_webdriver.Chrome(options=chrome_options)