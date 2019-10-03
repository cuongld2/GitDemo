import requests

from config.environment import Environment

env_info = Environment()


class TestUserInfo:

    def test_create_new_user_success(self, get_path_value):
        print("Env info is : " + get_path_value)
