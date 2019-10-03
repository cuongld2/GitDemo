from utils_customs.path import YAML


class Environment:
    yaml = YAML()

    def get_environment_info(self, env='local'):
        return self.yaml.read_data_from_file('../../resources/env.' + env + '.yaml')










