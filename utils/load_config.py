import json

config = None

def load_config():
    global config

    if config:
        return config

    with open('config.json', 'r') as fp:
        config = json.load(fp)
        return config
