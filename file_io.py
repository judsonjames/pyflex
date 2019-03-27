###############################################################################
# Author:  Judson James
# Purpose: Simple library to return lines of a file
#          This was borrowed from Judson' personal stash of helper functions.
import os


class EasyFileIO():
    """ Easy File IO
    A simple library used for various functions I was too lazy to rewrite over
    and over again.
    """
    @staticmethod
    def CopyFile(original: str, copy: str) -> None:
        """ Copy File
        Given an original file path and a destination file path, this method
        will create a copy of a file verbatem.
        """
        lines = FileReader.FileToLines(filename=original)
        FileWriter.LinesToFile(filename=copy, lines=lines)


class FileReader():
    """ File Reader
    A class written for easy usage of File IO in Python. Some examples of
    this include a simple FileToLines method to load the lines of a file as
    a list.
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


class FileWriter():
    """ File Writer
    A simple class written for easy File writing. For example,
    LinesToFile is used to create a new file given a file name and a list of
    strings.
    """
    @staticmethod
    def LinesToFile(filename: str, lines: list()) -> None:
        """ File To Lines
        Function that writes list of strings to a file.
        Simple function but is used to prevent duplication.
        """
        with open(filename, 'w') as f:
            f.writelines(lines)

# class FileWriter():
#     """ File Writer
#     NOTE THIS IS NOT CORRECT, WILL UPDATE WHEN FINISHED WITH OTHER STUFF
#     """
#     def __init__(self, out_file='out.txt', log_file='log.txt'):
#         self.out_file = out_file
#         self.log_file = log_file

#         if os.path.isfile(out_file):
#             open(self.out_file, 'w').close()

#         if os.path.isfile(log_file):
#             open(self.log_file, 'w').close()

#     def Log(self, place='', msg='') -> None:
#         with open(self.log_file, 'w+') as f:
#             f.writelines('{}:\t{}'.format(place, msg))

#     def Out(self, place='', msg='') -> None:
#         with open(self.out_file, 'w+') as f:
#             f.writelines('{}:\t{}'.format(place, msg))
