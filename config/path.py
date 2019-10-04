import os

from utils_customs.path import YamlCustom
yaml = YamlCustom()


def get_path_info():
    return yaml.read_data_from_file(os.getcwd().split('/practice/api')[0] + '/resources/path.yaml')


API_USER_PATH = get_path_info()['api']['user']
API_AUTHENTICATE_PATH = get_path_info()['api']['authenticate']
API_BLOG_PATH = get_path_info()['api']['blog']











