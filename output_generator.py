import json

START_PATH = 'action_result.data.*.' 
DATA_KEY = '' #value key i.e 'data' in response json where all of data are located, leave empty if response is signle data occurance

mapping = {
    bool: 'boolean',
    int: 'numeric',
    float: 'numeric',
    str: 'string',
    'bool': 'boolean',
    'int': 'numeric',
    'float': 'numeric',
    'string': 'string'
}

def generating(dict, start_path):
    for key, value in dict.items():
        if type(value) in mapping:
            yield start_path + key, mapping[type(value)]
        else:
            if not value:
                yield start_path + key + '.*', 'string'
            elif type(value) is list and all(isinstance(item, (str, bool)) for item in value):
                yield start_path + key + '.*', 'string'
            else:
                if type(value) is list:
                    yield from generating(value[0], start_path + key + '.*.')
                else:
                    yield from generating(value, start_path + key + '.')

json_odput = []
with open('response_scheme.json', 'r') as file:
    content = json.loads(file.read())
    iter_obj =  content[DATA_KEY] if DATA_KEY else [content]
    for nested in iter_obj:
        for key, value in generating(nested, START_PATH):
            json_odput.append(
                {
                    "data_path": key,
                    "data_type": value
                }
            )

with open('soar_paths.json', 'w') as write_file:
    json.dump(json_odput, write_file)
