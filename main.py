###############################################################################
# Authors: Judson James, Peyton Chandarana
# Purpose: Driver program for the PyFlex interpretter and Analyzer
import os
import sys
import atexit
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

    generator = Generator()
    ###########################################################################
    # At this point, we will create a new meta folder, which will contain a
    # file that contains the Python code within the .pyflex file, a meta driver
    # file that will be templated with pre-written code, and
    # Creates the temporary Work Area for the PyFlex Interface
    #
    # NOTE not sure if this should be part of the Generator init, but
    # if not, it's fine here.
    if os.path.isfile(generator.path_template):
        EasyFileIO.CreateEmptyFile(filename=generator.file_main)
        EasyFileIO.LinesToFile(filename=generator.file_main,
                               lines=(lines for lines in SymbolTable.CODE))
        EasyFileIO.AppendToFile(filename=generator.file_main, lines=['\n'])
        EasyFileIO.AppendToFile(filename=generator.file_main,
                                lines=EasyFileIO.FileToLines(generator.path_template))
        #######################################################################
        # This is outdated for the time being
        # EasyFileIO.CopyFile(original=generator.path_temp,
        #                     copy=generator.path_main)

    ###########################################################################
    # Used to test running a new Python environment to run the newly created
    # Python program
    print("Entering Subprocess")
    os.system('python3 generated_code.py')


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
