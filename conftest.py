import pytest
from selenium import webdriver


@pytest.fixture(scope='session')
def set_up_browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def pytest_addoption(parser):
    parser.addoption("--name", action="store", default="default name")
    parser.addoption("--env", action="store", default="local")


@pytest.fixture(scope='session')
def get_env_value(pytestconfig):
    return {pytestconfig.getoption('env')}



















