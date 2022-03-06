import utils
import Conversor.json_to_ann_V2


if __name__ == '__main__':
    args = utils.create_arguments()
    conversor = Conversor.json_to_ann_V2.conversor(
        args.origen[0], args.destination[0])
    conversor.convertor()
