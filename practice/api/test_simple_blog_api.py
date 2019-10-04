import requests

from api.blog.user import User
from config.environment import API_SERVER_URL


class TestUserInfo:
    user_api = User()

    def test_create_new_user_success(self):
        response = self.user_api.create_new_user('test1990@gmail.com', 'Abcd1234', 'Le Dinh Cuong')
        print(response)
        assert 200 == response.status_code



