import re
import os

TARGET_PRODUCTION_PATTERN = '(prod|production)'
TARGET_DEVELOPMENT_PATTERN = '(dev|development)'
TARGETS_PATTERN = '(base|{0}|{1})'.format(TARGET_PRODUCTION_PATTERN, TARGET_DEVELOPMENT_PATTERN)
REQUIREMENTS_REGEX = re.compile('({0}-)?requirements(-{0})?.txt'.format(TARGETS_PATTERN))

class Migrator:
    def run(self):
        self.search()

    def search(self):
        for item in os.listdir(os.getcwd()):
            if os.path.isdir(item) and item == 'requirements':
                print('Requirements folder found.')
            elif os.path.isfile(item) and REQUIREMENTS_REGEX.match(item):
                self.migrate_file(item)

    def migrate_file(self, filename):
        print(filename)
