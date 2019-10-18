from marshmallow_dataclass import dataclass
from typing import List, Optional
import marshmallow.validate


def userinfo(username, password, fullname):
    return {
        'username': username,
        'password': password,
        'fullname': fullname
    }


@dataclass
class UserInfo(object):
    id: Optional[int]
    username: int
    password: str
    fullname: str

    def __init__(self, username, password, fullname):
        self.username = username
        self.password = password
        self.fullname = fullname











