
from api.blog.user import User
from utils_customs.database import RestAPIDatabase


class TestUserInfo:
    user_api = User()
    restapi_query = RestAPIDatabase()

    def test_create_new_user_success(self, set_up_mysql):
        response = self.user_api.create_new_user('test1990@gmail.com', 'Abcd1234', 'Le Dinh Cuong')
        try:
            result_user_info = self.restapi_query.get_user_info_by_username(set_up_mysql, 'test1990@gmail.com')
            assert result_user_info is not None
            assert 200 == response.status_code
        finally:
            self.restapi_query.delete_user_info_by_username(set_up_mysql, 'test1990@gmail.com')




