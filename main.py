###############################################################################
# Authors: Judson James, Peyton Chandarana
# Purpose: Driver program for the PyFlex interpretter and Analyzer
import os
import sys
import atexit
from parser import Parser
from symbol_table import SymbolTable
from file_io import FileWriter
from file_io import FileReader
from file_io import EasyFileIO


def main() -> None:
    """ main
    Driver function for PyFlex program
    """
    # The first thing to do is get the lines of the PyFlex file we are given.
    writer = FileWriter()
    parser = Parser(filename=sys.argv[1], writer=writer)
    parsed_data = parser.ParseFile()

    # Upon retrieving the Parsed Data, assign the parsed data to the
    # Symbol Table.
    SymbolTable.RULESET = parsed_data['ruleset']
    SymbolTable.INSTRUCTIONS = parsed_data['instructions']
    SymbolTable.CODE = parsed_data['code']

    # Print to confirm everything
    PrintTable(writer=writer)

    ###########################################################################
    # At this point, we will create a new meta folder, which will contain a
    # file that contains the Python code within the .pyflex file, a meta driver
    # file that will be templated with pre-written code, and
    # Creates the temporary Work Area for the PyFlex Interface
    meta_folder = 'meta_data'
    meta_main = 'meta_main.py'
    meta_code = 'meta_code.py'
    meta_main_path = '{}/{}'.format(meta_folder, meta_main)
    meta_code_path = '{}/{}'.format(meta_folder, meta_code)
    template_folder = 'templates'
    tempalte_main = 'template_driver.py'
    template_path = '{}/{}'.format(template_folder, tempalte_main)

    ###########################################################################
    # This is just a matter of making a clean slate to work with
    if os.path.isdir(meta_folder) is False:
        os.mkdir(meta_folder)
    if os.path.isdir(template_folder) is False:
        print('The templates folder does not exist. Please reclone.')
        exit(1)

    ###########################################################################
    # The following lines of code create the 'meta_code' that is generated from
    # our code.
    if os.path.isfile(template_path):
        EasyFileIO.CopyFile(original=template_path, copy=meta_main_path)
        FileWriter.LinesToFile(filename=meta_code_path,
                               lines=(lines for lines in SymbolTable.CODE))

    ###########################################################################
    # Used to test running a new Python environment to run the newly created
    # Python program
    os.system('python3 meta_data/meta_main.py')


def PrintTable(writer: FileWriter):
    """ Helper Function to Print the current state of the Symbol Table
    """
    print('RULESET')
    for key in SymbolTable.RULESET:
        print('{} {}'.format(key, SymbolTable.RULESET[key]))

    print('INSTRUCTIONS')
    for key in SymbolTable.INSTRUCTIONS:
        print('{} {}'.format(key, SymbolTable.INSTRUCTIONS[key]))

    print('CODE')
    for line in SymbolTable.CODE:
        print(line)


@atexit.register
def OnExit():
    print("End Program")

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
