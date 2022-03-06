import json
import argparse
""" 
Para que el funcionamiento sea adecuado, es necesario que todos los .ann y todos los .txt esten en un mismo fichero.
El objetivo de este metodo es crear un .json desde 0 con estos dos ficheros.
"""

data = []


def create_arguments():
    parser = argparse.ArgumentParser(
        description='Print confussion matrix between to JSON files.')
    parser.add_argument('--ann', dest='origen_ann', nargs='+',
                        help='Path no the .ann file')
    parser.add_argument('--txt', dest='origen_txt', nargs='+',
                        help='Path no the .txt file')
    parser.add_argument('--d', dest='destination', nargs='+',
                        help='Path to created JSON')
    args = parser.parse_args()
    return args


def convert(origen_ann, origen_txt, dest):
    create_tokens(origen_ann, origen_txt,dest)


def create_tokens(origen_ann, origen_txt,dest):
    ann_opened = open(origen_ann, "r")
    ann_content = ann_opened.readlines()
    ann_opened.close()
    txt_opened = open(origen_txt, "r")
    txt_content = txt_opened.read()

    """ El formato funciona de la siguiente manera:
        1. Cada fila del .txt va a corresponder a un tokens de entrenamiento
        2. Los caracteres se han respetado, por cada salto de linea hay que resetear el contador de palabras y crear un json nuevo.
        3. Todo eso metido en un []
    
        -- Conjuntos de datos que necesitamos -
        1. Unlabeled data con todos los datos OK 
        2. Labeled data con todos los datos
    """

    with open(origen_txt) as file:
        for line in file:
            follow = True
            # 1. Creamos un json y anadimos los tokens
            actual_json = dict()
            print(line)
            line_dot_space = line.replace(".", " .")
            line_comma_space = line_dot_space.replace(",", " ,")
            tokens = line_comma_space.split()
            actual_json["tokens"] = tokens
            # En este punto tenemos un array de JSON con los tokens ya puestos.
            data.append(actual_json)

            # Cada elemento de la lista corresponde a una frase. Comentar los errores que puede traer las relaciones multilinea.
        with open(dest, 'w') as f:
            f.write(str(data))


if __name__ == '__main__':
    args = create_arguments()
    convert(args.origen_ann[0], args.origen_txt[0], args.destination[0])
