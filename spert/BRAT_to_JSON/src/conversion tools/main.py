import os
import argparse
from posixpath import split
import re
import json


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
    print(args.origen_txt[0])
    return args


def get_tokens(orig_txt):
    """ Obtenemos los tokens -OUTDATED-
        Con el metodo nuevo despues de la transformacion funciona mejor.    
    """
    txt_opened = open(orig_txt, "r")
    text = txt_opened.read()
    print(len(text))
    tp = text.replace('.', ' .')
    tp2 = tp.replace(",", " ,")
    split_text = tp2.split()
    result = {"tokens": split_text}
    print(result)
    with open('pruebas_formato.json', 'w') as fp:
        json.dump(result, fp)


def transformar_txt(orig_txt,dest):
    """ Con este metodo arreglamos los saltos de linea del formato BRAT para 
        hacer que se respeten los numeros de caracter y hacer salto de linea cada .[ESP]MAYUS
    """

    txt_opened = open(orig_txt, "r")
    text = txt_opened.read()
    lista_text = list(text)
    for idx, char in enumerate(text):
        if (len(text) - idx < 2):
            break
        if text[idx] == "." and text[idx+1] == " " and re.match("[A-Z]", text[idx+2]):
            print("Ha ocurrido en el idx: ", idx)
            lista_text[idx+1] = "\n"
    print(len("".join(lista_text)))

    with open(dest, 'w') as fp:
        fp.write("".join(lista_text))


def convert(orig_ann, orig_txt, dest):
    transformar_txt(orig_txt,dest)
   # get_tokens(orig_txt)


if __name__ == '__main__':
    args = create_arguments()
    convert(args.origen_ann[0], args.origen_txt[0], args.destination[0])
