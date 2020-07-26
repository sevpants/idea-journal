import os
import yaml


def get_config():
    config_path = os.path.relpath('idea-journal.yaml')

    with open(config_path, 'r') as f:
        contents = f.read()
        config = yaml.load(contents, Loader=yaml.BaseLoader)
    
    return config