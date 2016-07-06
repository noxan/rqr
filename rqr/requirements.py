import yaml

FILENAME = 'rqr.yaml'

def load_requirements():
    with open(FILENAME, 'r') as stream:
        return yaml.load(stream)
