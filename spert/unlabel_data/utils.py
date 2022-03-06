import argparse


def create_arguments():
    parser = argparse.ArgumentParser(
        description='Unlabel the data from SPERT JSON-parsed dataset')
    parser.add_argument('--o', dest='origen', nargs='+',
                        help='Path to JSON with labeled data')
    args = parser.parse_args()
    return args
