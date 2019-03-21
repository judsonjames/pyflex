###############################################################################
# Authors: Judson James, Peyton Chandarana
# Purpose: Driver program for the PyFlex interpretter and Analyzer
import sys
from parser import Parser
from symbol_table import SymbolTable

def main() -> None:
    # The first thing to do is get the lines of the PyFlex file we are given.
    parser = Parser()
    parsed_data = parser.ParseFile(filename=sys.argv[1])

    print('RULESET')
    for value in parsed_data['ruleset']:
        print(value)

    print('INSTRUCTIONS')
    for value in parsed_data['instructions']:
        print(value)

    print('CODE')
    for value in parsed_data['code']:
        print(value)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <pyflex_file>")
        print("Your arguments were: {}".format(sys.argv))
    elif sys.argv[1].split('.')[1] != 'pyfl':
        print("Invalid argument: {}, must be of filetype <filename>.pyfl"
              .format(sys.argv[1]))
    else:
        main()
