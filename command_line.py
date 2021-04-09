import argparse
import sys

# to test: run "./command_line.py -i alpha -n time -n spacing
class parse:

    def getOptions(args=sys.argv[1:]):
        parser = argparse.ArgumentParser(description="Parses command.")
        parser.add_argument("-i", "--input", help="Your input file.")
        parser.add_argument("-o", "--output", help="Your destination output file.")
        parser.add_argument("-n", "--num0", type=int, help="A number.")
        parser.add_argument("-n", "--num1", type=int, help="A number.")
        parser.add_argument("-v", "--verbose", dest='verbose', action='store_true', help="Verbose mode.")
        opts = parser.parse_args(args)

        return opts

    options = getOptions(sys.argv[1:])

    alpha = options.input
    beta = options.output
    spacing = options.num0
    time = options.num1

    items = [alpha, beta, spacing, time]

    def get_input(items):
        return items

    #to test we are saving correct input
    def print_input(items):
        for x in items:
            print(x)