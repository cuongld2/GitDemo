import os
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


def test_read_yaml_file():
    data_yaml = yaml.read_data_from_file('../resources/env.local.yaml')
    print('api server url is : ' + data_yaml['api_server_url'])


def test_print():
    if path.exists("guru.txt"):
        shutil.copyfile('guru.txt', 'test.txt')



