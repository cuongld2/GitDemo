import requests

from config.environment import EnvironmentCustom

environment_custom = EnvironmentCustom()


class TestUserInfo:

    def test_create_new_user_success(self):
        print("API URL IS : " + environment_custom.API_SERVER_URL)


