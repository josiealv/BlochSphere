import getopt
import sys

# to test: run command_line.py [alpha [alpha] beta [beta] [parameter1] [parameter2] [...]
class parse():

argv = sys.argv[1:]

opts, args = getopt.getopt(argv, 'alpha:beta')

alpha = argv[1]
beta = argv[2]

spacing = argv[3]
time = argv[4]

#pass into bloch.py

# list of options tuple (opt, value)
#print(f'Closed form wave vector {opts}')

# list of remaining command-line arguments
#print(f'With parameters {args}')