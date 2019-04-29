###############################################################################
# Authors: Judson James, Peyton Chandarana
# Purpose: Driver program for the PyFlex interpretter and Analyzer
import os
import re
import sys
import atexit
import autopep8
from pytils import EasyFileIO
from pyflex_libs import SymbolTable
from pyflex_libs import Parser
from pyflex_libs import Generator


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
    # SymbolTable.PrintTable()

    # Using the Generator backend, we can build the generated script
    generator = Generator()
    generator.GenerateNewScript()

    autopep8.fix_file(filename=generator.file_main)

    print("Generated Script can be found in {}".format(generator.file_main))

###############################################################################
# Main Functionality
# Checks for input:
#   - Confirms that there are three arguments
#   - Confirms that the second argument is the pyflex file
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 main.py {}".format('<pyflex_file>'))
        print("Your arguments were: {}".format(sys.argv))
    elif sys.argv[1].split('.')[1] != 'pyfl':
        print("Invalid argument: {}, must be of filetype <filename>.pyfl"
              .format(sys.argv[1]))
    else:
        main()
