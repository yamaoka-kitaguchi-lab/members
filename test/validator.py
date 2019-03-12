import sys
import glob
import json
import jsonschema

class Validator:
    def __init__(self, schema):
        with open(schema, 'r') as fd:
            self.schema = json.load(fd)

    def check(self, data):
        with open(data, 'r') as fd:
            data = json.load(fd)
            jsonschema.validate(data, self.schema)

members = lambda: Validator('./members.schema.json').check('../members.json')
past_students = lambda: Validator('./past_students.schema.json').check('../past_students.json')
past_exchange_students = lambda: Validator('./past_exchange_students.schema.json').check( '../past_exchange_students.json')

if __name__ == '__main__':
    members()
    past_students()
    past_exchange_students()
