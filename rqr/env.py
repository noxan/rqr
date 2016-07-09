import os
import sys
from venv import create

class Env():
    def ensure(self):
        path = os.path.join(os.getcwd(), '.env')
        create(path, with_pip=True)
        os.environ['VIRTUAL_ENV'] = path

        sys.prefix = path
        sys.exec_prefix = path
        print(sys.prefix)
