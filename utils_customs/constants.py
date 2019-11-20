

class SiteUrls:
    TESTRAIL_URL = 'https://phamduong.testrail.io/index.php?/auth/login'
    FACEBOOK_URL = 'https://www.facebook.com/'


class AuthenticationInfo:
    TESTRAIL_EMAIL = 'phamduongtest1@gmail.com'
    TESTRAIL_PASSWORD = 'Duong@123456'


class CocCocSettingsUrls:
    SETTINGS_LANGUAGES = 'coccoc://settings/languages'


class TestRailInfo:
    import os
    import configparser
    config = configparser.ConfigParser()
    config.read(os.getcwd().split('practice')[0] + '/testrail.cfg')

    TESTRAIL_URL = config['API']['url']
    TESTRAIL_USERNAME = config['API']['email']
    TESTRAIL_PASSWORD = config['API']['password']











