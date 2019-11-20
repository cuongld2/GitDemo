from testrail_api import TestRailAPI

from utils_customs.constants import TestRailInfo


class TestTitle:

    def test_change_title_name(self):
        api = TestRailAPI(TestRailInfo.TESTRAIL_URL, TestRailInfo.TESTRAIL_USERNAME, TestRailInfo.TESTRAIL_PASSWORD)
        print(api.cases.get_cases(15))
        api.cases.update_case(119379,
                              title='Tested Create new user successfully using predefined def')
















