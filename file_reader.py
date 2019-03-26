###############################################################################
# Author:  Judson James
# Purpose: Simple library to return lines of a file
#          This was borrowed from Judson' personal stash of helper functions.


class FileReader(object):
    """ File Reader
    """
    @staticmethod
    def FileToLines(filename: str) -> list:
        """ File To Lines
        Function that returns a list of strings that contains the data from a
        file. Simple function but is used to prevent duplication.
        """
        lines = list()
        with open(file=filename) as f:
            lines = f.readlines()
        return lines
