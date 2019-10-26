import json

from models.api.games.user import UserInfo, Identification, Address, Role, Job


class TestObject:

    def test_user_object(self):
        user_info = UserInfo('Cuong', 'Le', '12345')

        identification_passport = Identification('13131ABC', 'Passport')
        identification_cmnd = Identification('0126355335', 'CMND')
        identification_list = [identification_passport, identification_cmnd]

        address = Address('Van Quan', 'Van quan')

        role = Role('admin')

        job = Job()

        user_info.identification = identification_list
        user_info.address = address
        user_info.role = role
        user_info.job = job

        print(json.dumps(user_info, default=lambda o: o.__dict__,
                         indent=4))
