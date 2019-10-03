

class EnvironmentCustom:
    from utils_customs.path import YamlCustom
    yaml = YamlCustom()

    def get_environment_info(self):
        return self.yaml.read_data_from_file('../../resources/env.yaml')

    API_SERVER_URL = get_environment_info()['api_server_url']











