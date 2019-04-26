###############################################################################
# Authors: Judson James, Peyton Chandarana
# Purpose: Code Generator that creates the files to lexically analyze the
#          input file and call functions provided in the given pyflex file.
#
#
# NOTE we removed the option to output the code to a folder, it will be housed
# in a singular script for the time being
import os
from pytils import EasyFileIO


class Generator():
    """
    Class used to generate the code for the lexical analyzer.

    When initialized, a number of variables are created for house-keeping, as
    well as checking to making sure that the template folder is present and
    creating the generated Python program.
    """
    def __init__(self):
        # self.folder_main = folder
        self.folder_template = 'templates'
        self.file_main = 'generated_code.py'
        # self.file_meta = 'generated.py'
        self.file_temp = 'template_driver.py'
        # self.path_main = '{}/{}'.format(self.folder_main, self.file_main)
        self.path_template = '{}/{}'.format(self.folder_template, 
                                            self.file_temp)
        # self.path_meta = '{}/{}'.format(self.folder_main, self.file_meta)

        # System Checks
        self.__FolderCheck()

    ###########################################################################
    # The Following Methods are used for house-keeping.
    def __FolderCheck(self) -> None:
        """ Method used to a) create a generated code folder if it does not
        exist, and b) confirms that the template folder is present. If not,
        kill the program
        """
        # if os.path.isdir(self.folder_main) is False:
        #     os.mkdir(self.folder_main)
        if os.path.isdir(self.folder_template) is False:
            print('The templates folder does not exist. Please reclone.')
            exit(1)
