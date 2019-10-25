from typing import Optional


class UserInfo(object):
    id: Optional[int]
    role: object
    identification: list
    address: object
    job: object

    def __init__(self, first_name, last_name, password):
        self.name = Name(first_name, last_name)
        self.password = password


class Role(object):
    id: Optional[int]

    def __init__(self, role):
        self.role = role


class Name(object):

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


class Identification(object):
    id: Optional[int]

    def __init__(self, id_number, identification_type):
        self.id_number = id_number
        self.identification_type = IdentificationType(identification_type)


class IdentificationType(object):
    id: Optional[int]

    def __init__(self, identification_type):
        self.identification_type = identification_type


class Address(object):

    def __init__(self, permanent_address, current_address):
        self.permanent_address = permanent_address
        self.current_address = current_address


class Job(object):

    def __init__(self, field, role):
        self.field = field
        self.role = role







