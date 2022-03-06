import utils
from Conversor.confusion_matrix import compute_matrix


if __name__ == '__main__':
    args = utils.create_arguments()
    conversor = compute_matrix(
        args.origen[0], args.destination[0])
    conversor.compute()
    #TODO:   #1. Cambiar el fichero de configuracion para que detecte los tipos que no estan incluidos dentro.
