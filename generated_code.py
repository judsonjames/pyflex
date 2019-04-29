################################################################################
# START GENERATED HEADER
import sys
import os
import re
# END GENERATED HEADER
################################################################################



################################################################################
# CODE PROVIDED FROM PYFLEX FILE
################################################################################

import atexit

class Collection(object):
    VERBS = list()

@atexit.register
def EndProgram() -> None:
    print("Number of Verbs: {}".format(len(Collection.VERBS)))
    print("End Program")

def AddVerb(text: str) -> None:
    Collection.VERBS.append(text)
    


################################################################################
# GENERATED DRIVER
################################################################################
if __name__ == '__main__':
    for files in sys.argv[1:]:
        print('FILE: {}'.format(files))
        lines_from_file = []
        with open(file=sys.argv[1]) as f:
            lines = f.readlines()
        for line in lines:
            for word in line.split(' '):
                if re.match(pattern='[a-zA-Z]*_[a-zA-Z]*V[a-zA-Z]*', string=word) is not None:
                    AddVerb(word)
################################################################################
# END GENERATED CODE
################################################################################
