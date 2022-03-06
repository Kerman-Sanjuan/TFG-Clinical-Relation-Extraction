import argparse

import json



def create_arguments():
    parser = argparse.ArgumentParser(
        description='Print confussion matrix between to JSON files.')

    parser.add_argument('--json', dest='origen_json', nargs='+',
                        help='Path no the .json file')

    parser.add_argument('--d', dest='destination', nargs='+',
                        help='Path to created JSON')
    args = parser.parse_args()
    return args




def create_types(origen_json):
    entities_types = {}
    relations_type = {}
    with open(origen_json) as f:
        json_txt = json.load(f)
       # print(json_txt[216])
        for idx,jsons in enumerate(json_txt):
            print("Indice: ",idx)
            for entity in jsons["entities"]:
                print(jsons["tokens"][entity["start"]])





if __name__ == '__main__':
    args = create_arguments()
    create_types(args.origen_json[0])
