###############################################################################
# Authors: Judson James, Peyton Chandarana
# Purpose: Library used to read through a PyFlex file and create a custom
#          ruleset to fit the ReGex rules.
from enum import Enum
from pytils import EasyFileIO


class ParseState(Enum):
    RULES = 1
    INSTRUCTIONS = 2
    CODE = 3


class Parser():
    """ Parser
    Parser Object to parse a .pyflex file.
    """
    def __init__(self, filename: str):
        self.filename = filename
        self.ruleset_start = 0
        self.instruct_start = 0
        self.code_start = 0

    def ParseFile(self) -> dict:
        """ Parse File
        Main "driver" of the Parser Object.
        The program calls a number of 'private' methods to return a
        formated dictionary for 'ruleset', 'instructions', and 'code'.
        """
        file_lines = EasyFileIO.FileToLines(filename=self.filename)
        file_lines = self.__RemoveComments(file_lines)
        sections_dict = self.__SeparateBySections(file_lines)
        sections_dict = self.__FormatSections(sections_dict)
        return sections_dict

    def __RemoveComments(self, lines: list) -> list:
        """ Remove Comments
        Method to remove the commented lines from the file.
        The comments follow the style of Python. Using the '#' character.
        """
        no_comments = list()
        for line in lines:
            if line[0].strip(' \t') is '#':
                continue
            else:
                no_comments.append(line)
        return no_comments

    def __SeparateBySections(self, lines: list) -> dict:
        """ Separate By Sections
        Separate the lines by the following sections:
        ruleset, instructions, and code

        The three sections will be returned as a dictionary with the ids:

        'ruleset' | 'instructions' | 'code'
        """
        sections_dict = {'ruleset': [], 'instructions': [], 'code': []}
        section_state = ParseState.RULES

        #######################################################################
        # The for loop will encapsulate the sections given from the lines of
        # text. We will need to more 'deeply' parse each line when we interpret
        # rules. This simply gets the rules for the table. The code is not
        # to be formatted by us. We expect the users to write solid Pythonic
        # code.
        for i in range(0, len(lines)):
            p_line = lines[i].strip(' \n')
            if p_line == "%%" and section_state == ParseState.RULES:
                sections_dict['ruleset'] = lines[0:i]
                section_state = ParseState.INSTRUCTIONS
                self.instruct_start = i+1
            elif p_line == "%%" and section_state == ParseState.INSTRUCTIONS:
                sections_dict['instructions'] = lines[self.instruct_start:i]
                section_state = ParseState.CODE
                self.code_start = i+1
            elif section_state == ParseState.CODE:
                sections_dict['code'] = lines[self.code_start:]
                break
        return sections_dict

    def __FormatSections(self, sections_dict: dict) -> dict:
        """ Format Sections
        This method recieves the sections dictionary, which contains each
        section of the pyflex file, and reformats it such that their is a
        key and value to each line. I.E. Ruleset will have the name be the key,
        with the value being the regex, Instruction will have the filtered
        regex be the key and the Python call be the value.
        """
        ret_dict = {'ruleset': {}, 'instructions': {}, 'code': {}}

        #######################################################################
        # For parsing the 'ruleset', we will construct a list of size 2, where
        # the first element is the name of the rule, and the second element is
        # the regex associated. If the length is not equal to 2, the regex
        # contains a space, and will be merged. If there is a subexpression,
        # it will be matched with a currently existing rule and be inserted.
        for value in sections_dict['ruleset']:
            p_value = value.strip(' \n').split()
            if p_value != []:
                if len(p_value) is not 2:
                    # This is meant to mitigate issues with spaces within
                    # the regex NOTE will need to be extensively tested
                    if '[' in p_value[1] and ']' in p_value[-1]:
                        p_value[1] = " ".join(p_value[1:])
                        p_value = [p_value[0], p_value[1]]
                    elif '"' in p_value[1] and '"' in p_value[-1]:
                        p_value[1] = " ".join(p_value[1:])
                        p_value = [p_value[0], p_value[1]]
                if '{' in p_value[1] and '}' in p_value[1]:
                    key = p_value[1][p_value[1].find('{')+1:
                                     p_value[1].find('}')]

                    if ret_dict['ruleset'].get(key, None) is not None:
                        # This replaces the key with the regex
                        old = '{'+key+'}'
                        new = ret_dict['ruleset'][key]
                        p_value[1] = p_value[1].replace(old, new)
                    else:
                        print("Key: {} was not found, \
                               assume literal".format(key))
                # At this point we can safely update the ret_dict variable
                ret_dict['ruleset'].update({p_value[0]: p_value[1]})

        #######################################################################
        # For parsing the 'instructions', we will follow a similar methodology.
        # If there is a space in a specific string, join the list to create
        # two element lists.
        for value in sections_dict['instructions']:
            p_value = value.strip(' \n').split()
            if p_value != []:
                if len(p_value) is not 2:
                    # This case mitigates the space characters within the
                    # string for keys NOTE will need to be extensively tested
                    if '"' in p_value[0] and '"' in p_value[-2]:
                        p_value[0] = " ".join(p_value[:-1])
                        p_value = [p_value[0], p_value[-1]]
                if '{' in p_value[0] and '}' in p_value[0]:
                    key = p_value[0][p_value[0].find('{')+1:
                                     p_value[0].find('}')]
                    if ret_dict['ruleset'].get(key, None) is not None:
                        # This replaces the key with the regex
                        old = '{'+key+'}'
                        new = ret_dict['ruleset'][key]
                        p_value[0] = p_value[0].replace(old, new)
                    else:
                        print("Key: {} was not found, \
                               assume literal".format(key))
                ret_dict['instructions'].update({p_value[0]: p_value[1]})

        #######################################################################
        # We can just copy the code section of the input dictionary to the
        # output dictionary
        ret_dict['code'] = sections_dict['code']
        return ret_dict


if __name__ == "__main__":
    print("INCORRECT USAGE\nCorrect Usage: python3 main.py <pyflex_file>")
    exit(1)
