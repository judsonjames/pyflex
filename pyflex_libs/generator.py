###############################################################################
# Authors: Judson James, Peyton Chandarana
# Purpose: Code Generator that creates the files to lexically analyze the
#          input file and call functions provided in the given pyflex file.
#
#
# NOTE we removed the option to output the code to a folder, it will be housed
# in a singular script for the time being
import os
import re
from pyflex_libs.symbol_table import SymbolTable
from pytils import EasyFileIO


class Generator():
    """
    Class used to generate the code for the lexical analyzer.

    When initialized, a number of variables are created for house-keeping, as
    well as checking to making sure that the template folder is present and
    creating the generated Python program.
    """
    def __init__(self, output_file_name='generated_code.py'):
        self.file_main = output_file_name

    def GenerateNewScript(self):
        EasyFileIO.CreateEmptyFile(filename=self.file_main)

        # Inputs the headers to the generated code
        line = 'line'
        word = 'word'
        delim = ' '
        long_line = '#'*80
        tab = ' '*4
        header_lines = [
            long_line,
            '# START GENERATED HEADER',
            'import sys',
            'import os',
            'import re',
            '# END GENERATED HEADER',
            long_line,
        ]
        driver_lines = [
            long_line,
            '# GENERATED DRIVER',
            long_line,
            "if __name__ == '__main__':",
            "{}for files in sys.argv[1:]:".format(tab*1),
            "{}print('FILE: {}'.format(files))".format(tab*2, '{}'),
            "{}lines_from_file = []".format(tab*2),
            "{}with open(file=sys.argv[1]) as f:".format(tab*2),
            "{}lines = f.readlines()".format(tab*3),
            "{}for {} in lines:".format(tab*2, line),
            "{}for {} in {}.split('{}'):".format(tab*3, word, line, delim),
        ]
        EasyFileIO.AppendToFile(filename=self.file_main, lines=header_lines)
        EasyFileIO.AppendToFile(filename=self.file_main, lines=['\n\n'])
        user_lines = [
            long_line,
            '# CODE PROVIDED FROM PYFLEX FILE',
            long_line,
        ]
        EasyFileIO.AppendToFile(filename=self.file_main, lines=user_lines)
        EasyFileIO.AppendToFile(filename=self.file_main,
                                lines=(lines for lines in SymbolTable.CODE),
                                new_line=False)
        EasyFileIO.AppendToFile(filename=self.file_main, lines=['\n\n'])
        EasyFileIO.AppendToFile(filename=self.file_main, lines=driver_lines)

        # Goes through every rule and instruction to append to the thing
        statements = []
        for rule in SymbolTable.INSTRUCTIONS:
            parenthesis = r'\(([^\)]+)\)'
            instruction = SymbolTable.INSTRUCTIONS[rule]
            instruction = re.sub(pattern=parenthesis, repl='({})'.format(word),
                                 string=instruction)
            condition = "{}if re.match(pattern='{}', string={}) is not None:"\
                .format(tab*4, rule, word)
            consequent = '{}{}'.format(tab*5, instruction)
            statements.append(condition)
            statements.append(consequent)

        EasyFileIO.AppendToFile(filename=self.file_main, lines=statements)

        end_lines = [
            long_line,
            '# END GENERATED CODE',
            long_line,
        ]
        EasyFileIO.AppendToFile(filename=self.file_main, lines=end_lines)
    ###########################################################################
    # NOTE DEPRECATED
    # The Following Methods are used for house-keeping.
    # def __FolderCheck(self) -> None:
    #     """ Method used to a) create a generated code folder if it does not
    #     exist, and b) confirms that the template folder is present. If not,
    #     kill the program
    #     """
    #     # if os.path.isdir(self.folder_main) is False:
    #     #     os.mkdir(self.folder_main)
    #     if os.path.isdir(self.folder_template) is False:
    #         print('The templates folder does not exist. Please reclone.')
    #         exit(1)
