import os
import pytest
from selenium import webdriver
from utils_customs.files import Files

files = Files()


@pytest.fixture(scope='session')
def set_up_browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def pytest_addoption(parser):
    parser.addoption("--name", action="store", default="default name")
    parser.addoption("--env", action="store", default="local")


@pytest.fixture(scope='session', autouse=True)
def get_env_value(pytestconfig):
    files.copy_file(os.getcwd() + '/resources/env.' + str(pytestconfig.getoption('env')) + '.yaml',
                    os.getcwd() + '/resources/env.yaml')





















