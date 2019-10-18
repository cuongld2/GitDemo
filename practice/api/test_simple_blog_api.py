from api.blog.user import User
# from utils_customs.database import RestAPIDatabase
from utils_customs.database import RestAPIDatabase
from utils_customs.random import RandomGenerator


class TestUserInfo:
    user_api = User()
    restapi_query = RestAPIDatabase()
    random_gen = RandomGenerator()

    def test_create_new_user_success(self, set_up_mysql):
        username = self.random_gen.random_string(8) + '@gmail.com'
        # username = 'test1990@gmail.com'
        response = self.user_api.create_new_user(username, 'Abcd1234', 'Le Dinh Cuong')
        try:
            result_user_info = self.restapi_query.get_user_info_by_username(set_up_mysql, username)
            assert result_user_info is not None
            assert 200 == response.status_code
        finally:
            self.restapi_query.delete_user_info_by_username(set_up_mysql, username)

    def test_create_new_user_success_using_data_class(self, set_up_mysql):
        username = self.random_gen.random_string(8) + '@gmail.com'
        try:
            response = self.user_api.create_new_user_data_class(username, 'Abcd12345$', 'Le Dinh Cuong')
            assert 200 == response.status_code
        finally:
            self.restapi_query.delete_user_info_by_username(set_up_mysql, username)




