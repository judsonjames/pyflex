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

verb_count = 0
verb_list = []

def IncrementVerbCounter(text):
  global verb_count
  global verb_list
  verb_count += 1
  verb_list.append(text)

def PrintVerbCount():
  print("Found " + str(verb_count) + " verbs!")
  print(verb_list)

@atexit.register
def EndProgram() -> None:
  PrintVerbCount()



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
                if re.match(pattern='[a-zA-Z]*_[^Nn\t\n]*[V]+[^Nn\t\n]*', string=word) is not None:
                    IncrementVerbCounter(word)
################################################################################
# END GENERATED CODE
################################################################################
