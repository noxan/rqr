import pip
import yaml

FILENAME = 'rqr.yaml'


class Requirements:
    def install(self, pkg):
        pip.main(['install', pkg])


def load_requirements():
    with open(FILENAME, 'r') as stream:
        return yaml.load(stream)
