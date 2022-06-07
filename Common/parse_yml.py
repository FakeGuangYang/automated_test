import yaml

"""
Parse yaml files through file name, section and key
"""


def parse_yml(file, section, key):
    with open(file, 'r', encoding='utf-8') as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
        return data[section][key]
