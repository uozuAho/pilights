import argparse

class ArgParser:
    def __init__(self, description):
        self.description = description

    def parse_args(self):
        arg_parser = argparse.ArgumentParser(description=self.description)
        arg_parser.add_argument('--host', help='set the host address of the server, ' +
            'eg. 0.0.0.0 to accept external requests')
        arg_parser.add_argument('--device', help='set the display device (default: %(default)s)',
            choices=['pygame', 'arduino', 'phat'],
            default='pygame')
        return arg_parser.parse_args()
