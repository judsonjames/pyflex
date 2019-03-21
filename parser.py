###############################################################################
# Authors: Judson James, Peyton Chandarana
# Purpose: Library used to read through a PyFlex file and create a custom
#          ruleset to fit the ReGex rules.
from enum import Enum
from file_reader import FileReader


class ParseState(Enum):
    RULES = 1
    INSTRUCTIONS = 2
    CODE = 3


class Parser():
    """ Parser
    """

    def ParseFile(self, filename: str) -> dict:
        file_lines = FileReader.FileToLines(filename=filename)
        file_lines = self.RemoveComments(file_lines)
        sections_dict = self.SeparateBySections(file_lines)
        return sections_dict

    def RemoveComments(self, lines: list) -> list:
        """ Remove Comments
        Method to remove the commented lines from the file.
        The comments follow the style of Python. Using the '#' character.
        """
        no_comments = list()
        for line in lines:
            if line[0].strip(' \t') is '#':
                continue
            else:
                no_comments.append(line.strip(' \n'))
        return no_comments

    def SeparateBySections(self, lines: list) -> dict:
        """ Separate By Sections
        Separate the lines by the following sections:
        ruleset, instructions, and code

        The three sections will be returned as a dictionary with the ids:

        'ruleset' | 'instructions' | 'code'
        """
        sections_dict = {'ruleset': [], 'instructions': [], 'code': []}
        section_state = ParseState.RULES

        #######################################################################
        # The for loop will encapsulate the 'ruleset' and 'instructions' given
        # from the lines of text
        for i in range(0, len(lines)):
            if lines[i] == "%%" and section_state == ParseState.RULES:
                sections_dict['ruleset'] = lines[0:i]
                section_state = ParseState.INSTRUCTIONS
            elif lines[i] == "%%" and section_state == ParseState.INSTRUCTIONS:
                sections_dict['instructions'] = \
                        lines[len(sections_dict['ruleset'])+1:i]
                section_state = ParseState.CODE

        #######################################################################
        # Given that the for loop does not encapsulate the 'code' section, we
        # must encapsulate the remaining lines as 'code' manually
        temp_length = (len(sections_dict['ruleset']) +
                       len(sections_dict['instructions']))
        sections_dict['code'] = lines[temp_length+2:len(lines)]
        return sections_dict

if __name__ == "__main__":
    print("INCORRECT USAGE\nCorrect Usage: python3 main.py <pyflex_file>")
