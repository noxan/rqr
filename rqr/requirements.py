import pip
import yaml

FILENAME = 'rqr.yaml'


class Requirements:
    def __init__(self):
        self.pkgs = {}
        self.reload()

    def reload(self):
        with open(FILENAME, 'r') as stream:
            self.pkgs = yaml.load(stream)

    def install(self, pkg):
        pip.main(['install', pkg])
