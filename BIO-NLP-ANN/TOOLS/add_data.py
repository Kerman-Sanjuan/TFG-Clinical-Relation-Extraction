import argparse
import json


def create_arguments():
    parser = argparse.ArgumentParser(
        description='Print confussion matrix between to JSON files.')
    parser.add_argument('--ann', dest='origen_ann', nargs='+',
                        help='Path no the .ann file')
    parser.add_argument('--txt', dest='origen_txt', nargs='+',
                        help='Path no the .txt file')

    parser.add_argument('--json', dest='origen_json', nargs='+',
                        help='Path no the .json file')

    parser.add_argument('--d', dest='destination', nargs='+',
                        help='Path to created JSON')
    args = parser.parse_args()
    return args


def add_entities(origen_ann, origen_txt, origen_json, destination):
    txt_opened = open(origen_txt, "r")
    txt_content = txt_opened.read()
    with open(origen_json) as f:
        json_txt = json.load(f)
    with open(origen_ann) as file:
        for line in file:
            tab_div = line.split("\t")
            if tab_div[0][0] == "T":
                # Predicate 22 28 dentro
                entity_type, begin = tab_div[1].split()[:2]
                end = tab_div[1].split()[-1]
                print(end)
                entity_name = tab_div[2]
                # print(entity_name)
                #print("Entidad es: ",entity_type," inicio es: ",begin," final es: ",end)
                idx_word = 0
                idx_line = 0
                aux_begin = 0
                for i in range(0, int(end)):
                    if txt_content[i] == "\n":
                        idx_line = idx_line+1
                        idx_word = 0
                        aux_begin = 0
                    if txt_content[i] == "." or txt_content[i] == "," or txt_content[i] == " ":
                        idx_word = idx_word+1
                    if i == int(begin):
                        aux_begin = idx_word
                actual_json = json_txt[idx_line]
                if "entities" not in actual_json.keys():
                    actual_json["entities"] = []
                entities = actual_json["entities"]
                entities.append(
                    {"type": entity_type, "start": aux_begin, "end": idx_word+1})
                json_txt[idx_line]["entities"] = entities
                # Concept 281 291;292 305
        with open('json_data.json', 'w') as outfile:
            json.dump(json_txt, outfile)


if __name__ == '__main__':
    args = create_arguments()
    add_entities(args.origen_ann[0], args.origen_txt[0],
                 args.origen_json[0], args.destination[0])
