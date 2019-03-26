###############################################################################
# Authors: Judson James, Peyton Chandarana
# Purpose: Driver program for the PyFlex interpretter and Analyzer
import os
import sys
from parser import Parser
from symbol_table import SymbolTable


def main() -> None:
    """ main
    Driver function for PyFlex program
    """
    # The first thing to do is get the lines of the PyFlex file we are given.
    parser = Parser(filename=sys.argv[1])
    parsed_data = parser.ParseFile()

    # Upon retrieving the Parsed Data, assign the parsed data to the 
    # Symbol Table.
    SymbolTable.RULESET = parsed_data['ruleset']
    SymbolTable.INSTRUCTIONS = parsed_data['instructions']
    SymbolTable.CODE = parsed_data['code']
    
    # Print to confirm everything
    PrintTable()


def PrintTable():
    """ Helper Function to Print the current state of the Symbol Table
    """
    print('RULESET')
    for key in SymbolTable.RULESET:
        print(key, SymbolTable.RULESET[key])

    print('\nINSTRUCTIONS')
    for key in SymbolTable.INSTRUCTIONS:
        print(key, SymbolTable.INSTRUCTIONS[key])

    print('\nCODE')
    for line in SymbolTable.CODE:
        print(line)

###############################################################################
# Main Functionality
# Checks for input:
#   - Confirms that there are three arguments
#   - Confirms that the second argument is the pyflex file
#   - Confirms that the third argument is an existing input file
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 main.py {} {}".
              format('<pyflex_file>', '<input_file>'))
        print("Your arguments were: {}".format(sys.argv))
    elif sys.argv[1].split('.')[1] != 'pyfl':
        print("Invalid argument: {}, must be of filetype <filename>.pyfl"
              .format(sys.argv[1]))
    elif os.path.isfile(sys.argv[2]) is False:
        print("Invalid argument: {}, must be an actual file."
              .format(sys.argv[2]))
    else:
        main()
