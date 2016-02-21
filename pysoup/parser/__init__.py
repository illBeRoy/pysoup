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

    def dump_to_file(self, configuration, path):
        yaml_data = self.dump(configuration)
        with open(path, 'wb') as f:
            f.write(yaml_data)

    def dump(self, configuration):
        yaml_string = ''
        for key in ['name', 'author', 'version', 'repository', 'dependencies']:
            if configuration.has_key(key):
                yaml_string += yaml.dump({key: configuration[key]}, default_flow_style=False)
        return yaml_string
