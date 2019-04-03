###############################################################################
# Authors: Judson James
# Purpose: Object used to contain data from a parsed PyFlex file


class SymbolTable(object):
    """ Symbol Table
    This static class contains the following variables:

    RULEST : dict() : two-layered dictionary containing the ruleset
    INSTRUCTIONS: dict() : two-layed dictionary containing parse instructions
    CODE: list() : list of strings that house the undoctored code in the file
    """
    RULESET = dict()
    INSTRUCTIONS = dict()
    CODE = list()

    @staticmethod
    def PrintTable() -> str:
        print('RULESET')
        for key in SymbolTable.RULESET:
            print('{} {}'.format(key, SymbolTable.RULESET[key]))

        print('INSTRUCTIONS')
        for key in SymbolTable.INSTRUCTIONS:
            print('{} {}'.format(key, SymbolTable.INSTRUCTIONS[key]))

        print('CODE')
        for line in SymbolTable.CODE:
            print(line)
