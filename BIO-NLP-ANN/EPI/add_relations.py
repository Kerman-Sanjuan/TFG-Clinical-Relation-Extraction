import argparse
import json
import re


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
    mapping = {}
    txt_opened = open(origen_txt, "r")
    txt_content = txt_opened.read()
    with open(origen_json) as f:
        json_txt = json.load(f)

    with open(origen_ann) as file:
        for line in file:
            tab_div = line.split("\t")
            # Primero mapping de las entidades
            if tab_div[0][0] == "T":
                id = tab_div[0]
                end = tab_div[1].split()[-1]
                entity_type, begin = tab_div[1].split()[:2]
                idx_word = 0
                idx_line = 0
                aux_begin = 0
                for i in range(0, int(end)):
                    if txt_content[i] == "\n":
                        idx_line = idx_line+1
                        idx_word = 0
                        aux_begin = 0
                    if (txt_content[i] == "." and not bool(re.search(r'\d', txt_content[i+1]))) or txt_content[i] == "," or txt_content[i] == " ":
                        idx_word = idx_word+1
                    if i == int(begin):
                        aux_begin = idx_word

                json_pos = json_txt[idx_line]
                anadido = False
                for entity_idx, entities in enumerate(json_pos["entities"]):
                    if entities["start"] == aux_begin and entities["end"] == idx_word+1:
                       # print(id, "ha sido anadido al mapping")
                        mapping[id] = (idx_line, entity_idx)
                        anadido = True
                        break
                if not anadido:
                    print("La id ",id, " no ha cumplido por alguna razon el calculo de entity end y begin" )
                    
        
    with open(origen_ann) as file:
        for line2 in file:
            tab_div = line2.split("\t")
            if tab_div[0][0] == "E":
                content = tab_div[1]
                # Vamos a saber si es una relacion triple o binaria.

                if len(content.split()) == 2 or len(content.split()) == 3:
                    end_piece = content.split()[-1]
                    relation_name, end_entity = end_piece.split(":")

                #elif len(content.split()) == 3:
                 #   end_entity = content.split()[-1].split(":")[1]

                #    relation_name, _ = content.split()[1].split(":")

                else:
                  #  print("relacion malformada con mas de 3 entidades")
                   # print(tab_div[0])
                    pass

                begin_piece = content.split()[0]
                ignore, begin_entity = begin_piece.split(":")
                if begin_entity in mapping.keys() and end_entity in mapping.keys():
                    if mapping[begin_entity][0] == mapping[end_entity][0]:
                        print("Begin entity es " , begin_entity,"End entity es " , end_entity, "para la relacion ",tab_div[0],"nombre de relacion: ", relation_name)
                        actual_json = json_txt[mapping[begin_entity][0]]
                        print(idx_line, " es el indice de la linea del json")
                        print(actual_json," Las relaciones se estan metiendo en esta")
                        
                        if "relations" not in actual_json.keys():
                            actual_json["relations"] = []
                        relations = actual_json["relations"]
                        relations.append(
                            {"type": relation_name, "head": mapping[begin_entity][1], "tail": mapping[end_entity][1]})
                        json_txt[mapping[begin_entity][0]]["relations"] = relations
                    else:
                        print("En la frase ",begin_entity,end_entity,"algo no coincide")
                        
    with open(destination, 'w') as file_descriptor:
        json.dump(json_txt, file_descriptor)


if __name__ == '__main__':
    args = create_arguments()
    add_entities(args.origen_ann[0], args.origen_txt[0],
                 args.origen_json[0], args.destination[0])
