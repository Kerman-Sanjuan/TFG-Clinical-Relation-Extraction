import utils
from label_conversor import data


if __name__ == '__main__':
    args = utils.create_arguments()
    conversor = data(
        args.origen[0])
    conversor.unlabel_data()

