import json, jsonschema

def __validate(data, schema):
    with open(schema, 'r') as fd:
        schema = json.load(fd)
        jsonschema.validate(data, schema)

def validate_members_file():
    with open('../members.json', 'r') as fd:
        data = json.load(fd)
        __validate(data, './members.jsonschema')

def validate_past_members_file():
    with open('../past_members.json', 'r') as fd:
        data = json.load(fd)
        __validate(data, './past_members.jsonschema')

if __name__ == '__main__':
    validate_members_file()
    validate_past_members_file()
