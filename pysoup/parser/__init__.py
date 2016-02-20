import yaml


class Parser(object):

    def __init__(self):
        pass

    def parse_file(self, path):
        with open(path, 'rb') as f:
            yaml_data = f.read()
        return self.parse(yaml_data)

    def parse(self, string):
        return yaml.load(string)
