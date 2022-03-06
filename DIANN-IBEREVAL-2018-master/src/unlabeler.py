import argparse
import json
import re


def create_arguments():
    parser = argparse.ArgumentParser(
        description='Print confussion matrix between to JSON files.')

    parser.add_argument('--json', dest='origen_json', nargs='+',
                        help='Path no the .json file')

    parser.add_argument('--d', dest='destination', nargs='+',
                        help='Path to created JSON')
    args = parser.parse_args()
    return args


def unlabeler(origen_json, destination):

    with open(origen_json) as f:
        json_txt = json.load(f)

        for idx,jsons in enumerate(json_txt):
            del json_txt[idx]['entities']
            del json_txt[idx]['relations']
        
    with open(destination, 'w') as outfile:
        json.dump(json_txt, outfile)


if __name__ == '__main__':
    args = create_arguments()
    unlabeler(args.origen_json[0], args.destination[0])
