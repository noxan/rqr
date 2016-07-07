import re
import os

TARGET_PRODUCTION_PATTERN = '(prod|production)'
TARGET_PRODUCTION_REGEX = re.compile('.*{0}.*'.format(TARGET_PRODUCTION_PATTERN))
TARGET_DEVELOPMENT_PATTERN = '(dev|development)'
TARGET_DEVELOPMENT_REGEX = re.compile('.*{0}.*'.format(TARGET_DEVELOPMENT_PATTERN))
TARGETS_PATTERN = '(base|{0}|{1})'.format(TARGET_PRODUCTION_PATTERN, TARGET_DEVELOPMENT_PATTERN)
REQUIREMENTS_REGEX = re.compile('({0}-)?requirements(-{0})?.txt'.format(TARGETS_PATTERN))
TARGETS_REGEX = re.compile('{0}.txt'.format(TARGETS_PATTERN))
REQUIREMENTS_FOLDER_NAME = 'requirements'

class Migrator:
    def run(self):
        self.search()

    def search(self):
        for item in os.listdir(os.getcwd()):
            if os.path.isdir(item) and item == REQUIREMENTS_FOLDER_NAME:
                for subitem in os.listdir(item):
                    if TARGETS_REGEX.match(subitem):
                        self.migrate_file(os.path.join(REQUIREMENTS_FOLDER_NAME, subitem))
            elif os.path.isfile(item) and REQUIREMENTS_REGEX.match(item):
                self.migrate_file(item)

    def discover_target(self, filename):
        if TARGET_PRODUCTION_REGEX.match(filename):
            return 'production'
        elif TARGET_DEVELOPMENT_REGEX.match(filename):
            return 'development'
        else:
            return 'base'

    def migrate_file(self, filename):
        target = self.discover_target(filename)
        print(filename, 'for', target)
        with open(filename, 'r') as stream:
            line = True
            while line:
                line = stream.readline().strip()
                print(line)
            stream.close()
