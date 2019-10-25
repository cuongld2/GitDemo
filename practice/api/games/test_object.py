import json

from models.api.games.user import UserInfo, Identification


class TestObject:

    def test_user_object(self):
        user_info = UserInfo('Cuong', 'Le', '12345')

        identification_passport = Identification('13131ABC', 'Passport')
        identification_cmnd = Identification('0126355335', 'CMND')
        identification_list = [identification_passport, identification_cmnd]

        user_info.identification = identification_list

        print(json.dumps(user_info.__dict__))



