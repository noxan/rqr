import pip
import yaml

FILENAME = 'rqr.yaml'


class Requirements:
    def load(self):
        with open(FILENAME, 'r') as stream:
            return yaml.load(stream)

    def install(self, pkg):
        pip.main(['install', pkg])
