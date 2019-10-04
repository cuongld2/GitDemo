import json

import requests

from config.environment import API_SERVER_URL
from config.path import API_USER_PATH
from models.api.blog.user import userinfo


class User:

    def create_new_user(self, username, password, fullname):
        return requests.post(API_SERVER_URL + API_USER_PATH, data=json.dumps(userinfo(username, password, fullname)),
                             headers={'Content-Type': 'application/json'}
                             )
