###############################################################################
# Authors: Judson James, Peyton Chandarana
# Purpose: Driver program for the PyFlex interpretter and Analyzer
import os
import sys
from parser import Parser
from symbol_table import SymbolTable


def main() -> None:
    # The first thing to do is get the lines of the PyFlex file we are given.
    parser = Parser(filename=sys.argv[1])
    parsed_data = parser.ParseFile()

    SymbolTable.ruleset = parsed_data['ruleset']
    SymbolTable.instructions = parsed_data['instructions']
    SymbolTable.code = parsed_data['code']
    PrintTable()


def PrintTable():
    print('RULESET')
    for key in SymbolTable.ruleset:
        print(key, SymbolTable.ruleset[key])

    print('\nINSTRUCTIONS')
    for key in SymbolTable.instructions:
        print(key, SymbolTable.instructions[key])

    print('\nCODE')
    for line in SymbolTable.code:
        print(line)

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python3 main.py {} {} {} {}".
              format('<pyflex_file>', '<input_file>',
                     '<output_file>', '<log_file>'))
        print("Your arguments were: {}".format(sys.argv))
    elif sys.argv[1].split('.')[1] != 'pyfl':
        print("Invalid argument: {}, must be of filetype <filename>.pyfl"
              .format(sys.argv[1]))
    elif os.path.isfile(sys.argv[2]) is False:
        print("Invalid argument: {}, must be an actual file."
              .format(sys.argv[2]))
    else:
        main()
