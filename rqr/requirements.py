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

    def install(self, pkg, target):
        if target:
            print('TODO: save pkg to ' + target)
        pip.main(['install', pkg])

    def __str__(self):
        res = []
        for target in self.pkgs:
            res.append(target + ':')
            for requirement in self.pkgs[target]:
                version = self.pkgs[target][requirement]
                res.append('  - {0}@{1}'.format(requirement, version))
        return '\n'.join(res)
