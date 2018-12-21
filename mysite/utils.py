import yaml

def load_yaml_from_file(filename):
  with open(filename, 'r') as stream:
    return yaml.load(stream)
