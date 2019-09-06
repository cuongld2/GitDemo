import pytest
from selenium import webdriver


@pytest.fixture(scope='session')
def set_up_browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def pytest_addoption(parser):
    parser.addoption("--name", action="store", default="default name")















