from typing import Optional

from security_utils import Crypts


class UserInfo(object):
    id: Optional[int] = None
    role: object = None
    identification: list = []
    address: object = None
    job: object = None

    def __init__(self, first_name, last_name, password):
        self.name = Name(first_name, last_name)
        self.password = Crypts.encode('encode', password)


class Role(object):
    id: Optional[int] = None

    def __init__(self, role):
        self.role = role


class Name(object):

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


class Identification(object):
    id: Optional[int] = None
    id_number: str = None
    identification_type: object = None

    def __init__(self, id_number, identification_type):
        self.id_number = id_number
        self.identification_type = IdentificationType(identification_type)


class IdentificationType(object):
    id: Optional[int] = None

    def __init__(self, identification_type):
        self.identification_type = identification_type


class Address(object):
    permanent_address: str = None
    current_address: str = None

    def __init__(self, permanent_address, current_address):
        self.permanent_address = permanent_address
        self.current_address = current_address


class Job(object):
    field: str
    role: str

    def __init__(self):
        self.field = ''
        self.role = ''







