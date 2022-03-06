import argparse
import sys
from sys import stderr, stdin
import re

def create_arguments():
    parser = argparse.ArgumentParser(
        description='Print confussion matrix between to JSON files.')
    parser.add_argument('--txt', dest='carpeta donde estan los txt', nargs='+',
                        help='Path where are the .txt file')
    args = parser.parse_args()
    print(args.origen_txt[0])
    return args




def transformar_txt(orig_txt):
    for file_path in (l.strip() for l in stdin):
        print(file_path)
        txt = open(file_path, "r")
        text = txt.read()
        txt.close()
        open(file_path, "w").close()
        lista_text = list(text)
        
        txt = open(file_path, "w")
        for idx, char in enumerate(text):
            if (len(text) - idx < 3):
                break
            if text[idx] == "." and text[idx+1] == " " and re.match("[A-Z]", text[idx+2]):
                print("Ha ocurrido en el idx: ", idx)
                lista_text[idx+1] = "\n"
        print(len("".join(lista_text)))
        txt.write("".join(lista_text))
    """

def convert(orig_ann, orig_txt, dest):
    transformar_txt(orig_txt)
    tokens = get_tokens(orig_txt)
    """
if __name__ == '__main__':
    from sys import argv
    transformar_txt(argv)