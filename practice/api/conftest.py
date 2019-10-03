import pytest

from config.environment import Environment

env_info = Environment()


@pytest.fixture(scope='session')
def get_path_value(get_env_value):
    return env_info.get_environment_info()['api_server_url']