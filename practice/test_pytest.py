import re
import shutil
from os import path
import pytest

from utils_customs.path import YamlCustom

yaml = YamlCustom()


@pytest.fixture()
def name(pytestconfig):
    return pytestconfig.getoption("name")


def test_print_name(name):
    print(f"\ncommand line param (name): {name}")


def test_print_name_2(pytestconfig):
    print(f"test_print_name_2(name): {pytestconfig.getoption('name')}")


def test_print():
    if path.exists("guru.txt"):
        shutil.copyfile('guru.txt', 'test.txt')


def test_get_user():
    import getpass
    print(getpass.getuser())


def test_regex():
    assert_string = re.split(r'[A-Za-z]/', 'https://vuviphim.com/xem-phim-kochouki-wakaki-nobunaga-212770')[1]
    print(assert_string)

