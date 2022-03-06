import json


def count_first_chars(phrase, entity):
    """ Queremos contar cuantos caracteres hay hasta la primera palabra"""
    char_count = 0
    for i in range(0,entity):
        char_count = char_count + len(phrase[i]) + 1
    return char_count# Por la suma final que no toca.


class conversor:
    def __init__(self, origen, destination):
        self.origen = origen
        self.destination = destination
        with open(self.origen) as f:
            self.predictions_dict = json.load(f)

    def convertor(self):
        """ JSON to ANN conversor"""
        self.create_txt_file()
        self.create_ann_file()

    def create_txt_file(self):
        # BRAT needs to fiels to work, a .txt with the text and a .ann with the relations, so first we will create the txt.
        with open(self.destination + '.txt', "w") as x:
            for i in range(0, len(self.predictions_dict)):
                sentence = ' '.join(self.predictions_dict[i]['tokens'])
                # sentence = re.sub(r'\s([?.!,"](?:\s|$))', r'\1', sentence) #Whitespace on punctuation marks.
                x.write(sentence + '\n')

    def create_ann_file(self):
        self.write_entities()

    def write_entities(self):
        with open(self.destination + '.ann', "w", encoding="utf-8") as p:
            with open(self.destination + '.txt', encoding="utf-8") as r:
                lines = r.readlines()
                total_lines_length = 0
                T_id = 1
                for sentence_idx, sentence in enumerate(lines):
                    print(sentence)
                    for entity in self.predictions_dict[sentence_idx]['entities']:
                        phrase = " ".join(self.predictions_dict[sentence_idx]['tokens'][entity['start']:entity['end']])
                        # Que vamos a hacer por cada entidad.
                        # 1. Vamos a ver en que caracter empieza y en cual acaba.
                        # first char = acum+letrasHastaLaPalabra
                        first_char = total_lines_length+sentence_idx + count_first_chars(
                            self.predictions_dict[sentence_idx]["tokens"], entity["start"])
                        last_char = first_char+len(phrase)
                    #  print("Number of characters before last word: " + str(chars_until_last_word))

                        p.write('T' + str(T_id) + '\t' + str(entity['type']) + ' ' + str(
                                first_char) + ' ' + str(last_char) + '\t' + str(phrase) + '\n')
                        T_id += 1
                    total_lines_length = total_lines_length + len(str(sentence)) - 1


def write_relations(self):
        return None

