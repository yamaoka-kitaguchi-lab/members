import json, jsonschema

def __validate(data, schema):
    with open(schema, 'r') as fd:
        schema = json.load(fd)
        jsonschema.validate(data, schema)

def validate_members_file():
    with open('../members.json', 'r') as fd:
        data = json.load(fd)
        __validate(data, './members.jsonschema')

def validate_past_students_file():
    with open('../past_students.json', 'r') as fd:
        data = json.load(fd)
        __validate(data, './past_students.jsonschema')

def validate_past_exchange_students_file():
    with open('../past_exchange_students.json', 'r') as fd:
        data = json.load(fd)
        __validate(data, './past_exchange_students.jsonschema')

if __name__ == '__main__':
    validate_members_file()
    validate_past_students_file()
    validate_past_exchange_students_file()
