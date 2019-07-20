import os
import sys
import argparse
import json
import re

SCHEMA_PATH = os.path.abspath('../resources/schema')


def main():
    parser = argparse.ArgumentParser(description='Do stuff')
    parser.add_argument('--schema', default=None)
    arguments = parser.parse_args()
    schema_file = arguments.schema
    schema_file_path = SCHEMA_PATH + os.sep + schema_file

    name = schema_file.replace('.json', '')

    with open(schema_file_path, 'r') as myfile:
        schema = myfile.read()

    schema_json = json.loads(schema)

    autogenerate_parse(schema_json, name)


def autogenerate_parse(schema_json, name):
    myfile = open(name + '.py', 'w')
    final_string = '\n'

    final_string += 'def parse_{0}({0}, data):\n'.format(name)

    for key in schema_json.keys():
        py_key = convert_var(key)
        key_json = schema_json[key]

        if key == 'kind':
            continue

        if type(schema_json[key]) is not dict:
            final_string += '{3}{0}.{2} = data[\'{1}\']\n'.format(name, key, py_key, 4*' ')
            continue

        final_string += '\n'
        final_string += 4*' ' + '# ' + key + '\n'
        final_string += '{2}{1}_data = data.get(\'{0}\', False)\n'.format(key, py_key, 4*' ')
        final_string += '{1}if {0}_data:\n'.format(py_key, 4*' ')

        for key2 in key_json.keys():
            if type(key_json[key2]) is dict:
                continue
            py_key2 = convert_var(key2)
            key2_json = key_json[key2]
            final_string += '{4}{0}.{3} = {2}_data.get(\'{1}\', None)\n'.format(name, key2, py_key, py_key2, 8*' ')

    final_string += '\n'
    final_string += '{1}return {0}'.format(name, 4*' ')

    myfile.write(final_string)
    myfile.close()
    # print(final_string)


def convert_var(var_name):
    return re.sub('(?<!^)(?=[A-Z])', '_', var_name).lower()


def contains_only_primitive_keys(json_dict):
    for key in json_dict.keys():
        t = type(json_dict[key])
        if t is not dict:
            return True
    return False


if __name__ == '__main__':
    main()
