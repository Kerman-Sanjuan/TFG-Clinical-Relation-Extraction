import argparse


def create_arguments(): 
    parser = argparse.ArgumentParser(
        description='Print confussion matrix between to JSON files.')
    parser.add_argument('--o', dest='origen', nargs='+',
                        help='Path to JSON Real predictions') 
    parser.add_argument('--d', dest='destination', nargs='+',
                        help='Path to JSON Predicted')
    args = parser.parse_args()
    return args

