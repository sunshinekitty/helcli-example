def setup(parser, subparsers):
    parser_test = subparsers.add_parser(
        'test',
        help='Prints success for testing')


def main(parser, config):
    print("success")
